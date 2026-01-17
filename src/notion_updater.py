"""Notion Updater Module - Atualiza páginas do Notion com classificação."""

import os
import logging
from typing import Dict, Optional
from notion_client import Client
from datetime import datetime

logger = logging.getLogger(__name__)


class NotionUpdater:
    """Cliente para atualizar páginas do Notion."""
    
    def __init__(self, api_key: Optional[str] = None, database_id: Optional[str] = None):
        """
        Inicializa o cliente do Notion.
        
        Args:
            api_key: Notion API token (opcional, usa env var)
            database_id: ID da database (opcional, usa env var)
        """
        self.api_key = api_key or os.getenv('NOTION_API_KEY') or os.getenv('NOTION_TOKEN')
        self.database_id = database_id or os.getenv('NOTION_DATABASE_ID') or os.getenv('NOTION_DB_ID')
        
        if not self.api_key:
            raise ValueError("Notion API key não fornecida")
        
        self.client = Client(auth=self.api_key)
    
    def update_page(self, page_id: str, classification: Dict) -> bool:
        """
        Atualiza uma página do Notion com classificação.
        
        IMPORTANTE: Faz APPEND ao campo Notes, não sobrescreve!
        
        Args:
            page_id: ID da página no Notion
            classification: Dict com priority, priority_label, notes_reason, etc.
            
        Returns:
            True se atualizado com sucesso
        """
        try:
            logger.info(f"Atualizando página {page_id}...")
            
            # 1. Primeiro, obtém o conteúdo atual da página
            page = self.client.pages.retrieve(page_id=page_id)
            
            # 2. Extrai o Notes atual (se existir)
            existing_notes = self._get_existing_notes(page)
            
            # 3. Monta o novo conteúdo do Notes (APPEND)
            new_notes_content = self._build_notes_content(classification)
            
            # 4. Combina Notes existente + novo conteúdo
            if existing_notes and existing_notes.strip():
                # APPEND: adiciona ao final do Notes existente
                combined_notes = f"{existing_notes}\n\n{new_notes_content}"
                logger.info("Adicionando classificação ao Notes existente (APPEND)")
            else:
                combined_notes = new_notes_content
                logger.info("Criando novo Notes (não havia conteúdo anterior)")
            
            # 5. Prepara propriedades para atualizar
            properties = self._build_properties(classification, combined_notes)
            
            # 6. Atualiza a página
            self.client.pages.update(page_id=page_id, properties=properties)
            
            logger.info(f"Página {page_id} atualizada com sucesso")
            return True
            
        except Exception as e:
            logger.error(f"Erro ao atualizar página {page_id}: {str(e)}")
            raise
    
    def _get_existing_notes(self, page: Dict) -> str:
        """
        Extrai o conteúdo atual do campo Notes.
        
        Args:
            page: Objeto da página do Notion
            
        Returns:
            Texto do Notes ou string vazia
        """
        try:
            properties = page.get('properties', {})
            notes_prop = properties.get('Notes', properties.get('notes', {}))
            
            # Pode ser rich_text ou text
            if notes_prop.get('type') == 'rich_text':
                rich_texts = notes_prop.get('rich_text', [])
                if rich_texts:
                    # Concatena todos os textos
                    return ''.join([rt.get('plain_text', '') for rt in rich_texts])
            
            return ''
            
        except Exception as e:
            logger.warning(f"Erro ao extrair Notes existente: {e}")
            return ''
    
    def _build_notes_content(self, classification: Dict) -> str:
        """
        Constrói o conteúdo a ser adicionado ao Notes.
        
        Args:
            classification: Dict com a classificação
            
        Returns:
            Texto formatado para adicionar ao Notes
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')
        
        content_parts = [
            f"[Classificação Automática - {timestamp}]",
            f"Priority: {classification.get('priority')} ({classification.get('priority_label', '')})"
        ]
        
        # Adiciona subcategoria se presente
        if classification.get('sub_category'):
            sub_label = classification.get('sub_category_label', '')
            content_parts.append(
                f"Subcategoria: {classification['sub_category']} - {sub_label}"
            )
        
        # Adiciona justificativa
        if classification.get('notes_reason'):
            content_parts.append(f"\nJustificativa: {classification['notes_reason']}")
        
        return '\n'.join(content_parts)
    
    def _build_properties(self, classification: Dict, combined_notes: str) -> Dict:
        """
        Constrói o objeto de propriedades para atualizar o Notion.
        
        Args:
            classification: Classificação do mod
            combined_notes: Notes combinado (existente + novo)
            
        Returns:
            Dict de propriedades no formato do Notion
        """
        properties = {}
        
        # Priority (select)
        if 'priority' in classification:
            properties['Priority'] = {
                'select': {'name': str(classification['priority'])}
            }
        
        # Priority Label (select)
        if 'priority_label' in classification:
            properties['Priority Label'] = {
                'select': {'name': classification['priority_label']}
            }
        
        # Notes (rich_text) - COMBINADO com conteúdo existente
        properties['Notes'] = {
            'rich_text': [
                {
                    'type': 'text',
                    'text': {'content': combined_notes[:2000]}  # Notion limit
                }
            ]
        }
        
        return properties
    
    def get_page(self, page_id: str) -> Dict:
        """
        Obtém uma página do Notion.
        
        Args:
            page_id: ID da página
            
        Returns:
            Objeto da página
        """
        try:
            return self.client.pages.retrieve(page_id=page_id)
        except Exception as e:
            logger.error(f"Erro ao obter página {page_id}: {e}")
            raise


def update_notion_page(page_id: str, 
                       classification: Dict,
                       api_key: Optional[str] = None,
                       database_id: Optional[str] = None) -> bool:
    """
    Função de conveniência para atualizar página do Notion.
    
    Args:
        page_id: ID da página no Notion
        classification: Classificação do mod
        api_key: API key (opcional)
        database_id: Database ID (opcional)
        
    Returns:
        True se atualizado com sucesso
    """
    updater = NotionUpdater(api_key=api_key, database_id=database_id)
    return updater.update_page(page_id, classification)
