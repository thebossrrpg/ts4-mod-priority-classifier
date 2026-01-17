# Manual de Classificação de Mods: The Sims 4

**Versão:** 3.0 (Edição Definitiva de Integridade de Dados)**Data:** Fevereiro de 2026**Criado por:** Simone, Assistente de Organização de Mods & CC

### 1\. Mudança Fundamental na v3.0

A distinção entre **Prioridade 4 (Azul)** e **Prioridade 5 (Roxo)** não é mais sobre "Storytelling vs. Tuning", mas sobre **Dados Persistentes vs. Regras Voláteis**.

* **Prioridade 4 (Azul):** Mods que **anexam dados** ao seu Sim ou Save (Traits, Aspirações, Milestones). Se remover incorretamente, o Sim pode bugar ou perder progresso.  
* **Prioridade 5 (Roxo):** Mods que **alteram regras globais** de funcionamento (Tweaks, Menus, Tempos). Se remover, a regra apenas reverte para a original da EA. Não deixa "lixo" no Sim.

### 2\. Escala de Prioridades (0–5)

#### 🔴 1 — VERMELHO: Core & Estrutura

**Definição:** A base que sustenta outros mods.**Risco:** Quebra o jogo (Crash/Infinite Load).**O que entra:** XML Injector, Lot51 Core, Dependências de Biblioteca.**Monitoramento:** **Obrigatório a cada patch.**

#### 🟡 2 — AMARELO: Sistemas Grandes

**Definição:** Mods que reescrevem mecânicas nativas complexas.**Risco:** O sistema para de funcionar ou trava a simulação (Simulation Lag/Errors).**O que entra:** RPO (Lumpinou), Homebody (SimsRealist), Carreiras Ativas Complexas.**Monitoramento:** A cada patch grande (x.0).

#### 🟢 3 — VERDE: Gameplay Ativo (Conteúdo & IA)

**Definição:** Mods que adicionam ações que o jogador *escolhe* fazer ou melhoram a inteligência de NPCs.**Risco:** A interação específica desaparece ou o NPC quebra.**O que entra:**

* Eventos e Festas Novos.  
* Melhoria de IA (Better Butler/Nanny).  
* Objetos Funcionais (Pílulas, Palcos).  
* Skills Novas.**Monitoramento:** Se a funcionalidade específica falhar.

#### 🔵 4 — AZUL: Dados de Save (Personalidade & Narrativa)

*(Revisado na v3.0)***Definição:** Mods que **gravam informações no arquivo do Sim**. Eles definem "quem o Sim é".**Risco de Remoção:** Médio/Chato. Remover um Trait ou Aspiração pode deixar o Sim com slots vazios, UI bugada no CAS ou erros ao tentar carregar o Sim na galeria.**O que entra:**

* **Custom Traits (Traços):** Personalidade.  
* **Custom Aspirations:** Objetivos de vida.  
* **Milestones:** Memórias do Sim (RPO/Milestones mods).**Monitoramento:** Baixo, mas exige cuidado ao **remover** (limpar o Sim antes de desinstalar).

#### 🟣 5 — ROXO: Micro-Tuning & Regras Voláteis

*(Revisado na v3.0)***Definição:** Mods que alteram a **lógica global** de processamento (tempos, filtros, filas de interação). Não salvam dados no Sim.**Risco de Remoção:** Quase Nulo. O jogo apenas volta a usar a regra padrão da EA imediatamente.**O que entra:**

* **5A — Filtros de Menu:** (Ex: *Choose Who You Call to Meal*).  
* **5B — Utilitários de Gestão:** (Ex: *Transfer Inventory*).  
* **5C — Math Tuning:** Mudanças de velocidade/dinheiro (Ex: *Higher Payments*, *Faster Homework*).  
* **5D — Fixes & Tweaks:** Pequenos ajustes de lógica (Ex: *Tea for Children*).**Monitoramento:** Nenhum. Se quebrar, o mod apenas para de fazer efeito.

#### ⚫ 0 — CINZA: Cosmético Global

**Definição:** Substituições de arquivos de textura/arte da interface.**O que entra:** Mapas, Loading Screens, Fontes.

### 3\. Nova Fórmula de Score (v3.0)

Para corrigir a incoerência matemática, ajustamos os valores de **Remoção**:  
**Score \= Impacto de Remoção \+ Dependência \+ Necessidade**  
**1\. Impacto de Remoção (Peso ajustado):**

* **4 (Crítico):** Crash/Quebra Save (Core).  
* **3 (Sistêmico):** Desconfigura Mecânica (Overhaul).  
* **2 (Dados Persistentes):** Deixa "lixo" ou dados órfãos no Sim (Traits/Aspirações/Milestones). **\-\> Define o AZUL.**  
* **1 (Volátil/Regra):** Reverte para regra EA sem danos (Tuning/Tweaks). **\-\> Define o ROXO.**  
* **0 (Estético):** Apenas visual.

**2\. Dependência (Framework):**

* **1:** Sim.  
* **0:** Não.

**3\. Necessidade Mecânica (Rigor):**

* **2 (Alta):** O jogo é injogável sem isso para mim.  
* **1 (Ativa):** Adiciona ação nova (Gameplay Verde).  
* **0 (Passiva/Flavor):** Apenas ajusta ou decora.

### 4\. Tabela de Conversão Definitiva (v3.0)

Score,Prioridade,Categoria,Perfil do Mod  
≥ 6,1 — Vermelho,Core,Frameworks essenciais.  
5,2 — Amarelo,Sistemas,Overhauls pesados.  
3 – 4,3 — Verde,Gameplay,Ações novas e melhorias de IA.  
2,4 — Azul,Persistente,"Traits, Aspirações (Remoção 2 \+ Nec 0)."  
1,5 — Roxo,Volátil,"Tweaks, QoL, Tuning (Remoção 1 \+ Nec 0)."  
0,0 — Cinza,Cosmético,"Mapas, Telas."

### 5\. Resumo da Auditoria para sua Coleção

Com a v3.0, a incoerência foi resolvida:

* **Por que 4 (Azul) \> 5 (Roxo)?**  
* Porque **Azul** envolve dados do Sim. Se a EA mudar a estrutura de Traits, você precisa atualizar ou seu Sim quebra no CAS.  
* O **Roxo** é apenas uma regra "por cima". Se a EA mudar o código, o mod Roxo geralmente é ignorado silenciosamente e o jogo segue.  
* **Exemplos Reais Corrigidos:**  
* **Proud Geek Aspiration (Azul):** Score antigo 1 \-\> **Novo Score 2** (Remoção 2 Dado Persistente \+ Nec 0). **Fica no Azul.**  
* **Choose Who You Call to Meal (Roxo):** Score antigo 2 \-\> **Novo Score 1** (Remoção 1 Regra Volátil \+ Nec 0). **Fica no Roxo.**

Agora o sistema é logicamente consistente: **quanto menor o número da prioridade, maior o risco técnico ou de dados.**  
