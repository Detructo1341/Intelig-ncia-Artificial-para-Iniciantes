# 🌡️ Temperatura e Parâmetros: Controlando o Comportamento da IA

## 🎯 O que você vai aprender

Temperatura não é apenas um número — é um **controle de personalidade** da IA. Neste guia, você descobrirá como temperatura, top-p, frequency penalty e outros parâmetros moldam respostas de LLMs, e como usá-los estrategicamente.

## 🧠 Por que isso importa?

Usar IA com parâmetros padrão é como dirigir um carro sem ajustar o banco: funciona, mas não é otimizado. Dominar parâmetros permite:

- **Respostas mais consistentes** para tarefas técnicas
- **Criatividade controlada** para brainstorming
- **Redução de repetições** em textos longos
- **Penalização de padrões indesejados**

**Analogia para psicólogos**: É como modular estados mentais — foco vs. divagação, convergência vs. divergência.

---

## 📖 Explicação

### Os 5 Parâmetros Principais

| Parâmetro | O que controla | Quando usar |
|-----------|----------------|-------------|
| **Temperature** | Aleatoriedade/criatividade | SEMPRE ajustar |
| **Top-p** | Diversidade de vocabulário | Tarefas criativas |
| **Max Tokens** | Comprimento da resposta | Limitar custos/tempo |
| **Frequency Penalty** | Repetição de palavras | Textos longos |
| **Presence Penalty** | Introdução de novos tópicos | Diversidade temática |

---

## 1️⃣ Temperature (0.0 - 2.0): O Dial Criativo

### Como Funciona

Temperature modifica a **distribuição de probabilidades** das próximas palavras.

**Exemplo**:
```
Prompt: "O céu está ___"

Probabilidades originais:
azul: 40%
nublado: 25%
claro: 20%
escuro: 10%
roxo: 3%
xadrez: 0.01%
```

**Com Temperature 0.0** (determinístico):
```
azul: 100%  ← Sempre escolhe a mais provável
nublado: 0%
claro: 0%
...
```

**Com Temperature 1.0** (balanceado):
```
azul: 40%
nublado: 25%
claro: 20%
escuro: 10%
roxo: 3%
xadrez: 0.01%
```

**Com Temperature 2.0** (criativo/caótico):
```
azul: 25%
nublado: 20%
claro: 18%
escuro: 15%
roxo: 10%  ← Opções improváveis ganham chance
xadrez: 5%
```

### Guia de Uso

| Temperature | Comportamento | Casos de Uso |
|-------------|---------------|--------------|
| **0.0 - 0.3** | Determinístico, previsível | Código, traduções, extrações de dados |
| **0.4 - 0.6** | Balanceado, leve variação | Respostas técnicas com alguma flexibilidade |
| **0.7 - 1.0** | Conversacional, natural | Chat, explicações, tutoriais |
| **1.1 - 1.5** | Criativo, surpreendente | Brainstorming, poesia, ficção |
| **1.6 - 2.0** | Experimental, imprevisível | Arte generativa, exploração conceitual |

### Exemplos Práticos

#### Tarefa: Gerar slogan para cafeteria

**Temperature 0.2**:
```
"Café de qualidade, todos os dias"
"O melhor café da cidade"
```
✅ Seguro, previsível  
❌ Genérico

**Temperature 1.0**:
```
"Onde cada xícara conta uma história"
"Seu refúgio aromático diário"
```
✅ Criativo, memorável  
✅ Ainda coerente

**Temperature 1.8**:
```
"Líquido solar em cerâmica sussurrante"
"Despertar em notas caramelizadas de sonho"
```
✅ Original, poético  
⚠️ Pode ser excessivo para alguns contextos

---

## 2️⃣ Top-p (Nucleus Sampling): Filtrando Opções

### Como Funciona

Top-p limita escolhas a **cumulativo de probabilidade**.

**Exemplo**:
```
Probabilidades originais:
azul: 40%
nublado: 25%
claro: 20%
escuro: 10%
roxo: 3%
xadrez: 2%
```

**Com top-p = 0.9** (90%):
```
Considera apenas:
azul: 40% }
nublado: 25% } = 95% cumulativo
claro: 20%   }

Ignora: escuro, roxo, xadrez
```

### Diferença: Temperature vs. Top-p

- **Temperature**: Repondera todas as opções
- **Top-p**: Descarta opções improváveis

**Melhor prática**: Usar **OU** temperature **OU** top-p, não ambos.

---

## 3️⃣ Max Tokens: Limite de Comprimento

### Como Funciona

Define **número máximo** de tokens (palavras + fragmentos) na resposta.

**Exemplos**:
```
max_tokens=50  → ~40 palavras (resposta curta)
max_tokens=500  → ~400 palavras (parágrafo longo)
max_tokens=2000  → ~1500 palavras (artigo curto)
```

### Quando Usar

- **Controle de custos**: Tokens custam dinheiro em APIs
- **Tempo de resposta**: Menos tokens = resposta mais rápida
- **Formato desejado**: "Responda em 1 parágrafo" (set max_tokens baixo)

⚠️ **Atenção**: Se o limite é atingido, resposta pode ser cortada no meio.

---

## 4️⃣ Frequency Penalty (-2.0 a 2.0): Evitando Repetição

### Como Funciona

**Penaliza palavras** proporcionalmente a quantas vezes já apareceram.

**Valor positivo** (ex: 0.5): Desencoraja repetição  
**Valor negativo** (ex: -0.5): Encoraja repetição

### Exemplo

**Sem penalty** (0.0):
```
"A inteligência artificial é fascinante. A IA está revolucionando tudo. 
A tecnologia de IA é impressionante. A IA mudará o futuro."
```
❌ "IA" repetido excessivamente

**Com frequency_penalty=0.8**:
```
"A inteligência artificial é fascinante. Essa tecnologia está revolucionando tudo. 
Machine learning impressiona pela capacidade adaptativa. 
Sistemas cognitivos moldarão nosso futuro."
```
✅ Vocabulário mais diverso

### Quando Usar

- **Textos longos**: Artigos, ensaios, relatórios
- **Criatividade**: Evitar clichês ("No fim das contas...", "É importante notar...")
- **Listas variadas**: Gerar 50 ideias sem repetição

---

## 5️⃣ Presence Penalty (-2.0 a 2.0): Explorando Novos Tópicos

### Como Funciona

**Frequency Penalty**: Penaliza por **quantas vezes** palavra apareceu  
**Presence Penalty**: Penaliza se palavra **já apareceu** (sim/não binário)

**Diferença sutil mas importante**:

```
Palavra "gato" apareceu 5 vezes

Frequency Penalty: Penalidade cresce (1x, 2x, 3x, 4x, 5x)
Presence Penalty: Penalidade fixa (apareceu? sim → penaliza)
```

### Quando Usar

- **Diversidade temática**: Brainstorming, exploração de ideias
- **Evitar fixação**: Quando modelo insiste em voltar ao mesmo ponto
- **Redações criativas**: Forçar introdução de novos conceitos

---

## 🔬 Combinações Estratégicas de Parâmetros

### Cenário 1: Código de Produção
```python
temperature=0.1
max_tokens=2000
frequency_penalty=0.0
```
**Por quê**: Código precisa ser determinístico e repetição é OK (loops, patterns).

---

### Cenário 2: Brainstorming Criativo
```python
temperature=1.2
top_p=0.95
frequency_penalty=0.8
presence_penalty=0.6
max_tokens=500
```
**Por quê**: Alta criatividade, vocabulário diverso, explora múltiplas direções.

---

### Cenário 3: Redação Acadêmica
```python
temperature=0.6
frequency_penalty=0.3
presence_penalty=0.2
max_tokens=3000
```
**Por quê**: Formal mas não robótico, evita repetições, comprimento adequado.

---

### Cenário 4: Chatbot de Suporte
```python
temperature=0.4
max_tokens=150
frequency_penalty=0.2
```
**Por quê**: Respostas consistentes, concisas, levemente variadas para naturalidade.

---

### Cenário 5: Poesia Experimental
```python
temperature=1.8
top_p=0.90
frequency_penalty=1.0
presence_penalty=0.8
```
**Por quê**: Máxima criatividade, vocabulário único, evita clichês.

---

## 🧪 Experimentos para Testar Parâmetros

### Experimento 1: Teste de Temperature
Gere a mesma história 5 vezes com temperatures diferentes:
```
0.0, 0.5, 1.0, 1.5, 2.0
```
Compare coerência vs. originalidade.

---

### Experimento 2: Teste de Frequency Penalty
Gere uma lista de 50 ideias com:
```
A) frequency_penalty=0.0
B) frequency_penalty=1.0
```
Conte repetições.

---

### Experimento 3: Top-p vs. Temperature
Gere texto criativo com:
```
A) temperature=1.5, top_p=1.0
B) temperature=0.7, top_p=0.85
```
Qual é mais coerente? Qual é mais surpreendente?

---

## 🤔 Questões para Reflexão

1. **Temperature alta simula "pensamento divergente" ou apenas aleatoriedade?** Há diferença?

2. **Se você sempre usa temperature=1.0, está perdendo oportunidades de controle?**

3. **Para psicólogos**: Penalties são como **inibição cognitiva** (suprimir padrões habituais)?

4. **Existe um "parâmetro perfeito" ou cada tarefa exige calibração?**

5. **Se você descobrir parâmetros que geram "superinteligência aparente", você compartilharia publicamente?**

---

## 🛠️ Cheat Sheet de Parâmetros

```python
# FORMATO TÉCNICO
{
  "temperature": 0.7,        # 0.0-2.0
  "top_p": 1.0,              # 0.0-1.0
  "max_tokens": 1000,        # 1-∞
  "frequency_penalty": 0.0,  # -2.0 a 2.0
  "presence_penalty": 0.0    # -2.0 a 2.0
}

# PRESETS RECOMENDADOS
PRESETS = {
    "codigo": {"temperature": 0.1, "max_tokens": 2000},
    "chat": {"temperature": 0.7, "max_tokens": 500},
    "criativo": {"temperature": 1.2, "frequency_penalty": 0.8},
    "academico": {"temperature": 0.6, "frequency_penalty": 0.3},
    "poetico": {"temperature": 1.5, "presence_penalty": 0.8}
}
```

---

## 📚 Referências

### Documentação Oficial
- **OpenAI API Params**: [platform.openai.com/docs/api-reference/completions](https://platform.openai.com/docs/api-reference/completions)
- **Anthropic Claude Params**: [docs.anthropic.com/en/api](https://docs.anthropic.com/en/api)

### Papers
- **"The Curious Case of Neural Text Degeneration"** – Holtzman et al. (2019) [Top-p]
- **"Nucleus Sampling"** – Fan et al. (2018)

### Recursos Práticos
- **OpenAI Playground**: Teste parâmetros visualmente
- **LangChain Docs**: Integração de parâmetros em pipelines

---

## ➡️ Próximos Passos

1. **[Como Funcionam os LLMs](como-funcionam-os-llms.md)** → Entenda por que parâmetros funcionam
2. **[Psicologia do Prompt Eficaz](psicologia-do-prompt-eficaz.md)** → Combine com prompts otimizados
3. **[Tipos de Prompting](tipos-de-prompting.md)** → Técnicas avançadas de interação

---

## 🎓 Nota do Autor

Parâmetros são o "painel de controle" da IA. Ignorá-los é como dirigir sempre na mesma velocidade — funciona, mas você não está no controle total.

Experimente. Documente. Descubra suas configurações ideais. Não há "certo" ou "errado" — há **adequado ao propósito**.

Como psicólogo, você reconhece que estados mentais humanos também são moduláveis (atenção, humor, energia). Parâmetros de IA são a versão computacional disso.

---

**Escrito por Gabriel, Arquiteto Cognitivo**  
*Última atualização: Dezembro 2024*
