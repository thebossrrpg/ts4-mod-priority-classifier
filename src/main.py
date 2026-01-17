#!/usr/bin/env python3
"""
TS4 Mod Priority Classifier - Main Pipeline

Este script automatiza o processo de classificação de prioridade de mods do The Sims 4:
1. Extrai conteúdo da página do mod
2. Envia para o LLM (NotebookLM ou API) para classificação
3. Atualiza a database do Notion com prioridade e notas
"""

import os
import sys
from dotenv import load_dotenv
import logging

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
        self.notion_token = os.getenv('NOTION_TOKEN')
        self.notion_database_id = os.getenv('NOTION_DATABASE_ID')
        self.llm_api_key = os.getenv('LLM_API_KEY')
        
        if not all([self.notion_token, self.notion_database_id]):
            raise ValueError("Variáveis de ambiente NOTION_TOKEN e NOTION_DATABASE_ID são obrigatórias")
    
    def extract_mod_content(self, mod_url):
        """
        Extrai conteúdo da página do mod.
        
        Args:
            mod_url: URL da página do mod
            
        Returns:
            dict: Dicionário com informações do mod (nome, descrição, etc.)
        """
        logger.info(f"Extraindo conteúdo de: {mod_url}")
        # TODO: Implementar extração com BeautifulSoup ou Playwright
        return {
            'url': mod_url,
            'content': 'Conteúdo extraído da página'
        }
    
    def classify_mod(self, mod_content):
        """
        Classifica o mod usando LLM com base no roteiro estruturado.
        
        Args:
            mod_content: Conteúdo do mod para análise
            
        Returns:
            dict: Classificação com priority, priority_label e notes_reason
        """
        logger.info("Classificando mod com LLM...")
        # TODO: Implementar chamada para API do LLM (OpenAI, Anthropic, etc.)
        # Carregar o prompt do classificador de prompts/classificador-mods-ts4-prompt.md
        
        return {
            'priority': 3,
            'priority_label': 'Verde',
            'sub_category': '3C',
            'sub_category_label': 'Família & Relações Pontuais',
            'notes_reason': 'Justificativa da classificação baseada na análise do LLM'
        }
    
    def update_notion(self, page_id, classification):
        """
        Atualiza a página do Notion com a classificação.
        
        Args:
            page_id: ID da página no Notion
            classification: Dicionário com a classificação
        """
        logger.info(f"Atualizando Notion page {page_id}...")
        # TODO: Implementar atualização via Notion API
        # Importante: ACRESCENTAR ao Notes existente, não sobrescrever
        pass
    
    def process_mod(self, mod_url, notion_page_id):
        """
        Processa um mod completo: extração -> classificação -> atualização Notion.
        
        Args:
            mod_url: URL da página do mod
            notion_page_id: ID da página no Notion
        """
        try:
            # 1. Extrair conteúdo
            mod_content = self.extract_mod_content(mod_url)
            
            # 2. Classificar com LLM
            classification = self.classify_mod(mod_content)
            
            # 3. Atualizar Notion
            self.update_notion(notion_page_id, classification)
            
            logger.info(f"Mod processado com sucesso: {mod_url}")
            return classification
            
        except Exception as e:
            logger.error(f"Erro ao processar mod {mod_url}: {str(e)}")
            raise


def main():
    """
    Função principal do script.
    """
    if len(sys.argv) < 3:
        print("Uso: python main.py <mod_url> <notion_page_id>")
        sys.exit(1)
    
    mod_url = sys.argv[1]
    notion_page_id = sys.argv[2]
    
    pipeline = ModClassifierPipeline()
    result = pipeline.process_mod(mod_url, notion_page_id)
    
    print(f"\nClassificação concluída:")
    print(f"Prioridade: {result['priority']} ({result['priority_label']})")
    print(f"Sub-categoria: {result['sub_category']} - {result['sub_category_label']}")
    print(f"Justificativa: {result['notes_reason']}")


if __name__ == '__main__':
    main()
