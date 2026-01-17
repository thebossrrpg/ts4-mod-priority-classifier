#!/usr/bin/env python3
"""
TS4 Mod Priority Classifier - Main Pipeline

Este script automatiza o processo de classificação de prioridade de mods do The Sims 4:
1. Extrai conteúdo da página do mod
2. Envia para o LLM para classificação
3. Atualiza a database do Notion com prioridade e notas
"""

import os
import sys
import logging
from dotenv import load_dotenv

# Importa os módulos implementados
from web_scraper import extract_mod_content
from llm_client import classify_with_llm
from notion_updater import update_notion_page

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Carregar variáveis de ambiente
load_dotenv()


class ModClassifierPipeline:
    """Pipeline principal para classificação de mods."""
    
    def __init__(self):
        """
        Inicializa o pipeline.
        Verifica se as variáveis de ambiente necessárias estão configuradas.
        """
        # Verifica variáveis essenciais
        self.notion_token = os.getenv('NOTION_API_KEY') or os.getenv('NOTION_TOKEN')
        self.notion_database_id = os.getenv('NOTION_DATABASE_ID') or os.getenv('NOTION_DB_ID')
        self.llm_api_key = os.getenv('LLM_API_KEY')
        self.llm_model = os.getenv('LLM_MODEL', 'gpt-4o')
        
        if not self.notion_token:
            logger.warning("NOTION_API_KEY não configurada - atualização do Notion será desabilitada")
        
        if not self.llm_api_key:
            logger.warning("LLM_API_KEY não configurada - classificação LLM será desabilitada")
        
        logger.info(f"Pipeline inicializado com modelo: {self.llm_model}")
    
    def process_mod(self, mod_url: str, notion_page_id: str = None) -> dict:
        """
        Processa um mod completo: extração -> classificação -> atualização Notion.
        
        Args:
            mod_url: URL da página do mod
            notion_page_id: ID da página no Notion (opcional)
            
        Returns:
            dict: Classificação do mod
        """
        try:
            logger.info("="*70)
            logger.info(f"Iniciando processamento do mod: {mod_url}")
            logger.info("="*70)
            
            # PASSO 1: Extrair conteúdo da página
            logger.info("[1/3] Extraindo conteúdo da página...")
            mod_content = extract_mod_content(mod_url)
            logger.info(f"     ✓ Extraído: {mod_content['title']}")
            logger.info(f"     Total de palavras: {mod_content['word_count']}")
            
            # PASSO 2: Classificar com LLM
            logger.info("[2/3] Classificando mod com LLM...")
            classification = classify_with_llm(mod_content)
            logger.info(f"     ✓ Priority: {classification['priority']} ({classification.get('priority_label', '')})")
            if classification.get('sub_category'):
                logger.info(f"     ✓ Sub: {classification['sub_category']} - {classification.get('sub_category_label', '')}")
            
            # PASSO 3: Atualizar Notion (se page_id fornecido)
            if notion_page_id and self.notion_token:
                logger.info(f"[3/3] Atualizando Notion page {notion_page_id}...")
                update_notion_page(notion_page_id, classification)
                logger.info("     ✓ Página do Notion atualizada com sucesso (APPEND ao Notes)")
            elif notion_page_id and not self.notion_token:
                logger.warning("     ⚠ NOTION_API_KEY não configurada - pulando atualização")
            else:
                logger.info("     - Notion page ID não fornecido, pulando atualização")
            
            logger.info("="*70)
            logger.info("✅ Processamento concluído com sucesso!")
            logger.info("="*70)
            
            return classification
            
        except Exception as e:
            logger.error(f"❌ Erro ao processar mod: {str(e)}")
            logger.exception(e)
            raise


def main():
    """
    Função principal do script.
    """
    if len(sys.argv) < 2:
        print("""\nUso: python main.py <mod_url> [notion_page_id]
        
Exemplos:
  python main.py "https://modthesims.info/d/12345"
  python main.py "https://modthesims.info/d/12345" "abc123def456"
  
Variaveis de ambiente necessárias:
  LLM_API_KEY        - API key do provedor LLM
  LLM_MODEL          - Modelo LLM (padrão: gpt-4o)
  NOTION_API_KEY     - Token de integração do Notion
  NOTION_DATABASE_ID - ID da database do Notion (opcional)
        """)
        sys.exit(1)
    
    mod_url = sys.argv[1]
    notion_page_id = sys.argv[2] if len(sys.argv) > 2 else None
    
    try:
        pipeline = ModClassifierPipeline()
        result = pipeline.process_mod(mod_url, notion_page_id)
        
        # Exibe resultado formatado
        print("\n" + "="*70)
        print("🎮  RESULTADO DA CLASSIFICAÇÃO")
        print("="*70)
        print(f"\nPrioridade: {result['priority']} ({result.get('priority_label', '')})")
        
        if result.get('sub_category'):
            print(f"Sub-categoria: {result['sub_category']} - {result.get('sub_category_label', '')}")
        
        print(f"\nJustificativa:")
        print(f"{result.get('notes_reason', 'N/A')}")
        print("\n" + "="*70 + "\n")
        
        sys.exit(0)
        
    except Exception as e:
        logger.error(f"Erro fatal: {str(e)}")
        sys.exit(1)


if __name__ == '__main__':
    main()
