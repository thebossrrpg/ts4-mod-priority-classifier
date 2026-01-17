"""Web Scraper Module - Extrai conteúdo de páginas de mods."""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import logging
from typing import Dict, Optional

logger = logging.getLogger(__name__)


class WebScraper:
    """Classe para extração de conteúdo de páginas web."""
    
    def __init__(self, timeout: int = 30):
        """
        Inicializa o scraper.
        
        Args:
            timeout: Timeout para requisições HTTP em segundos
        """
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def extract_content(self, url: str) -> Dict[str, str]:
        """
        Extrai conteúdo de uma página de mod.
        
        Args:
            url: URL da página do mod
            
        Returns:
            Dicionário com url, title, description e full_text
            
        Raises:
            requests.RequestException: Se houver erro na requisição
        """
        try:
            logger.info(f"Extraindo conteúdo de: {url}")
            
            # Faz requisição HTTP
            response = self.session.get(url, timeout=self.timeout)
            response.raise_for_status()
            
            # Parse HTML
            soup = BeautifulSoup(response.content, 'lxml')
            
            # Remove scripts e styles
            for tag in soup(['script', 'style', 'nav', 'footer', 'header']):
                tag.decompose()
            
            # Extrai informações
            title = self._extract_title(soup)
            description = self._extract_description(soup)
            full_text = self._extract_text(soup)
            
            result = {
                'url': url,
                'title': title,
                'description': description,
                'full_text': full_text,
                'word_count': len(full_text.split())
            }
            
            logger.info(f"Extração concluída: {result['word_count']} palavras")
            return result
            
        except requests.Timeout:
            logger.error(f"Timeout ao acessar {url}")
            raise
        except requests.RequestException as e:
            logger.error(f"Erro ao acessar {url}: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Erro inesperado: {str(e)}")
            raise
    
    def _extract_title(self, soup: BeautifulSoup) -> str:
        """Extrai o título da página."""
        # Tenta várias opções de título
        title = None
        
        # Meta title ou og:title
        meta_title = soup.find('meta', property='og:title')
        if meta_title and meta_title.get('content'):
            title = meta_title['content']
        
        # Tag title
        if not title and soup.title:
            title = soup.title.string
        
        # H1
        if not title:
            h1 = soup.find('h1')
            if h1:
                title = h1.get_text(strip=True)
        
        return title or 'Sem título'
    
    def _extract_description(self, soup: BeautifulSoup) -> str:
        """Extrai a descrição da página."""
        # Tenta meta description
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        if meta_desc and meta_desc.get('content'):
            return meta_desc['content']
        
        # Tenta og:description
        og_desc = soup.find('meta', property='og:description')
        if og_desc and og_desc.get('content'):
            return og_desc['content']
        
        # Primeiro parágrafo
        p = soup.find('p')
        if p:
            return p.get_text(strip=True)[:500]
        
        return ''
    
    def _extract_text(self, soup: BeautifulSoup) -> str:
        """Extrai todo o texto relevante da página."""
        # Tenta encontrar conteúdo principal
        main_content = None
        
        # Procura por tags comuns de conteúdo
        for selector in ['article', 'main', '[role="main"]', '.content', '#content']:
            main_content = soup.select_one(selector)
            if main_content:
                break
        
        # Se não encontrou, usa body
        if not main_content:
            main_content = soup.find('body')
        
        if main_content:
            # Extrai texto com espaços entre elementos
            text = main_content.get_text(separator=' ', strip=True)
            # Limpa espaços múltiplos
            text = ' '.join(text.split())
            return text
        
        return ''
    
    def close(self):
        """Fecha a sessão HTTP."""
        self.session.close()


def extract_mod_content(url: str) -> Dict[str, str]:
    """
    Função de conveniência para extrair conteúdo de mod.
    
    Args:
        url: URL da página do mod
        
    Returns:
        Dicionário com informações do mod
    """
    scraper = WebScraper()
    try:
        return scraper.extract_content(url)
    finally:
        scraper.close()
