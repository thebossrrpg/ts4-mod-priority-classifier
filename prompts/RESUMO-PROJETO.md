# Resumo do Projeto: Classificador Automático de Prioridade de Mods TS4

## Objetivo
Automatizar a classificação de mods de The Sims 4 por prioridade (0-5) com sub-categorias, integrando com o Notion.

## Fluxo do Pipeline

1. **Input**: URL da página do mod
2. **Extração**: Texto da página (nome, descrição, requisitos, changelog)
3. **Classificação**: LLM analisa seguindo roteiro estruturado → JSON
4. **Notion**: Atualiza/cria página na database

## Estrutura do Projeto

- `docs/` - Manuais de classificação e sub-classificação
- `prompts/` - Prompt completo do classificador
- `src/` - Código Python do pipeline
- `config/` - Configurações (API keys)

## JSON de Saída do Classificador

```json
{
  "priority": 3,
  "priority_label": "Verde",
  "score": 4,
  "remocao": 2,
  "framework": 0,
  "essencial": 2,
  "sub_category": "3C",
  "sub_category_label": "Família & Relações Pontuais",
  "mod_name": "Nome do mod",
  "creator": "Criador",
  "notes_reason": "Justificativa"
}
```

## Integração Notion

### Campos da Database
- **Priority** (Number): 0-5
- **Notes** (Text): Sub-categoria + justificativa

### Regra de Notes
- Priority 0, 1, 2: Notes opcional ou vazio
- Priority 3, 4, 5: Notes =  `"{sub_category} — {sub_category_label}. {notes_reason}"`

### Comportamento de Atualização
- Se Notes já tem conteúdo: **ACRESCENTAR** em nova linha (não sobrescrever)
- Se mod não existe na DB: criar nova página

## Próximos Passos

1. Criar arquivo de prompt completo (classificador-mods-ts4.md)
2. Adicionar manuais em docs/
3. Criar README.md principal
4. Desenvolver código Python em src/
