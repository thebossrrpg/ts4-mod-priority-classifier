"""LLM Client Module - Integração com vários provedores de LLM."""

import os
import logging
import json
from typing import Dict, Optional
from pathlib import Path

logger = logging.getLogger(__name__)


class LLMClient:
    """Cliente unificado para múltiplos provedores de LLM."""
    
    def __init__(self, api_key: Optional[str] = None, model: Optional[str] = None):
        """
        Inicializa o cliente LLM.
        
        Args:
            api_key: API key do provedor (opcional, usa env var)
            model: Nome do modelo (opcional, usa env var)
        """
        self.api_key = api_key or os.getenv('LLM_API_KEY')
        self.model = model or os.getenv('LLM_MODEL', 'gpt-4o')
        
        if not self.api_key:
            raise ValueError("API key não fornecida")
        
        # Detecta provedor pelo modelo
        self.provider = self._detect_provider()
        self.client = self._init_client()
        
        # Carrega prompt do classificador
        self.classifier_prompt = self._load_classifier_prompt()
    
    def _detect_provider(self) -> str:
        """Detecta o provedor baseado no nome do modelo."""
        model_lower = self.model.lower()
        
        if any(x in model_lower for x in ['gpt', 'openai']):
            return 'openai'
        elif any(x in model_lower for x in ['claude', 'anthropic']):
            return 'anthropic'
        elif any(x in model_lower for x in ['gemini', 'google']):
            return 'google'
        else:
            logger.warning(f"Provedor desconhecido para modelo {self.model}, usando OpenAI")
            return 'openai'
    
    def _init_client(self):
        """Inicializa o cliente do provedor específico."""
        try:
            if self.provider == 'openai':
                from openai import OpenAI
                return OpenAI(api_key=self.api_key)
            elif self.provider == 'anthropic':
                from anthropic import Anthropic
                return Anthropic(api_key=self.api_key)
            elif self.provider == 'google':
                import google.generativeai as genai
                genai.configure(api_key=self.api_key)
                return genai
            else:
                raise ValueError(f"Provedor {self.provider} não suportado")
        except ImportError as e:
            logger.error(f"Biblioteca do provedor não instalada: {e}")
            raise
    
    def _load_classifier_prompt(self) -> str:
        """Carrega o prompt do classificador de mods."""
        # Tenta encontrar o arquivo do prompt
        prompt_paths = [
            Path('prompts/classificador-mods-ts4-prompt.md'),
            Path('../prompts/classificador-mods-ts4-prompt.md'),
            Path('../../prompts/classificador-mods-ts4-prompt.md')
        ]
        
        for path in prompt_paths:
            if path.exists():
                with open(path, 'r', encoding='utf-8') as f:
                    return f.read()
        
        logger.warning("Arquivo de prompt não encontrado, usando prompt padrão")
        return self._get_default_prompt()
    
    def _get_default_prompt(self) -> str:
        """Retorna um prompt padrão simplificado."""
        return """
Você é um especialista em classificar mods de The Sims 4.

Classifique o mod em uma escala de 0-5:
- Priority 0 (Cinza): Sem interesse/incompatibilidade
- Priority 1 (Vermelho): Core/Framework/Dependência essencial
- Priority 2 (Amarelo): Gameplay importante
- Priority 3 (Verde): Gameplay relevante localizado  
- Priority 4 (Azul): Hobby/Storytelling
- Priority 5 (Roxo): Visual/Estético

Retorne APENAS um JSON válido com:
{
  "priority": <número 0-5>,
  "priority_label": "<Cinza|Vermelho|Amarelo|Verde|Azul|Roxo>",
  "sub_category": "<subcategoria se 3, 4 ou 5>",
  "sub_category_label": "<descrição da subcategoria>",
  "notes_reason": "<justificativa detalhada>"
}
"""
    
    def classify_mod(self, mod_content: Dict[str, str]) -> Dict:
        """
        Classifica um mod usando LLM.
        
        Args:
            mod_content: Dicionário com title, description, full_text
            
        Returns:
            Classificação estruturada
        """
        try:
            # Monta o prompt completo
            user_message = f"""
Título: {mod_content.get('title', 'N/A')}

Descrição: {mod_content.get('description', 'N/A')}

Conteúdo:
{mod_content.get('full_text', '')[:8000]}  # Limita tamanho

Classifique este mod seguindo as instruções.
"""
            
            logger.info(f"Classificando mod com {self.provider}: {self.model}")
            
            # Chama o provedor específico
            if self.provider == 'openai':
                response = self._call_openai(user_message)
            elif self.provider == 'anthropic':
                response = self._call_anthropic(user_message)
            elif self.provider == 'google':
                response = self._call_google(user_message)
            else:
                raise ValueError(f"Provedor {self.provider} não implementado")
            
            # Parse JSON response
            result = self._parse_response(response)
            logger.info(f"Classificação concluída: Priority {result['priority']}")
            return result
            
        except Exception as e:
            logger.error(f"Erro ao classificar mod: {str(e)}")
            raise
    
    def _call_openai(self, user_message: str) -> str:
        """Chama API da OpenAI."""
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.classifier_prompt},
                {"role": "user", "content": user_message}
            ],
            temperature=0.3,
            response_format={"type": "json_object"}
        )
        return response.choices[0].message.content
    
    def _call_anthropic(self, user_message: str) -> str:
        """Chama API da Anthropic."""
        response = self.client.messages.create(
            model=self.model,
            max_tokens=2048,
            system=self.classifier_prompt,
            messages=[
                {"role": "user", "content": user_message}
            ],
            temperature=0.3
        )
        return response.content[0].text
    
    def _call_google(self, user_message: str) -> str:
        """Chama API do Google Gemini."""
        model = self.client.GenerativeModel(self.model)
        full_prompt = f"{self.classifier_prompt}\n\n{user_message}"
        response = model.generate_content(
            full_prompt,
            generation_config={'temperature': 0.3}
        )
        return response.text
    
    def _parse_response(self, response: str) -> Dict:
        """Parse da resposta JSON do LLM."""
        try:
            # Remove markdown code blocks se presente
            if '```json' in response:
                response = response.split('```json')[1].split('```')[0]
            elif '```' in response:
                response = response.split('```')[1].split('```')[0]
            
            # Parse JSON
            result = json.loads(response.strip())
            
            # Valida campos obrigatórios
            required_fields = ['priority', 'priority_label', 'notes_reason']
            for field in required_fields:
                if field not in result:
                    raise ValueError(f"Campo obrigatório ausente: {field}")
            
            return result
            
        except json.JSONDecodeError as e:
            logger.error(f"Erro ao fazer parse do JSON: {e}")
            logger.error(f"Resposta recebida: {response}")
            raise ValueError(f"Resposta inválida do LLM: {response[:200]}")


def classify_with_llm(mod_content: Dict[str, str], 
                      api_key: Optional[str] = None,
                      model: Optional[str] = None) -> Dict:
    """
    Função de conveniência para classificar com LLM.
    
    Args:
        mod_content: Conteúdo do mod
        api_key: API key (opcional)
        model: Nome do modelo (opcional)
        
    Returns:
        Classificação estruturada
    """
    client = LLMClient(api_key=api_key, model=model)
    return client.classify_mod(mod_content)
