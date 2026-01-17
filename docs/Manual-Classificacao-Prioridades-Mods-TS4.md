# Manual de Classificação de Prioridades de Mods — The Sims 4

**Versão:** 1.0  
**Data:** Janeiro de 2026  
**Criado por:** Simone, Assistente de Organização de Mods & CC  

---

## Introdução

Este manual descreve o sistema de classificação de prioridades (0–5) para mods de The Sims 4, desenvolvido para organizar, manter e atualizar sua coleção de forma eficiente e estruturada.

A lógica da régua considera:
1. **Remoção**: Impacto se o mod for removido por causa de patch ou conflito.
2. **Framework**: Se o mod é core/library/dependência obrigatória para outros mods.
3. **Essencial**: Essencialidade genérica do tipo de mod (não gosto pessoal).

**Score = Remoção + Framework + Essencial**

Essa pontuação é então convertida em uma **Prioridade numérica (0–5)** que reflete a urgência de atualização/checagem em patches.

---

## Escala de Prioridades (0–5)

### 0 — CINZA: Cosmético & Visual Global Puro

**Impacto de remoção:** Zero. O jogo roda normalmente; você perde apenas elemento visual/estético.

**O que entra:**
- Map overrides e decorações de mundos.
- Loading screens temáticas.
- Main menu overrides.
- Fontes e ícones de UI.
- Telas de mundos customizadas.
- Overrides visuais sem função mecânica.

**Exemplo:** Map override do FilipeSims, fontes customizadas, loading screen estilizada.

**Frequência de checagem:** Raramente. Só em patches visuais muito radicais.

---

### 1 — VERMELHO: Core/Framework/Dependência Essencial

**Impacto de remoção:** Pode quebrar saves e/ou vários outros mods que dependem dele; sistema inteiro desaba.

**O que entra:**
- XML Injector (Scumbumbo).
- Lot51 Core.
- ModGuard.
- Better Exceptions.
- Qualquer mod explicitamente descrito como "core", "framework", "library" ou "required for other mods".

**Exemplo:** XML Injector é dependência de muitos mods de Ilkavelle, Kuttoe, etc. Remover = quebra tudo.

**Frequência de checagem:** Em CADA patch. Se quebrar, tudo quebra.

**Ação essencial:** Manter SEMPRE atualizado. Este é o primeiro mod a verificar.

---

### 2 — AMARELO: Importante (Afeta Sistemas Grandes)

**Impacto de remoção:** Desconfigura um sistema importante, mas o jogo ainda roda. Sims perdem funcionalidade core; pode haver erros de transição.

**O que entra:**
- Mods que mexem em **morte, temperatura, necessidades, finanças, gravidez, relacionamentos genéricos, emoções/sentimentos, clubes, calendário, comida como sistema, polícia/lei, carreiras grandes, educação**.
- Overhauls de carreiras completas (ex.: Archaeologist/Palaeontologist Freelancer Career).
- Overhauls de eventos escolares (ex.: Career Day Overhaul).
- Overhauls de sistema de natação/afogamento (ex.: Realistic Swimming v2.0).
- Grandes modificações de UI funcional que mexem em menus/catálogos estruturais.

**Exemplo:**
- Archaeologist/Palaeontologist Freelancer Career (carreira freelancer com drama_scheduler).
- Career Day Overhaul (evento + carreiras teens).
- Realistic Swimming v2.0 (sistema de natação + afogamento + carreira).
- Vacuum Overhaul (sistema de limpeza).
- More Traits in CAS (sistema de traits).

**Frequência de checagem:** Em CADA patch grande (patch.X.0 ou patch quando há mudança em sistema afetado).

**Ação essencial:** Verificar changelog; atualizar ASSIM que houver versão nova do mod.

---

### 3 — VERDE: Gameplay/QoL Relevante Localizado

**Impacto de remoção:** Só muda comportamentos/eventos pontuais; o jogo roda normalmente, mas você perde conteúdo/qualidade de vida específica.

**O que entra:** Jogos que adicionam/ajustam gameplay em escopo localizado:
- Novas interações sociais, eventos temáticos, tradições de feriado.
- Ajustes de buffs/sentimentos específicos (não overhaul de sentimentos inteiro).
- Carreiras simples ou hobbies novos.
- Skills & atividades localizadas.
- Objetos funcionais específicos (um tipo novo com interação).
- QoL de menus/CAS sem reescrever estrutura.

**Subcategorias (3A–3F):**

#### 3A — Eventos & Festas
Tudo que mexe em **eventos sociais, convidados, objetivos de evento, tipos de festa**.

**Exemplos:**
- Events Overhaul – Invite Anyone (convida qualquer Sim para quase todos eventos).
- NPC Weddings and Invites.
- Better and Longer Prom [Plus Event Goals Bug Fix].

#### 3B — Feriados & Calendário Leve
**Tradições de feriado novas e mecânicas ligadas a feriados específicos, sem reescrever o sistema inteiro de calendário.**

**Exemplos:**
- Letter to Father Winter (tradição de Papai Inverno + carta + 25 presentes).
- All In-Game Traditions are Updated by Preferences and Traits + New Pets and Farm Traditions.

#### 3C — Família & Relações Pontuais
**Interações extras entre familiares, pequenos ajustes de sentimentos, buffs de luto, ciúmes, traição, romance — sem ser overhaul completo de relacionamentos.**

**Exemplos:**
- Break Up, Divorce, Discuss Having Baby Options.
- Longer and Stronger Mourning Buffs by Relationship.
- Ask About Romantic and WooHoo Orientation Friendly and Successful.
- Longer and Stronger Being Cheated Sentiments by Mood and Effect.
- Better Introductions by Traits and Preferences.
- Assertive & Passive Romance Styles.

#### 3D — Skills, Hobbies & Carreiras Leves
**Escrever livros para toddlers, carreiras simples, hobbies novos ou expansões pequenas de atividades específicas.**

**Exemplos:**
- Write Books for Toddlers.
- Best Mentoring.
- Random Crafting.
- Career Aptitude Test (teste de carreira com 35 resultados).

#### 3E — Objetos Funcionais Específicos
**Um ou poucos objetos com interações extras, sem criar um sistema grande por trás.**

(Nenhum exemplo catalogado até agora na sua coleção.)

#### 3F — Outros 3 Verde
**Qualquer mod claramente "gameplay/QoL localizado relevante" que não encaixe bem nas categorias acima.**

**Exemplos:**
- Better Hygiene Reactions and Buffs by Traits (Traits & Ambiente/Higiene).
- Reapply for Scholarship (mecânica de universidade/bolsa).

**Frequência de checagem:** A cada patch grande (patch.X.0) ou conforme criador avisa atualização.

**Ação recomendada:** Atualizar quando houver patch para versão do mod, mas não é urgência como Amarelo.

---

### 4 — AZUL: Hobby/Storytelling

**Impacto de remoção:** Zero impacto mecânico. Você perde apenas conteúdo narrativo/hobby pessoal.

**O que entra:**
- Aspirações temáticas e traços de flavor.
- Marcos narrativos (milestones) puramente de enredo.
- Interações cenográficas (poses, anims, clutter narrativo) para storytelling.

**Subcategorias (4A–4D):**

#### 4A — Aspirações
**Qualquer mod que adicione ou ajuste aspirações (infantis, teens, adultos, de hobby, de carreira, de storytelling).**

**Exemplos:**
- Proud Geek Aspiration.
- Teen Aspirations customizadas.

#### 4B — Traits, Estilos & Flavor de Personalidade
**Traços extras e pequenos sistemas de "estilo de vida" que são narrativos, mexendo em quem o Sim é.**

(Subcategoria reconhecida mas sem exemplo específico catalogado.)

#### 4C — Storytelling de Cena
**Poses, animações para screenshots, interações quase sem consequência mecânica, objetos de cena usados só para contar história.**

(Subcategoria reconhecida mas sem exemplo específico catalogado.)

#### 4D — Marcos Narrativos (Milestones)
**Novos milestones que registram "acontecimentos" (prom, ser pego pela escola, primeira viagem, affair de teen, etc.), mas não alteram sistemas grandes.**

**Exemplos:**
- Attended Prom New Milestone.
- First Visitor, Slept Through Night (toddlers), First Vacation.
- Caught Sneaking Out New Milestone.
- Caught By School Staff New Milestone.
- Rejected as WooHoo Partner New Milestone.
- Caught Trashing Rival Photo Op Stand Milestone.
- Affair, Woohoo, Give Birth Milestones For Teens.

**Frequência de checagem:** Raramente. Só se houver patch que quebre aspiration/milestone system.

**Ação:** Manter instalado; atualizar conforme necessário.

---

### 5 — ROXO: Experimentais/Nicho/Teste

**Impacto de remoção:** Zero. Você remove e o jogo roda normalmente, sem impacto em saves ou outros mods.

**O que entra:**
- Mods muito específicos/nichados.
- Conteúdo NSFW (se houver na sua coleção).
- Mods que você está ainda testando/avaliando.
- Mods que talvez nem entrem na coleção principal.
- Temas, estética & imersão leve (mini buffs temáticos, rotinas imersivas fofinhas).

**Subcategorias (5A–5E, conforme necessário):**

#### 5A — Temas, Estética & Imersão Leve
**Pequenos mods que mudam ambiente/tema de forma imersiva, mas não são só override global. Mini-eventos decorativos, detalhes de clima emocional, micro buffs temáticos que deixam a narrativa mais gostosa.**

**Exemplos:**
- Mod de "buffzinho de café na manhã".
- Mini-mood de "ama chuva".
- Rotina decorativa matinal.

**Frequência de checagem:** Nenhuma. Siga atualizações do criador, mas não é prioridade.

---

## Fórmula de Cálculo

### Passo 1: Determinar Remoção

Responda internamente: **"Se eu tiver que remover este mod por causa de um patch, o que provavelmente acontece com o resto do jogo e com outros mods?"**

| Categoria | Descrição | Valor |
|-----------|-----------|-------|
| **A** | Pode quebrar ou buggar saves e/ou vários outros mods que dependem dele | 4 |
| **B** | Desconfigura um sistema importante, mas o jogo ainda roda (relacionamentos, gravidez, finanças, clubes, medos, calendário, comida como sistema) | 3 |
| **C** | Só muda comportamentos pontuais (prom, presentes, beijos extras, autonomia específica, menos cadeiras, menos festivais, usabilidade de menus/CAS) | 2 |
| **D** | Só visual/estético (UI temática, cores, mapas desenhados, fontes, loading screen, ícones, tela de mundos, main menu decorativo) | 1 |

**Resultado:** remoção = [1, 2, 3 ou 4]

---

### Passo 2: Detectar Framework

**Pergunta:** "Este mod é core/framework/library/dependência obrigatória para outros mods?"

- SIM → framework = 1
- NÃO → framework = 0

**Resultado:** framework = [0 ou 1]

---

### Passo 3: Estimar Essencialidade Genérica

Olhe **apenas para o tipo de mod** (não para seu gosto pessoal).

| Nível | Critério | Valor |
|-------|----------|-------|
| Muito Alta | Correção de bugs graves OU melhora forte de sistemas centrais do jogo base/expansões OU "must-have" de estabilidade/realismo básico | 3 |
| Alta | Expande bastante o gameplay de tema importante (família, carreira, escola, finanças, emoções, hobbies grandes) OU QoL muito forte (facilita muito tarefas comuns) | 2 |
| Média | Adiciona coisas legais mas específicas (conteúdo de hobby, evento, receitas, interações sociais extras, ajustes de autonomia pontuais, QoL localizado) | 1 |
| Baixa | Altamente nichado OU puramente cosmético (visual, UI temática, loading screen, mapas estilizados, fontes, detalhes de interface) | 0 |

**Resultado:** essencial = [0, 1, 2 ou 3]

---

### Passo 4: Calcular Score

```
score = remoção + framework + essencial
```

**Resultado:** score = [0 até 8]

---

### Passo 5: Converter para Prioridade

| Score | Priority | Cor |
|-------|----------|-----|
| ≥ 7 | 1 | Vermelho |
| 5–6 | 2 | Amarelo |
| 3–4 | 3 | Verde |
| 2 | 4 | Azul |
| ≤ 1 | 0 | Cinza |

**Resultado final:** Priority = [0, 1, 2, 3 ou 4]

---

## Exemplos de Classificação

### Exemplo 1: Letter to Father Winter (Ilkavelle)

**Análise:**
- Tipo: Tradição de feriado nova + interação de carta + 25 presentes.
- Requer: Seasons EP, XML Injector.

**Cálculo:**
1. **Remoção:** Se remover, o feriado vanilla volta; nada quebra. → **remoção = 2 (C)**
2. **Framework:** Não é core; é consumidor de XML Injector. → **framework = 0**
3. **Essencial:** Adiciona tradição temática legal, mas localizada. → **essencial = 1**

**Score = 2 + 0 + 1 = 3**

**Priority = 3 Verde – 3B (Feriados & Calendário Leve)**

---

### Example 2: Events Overhaul – Invite Anyone (Ilkavelle)

**Análise:**
- Tipo: Altera filtros de convidados em quase todos os eventos; permite convidar qualquer Sim.
- Requer: Vários arquivos de filter_ e situations.

**Cálculo:**
1. **Remoção:** Comportamento pontual de convidados; jogo roda com sistema vanilla. → **remoção = 2 (C)**
2. **Framework:** Não é framework. → **framework = 0**
3. **Essencial:** Expande bem gameplay de eventos sociais, mas localizado. → **essencial = 1**

**Score = 2 + 0 + 1 = 3**

**Priority = 3 Verde – 3A (Eventos & Festas)**

---

### Exemplo 3: Archaeologist/Palaeontologist Freelancer Career (Ilkavelle)

**Análise:**
- Tipo: Carreira freelancer completa com sistema de gigs, drama_scheduler.
- Mexe em: drama_scheduler (arquivo core), sistema de carreiras, objetivos, viagens.
- Requer: XML Injector; versões especiais para compatibilidade.
- Histórico: Atualizado em praticamente todos os patches.

**Cálculo:**
1. **Remoção:** Sims nessa carreira podem perder emprego, LE possível; carreira é estruturada. → **remoção = 3 (B)**
2. **Framework:** Não é framework para outros, mas usa core de drama_scheduler. → **framework = 0**
3. **Essencial:** Grande carreira de tema importante (exploração, arqueologia, hobbies). → **essencial = 2**

**Score = 3 + 0 + 2 = 5**

**Priority = 2 Amarelo**

---

### Exemplo 4: Better Hygiene Reactions and Buffs by Traits

**Análise:**
- Tipo: Ajusta reações de Sims a sujeira/cheiro/higiene, ligado a traits (slob, neat, snob, etc.).
- Afeta: Reações de Sims e distribuição de buffs, sem overhaul total.

**Cálculo:**
1. **Remoção:** Comportamento pontual; sistema vanilla retorna sem dano. → **remoção = 2 (C)**
2. **Framework:** Não é framework. → **framework = 0**
3. **Essencial:** Melhora coerência entre traits e reações, é flavor/gameplay localizado. → **essencial = 1**

**Score = 2 + 0 + 1 = 3**

**Priority = 3 Verde – 3F (Outros 3 Verde)**

---

### Exemplo 5: Proud Geek Aspiration (Ilkavelle)

**Análise:**
- Tipo: Aspiração temática com trait de recompensa.
- Mexe em: Apenas aspiração e trait novo; sem sistema.

**Cálculo:**
1. **Remoção:** Perde-se aspiração/trait; nada quebra. → **remoção = 1 (D)**
2. **Framework:** Não é framework. → **framework = 0**
3. **Essencial:** Hobby/storytelling; nichado de gosto pessoal. → **essencial = 0**

**Score = 1 + 0 + 0 = 1**

**Priority = 4 Azul – 4A (Aspirações)**

---

### Exemplo 6: Map Override (FilipeSims)

**Análise:**
- Tipo: Decoração visual de mapa; sem função.

**Cálculo:**
1. **Remoção:** Perde visual; nada mecânico. → **remoção = 1 (D)**
2. **Framework:** Não é framework. → **framework = 0**
3. **Essencial:** Puramente cosmético. → **essencial = 0**

**Score = 1 + 0 + 0 = 1**

**Priority = 0 Cinza**

---

### Exemplo 7: XML Injector (Scumbumbo)

**Análise:**
- Tipo: Framework/library.
- Função: Dependência obrigatória de centenas de mods.

**Cálculo:**
1. **Remoção:** Quebra muitos mods. → **remoção = 4 (A)**
2. **Framework:** É core/library. → **framework = 1**
3. **Essencial:** Must-have de estabilidade. → **essencial = 3**

**Score = 4 + 1 + 3 = 8**

**Priority = 1 Vermelho**

---

## Frequência de Checagem por Prioridade

| Priority | Cor | Quando Verificar | Urgência |
|----------|-----|------------------|----------|
| 0 | Cinza | Raramente; conforme gosto | Baixíssima |
| 1 | Vermelho | **EM CADA PATCH** | Crítica |
| 2 | Amarelo | Cada patch grande (patch.X.0) | Muito alta |
| 3 | Verde | Cada patch ou conforme aviso | Alta |
| 4 | Azul | Conforme disponível | Média |
| 5 | Roxo | Conforme disponível | Baixa |

---

## Notas sobre Subcategorias (3A–3F, 4A–4D, 5A–5E)

As subcategorias **refinem a organização dentro da mesma prioridade**, sem alterar o número base.

### Usar quando:
- Você tem muitos mods na mesma prioridade e quer organizá-los melhor.
- Precisa de contexto visual rápido sobre "tipo" do mod dentro da cor.
- Quer filtragens mais granulares no Notion/banco de dados.

### Exemplo de uso no Notion:
- Propriedade **Priority**: 3 (número/cor).
- Propriedade **Priority Sub** (select): 3A, 3B, 3C, 3D, 3E, 3F.

---

## Dicas de Manutenção

### Checklist de Patch

Quando EA lança um novo patch:

1. **Verificar Priority 1 Vermelho imediatamente:**
   - XML Injector atualizado?
   - Outros cores/libraries funcionam?

2. **Verificar Priority 2 Amarelo em seguida:**
   - Carreiras grandes quebradas?
   - Sistemas de eventos/calendário/morte afetados?
   - Criadores já liberaram updates?

3. **Verificar Priority 3 Verde conforme informações surgem:**
   - Milestones quebrados?
   - Eventos/feriados afetados?

4. **Priority 4 Azul & 5 Roxo:**
   - Atualizar conforme criadores liberem; não urgência.

### Manutenção Trimestral

- Limpar mods com status **Outdated** há mais de 3 meses.
- Revisar mods com **Installation = Downloaded** há muito tempo (não ativados).
- Atualizar notes sobre conflitos conhecidos.

### Atualização do Manual

Este manual deve ser **revisado e atualizado:**
- A cada grande mudança no sistema de prioridades.
- Quando novos padrões de mods surgirem.
- Conforme patches e novas expansões do jogo alterem dinâmica de compatibilidade.

---

## Contato & Feedback

Se tiver dúvidas sobre a classificação de um mod específico ou quiser sugerir mudanças no manual:

**Sempre lembre-se:**
- A régua é **ferramenta de organização**, não lei absoluta.
- Adapte conforme sua necessidade pessoal e coleção.
- O mais importante é **consistência** dentro do seu próprio sistema.

---

**Fim do Manual**

*Desenvolvido para a organização de The Sims 4 mods com Notion e Simone.*