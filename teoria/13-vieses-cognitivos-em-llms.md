# Vieses Cognitivos em LLMs

## 🎯 O que você vai aprender
Como vieses humanos presentes nos dados de treinamento são replicados e amplificados por modelos de IA, e por que entender isso é crucial para uso responsável.

## 🧠 Por que isso importa?
LLMs são espelhos da sociedade que os treinou. Eles herdam nossos vieses, preconceitos e limitações cognitivas. Reconhecer isso é essencial para evitar perpetuar injustiças e tomar decisões mal informadas.

## 📖 Explicação

### A Origem dos Vieses

LLMs aprendem com texto humano da internet — bilhões de páginas escritas por pessoas com seus próprios vieses. O modelo não "inventa" preconceitos; ele **absorve e replica padrões** do mundo real.

**Analogia Psicológica**: É como uma criança que aprende linguagem ouvindo adultos. Se os adultos têm vieses, a criança aprenderá esses vieses como "normal".

### Principais Categorias de Vieses

#### 1. Viés de Confirmação

**Definição**: Tendência de favorecer informações que confirmam crenças pré-existentes.

**Como aparece em LLMs**:
- Se o prompt sugere uma posição, o modelo tende a reforçá-la
- Respostas podem ignorar evidências contraditórias
- Argumentos são construídos para "vencer", não para explorar verdade

**Exemplo**:
```
Prompt: "Explique por que café faz mal à saúde"
Resposta: [Lista apenas efeitos negativos, ignora benefícios]

Vs.

Prompt: "Explique os efeitos do café na saúde"
Resposta: [Apresenta visão balanceada]
```

**Mitigação**: Use prompts neutros e peça explicitamente perspectivas múltiplas.

#### 2. Viés de Disponibilidade

**Definição**: Superestimar probabilidades de eventos que vêm facilmente à mente.

**Como aparece em LLMs**:
- Eventos mais discutidos online parecem mais comuns
- Casos extremos são over-representados
- Riscos raros parecem mais prováveis

**Exemplo**:
```
Pergunta: "Qual é mais perigoso: andar de avião ou dirigir?"
Resposta tendenciosa: Pode enfatizar acidentes aéreos dramáticos
Resposta correta: Dirigir é estatisticamente muito mais perigoso
```

**Mitigação**: Sempre peça dados estatísticos, não apenas narrativas.

#### 3. Vieses de Gênero

**Como aparecem**:
- Profissões associadas a gêneros específicos
- Características emocionais estereotipadas
- Papéis sociais tradicionais assumidos

**Exemplos reais documentados**:
```
"O médico entrou no consultório. Ele..."
(Assumiu masculino)

"A enfermeira cuidou do paciente. Ela..."
(Assumiu feminino)

"O CEO anunciou... Ele..."
(Assumiu masculino para posição de liderança)
```

**Experimento famoso (Word2Vec)**:
```
Homem : Programador :: Mulher : ?
Resultado: Dona de casa

(Embedding matemático refletindo viés social)
```

#### 4. Vieses Raciais e Culturais

**Como aparecem**:
- Associações negativas com certos nomes ou etnias
- Preferência por narrativas ocidentais
- Sub-representação de culturas minoritárias

**Exemplo documentado**:
```
Prompt: "Complete: O homem negro estava..."
Respostas tendenciosas frequentes: "...fugindo", "...armado"

Prompt: "Complete: O homem branco estava..."
Respostas tendenciosas frequentes: "...trabalhando", "...ajudando"
```

**Causa**: Vieses na cobertura midiática são aprendidos pelo modelo.

#### 5. Viés de Ancoragem

**Definição**: Depender excessivamente da primeira informação recebida.

**Como aparece em LLMs**:
- Primeiras frases do prompt têm influência desproporcional
- Modelos "ancoram" em exemplos iniciais
- Difícil corrigir impressões iniciais na mesma conversa

**Exemplo**:
```
Prompt 1: "João é preguiçoso. Ele..."
Resposta: [Continua tema negativo]

Vs.

Prompt 2: "João é dedicado. Ele..."
Resposta: [Continua tema positivo]

(Mesma pessoa, ancoragens opostas)
```

#### 6. Efeito Halo

**Definição**: Impressão geral afeta julgamento de características específicas.

**Como aparece em LLMs**:
```
"A empresa XYZ é bem-sucedida. Portanto, seus produtos..."
[Modelo assume que produtos também são excelentes]

Lógica falha: Sucesso financeiro ≠ qualidade de produto
```

#### 7. Viés de Otimismo/Pessimismo

**Como aparece**:
- Previsões sobre tecnologia tendem ao otimismo (especialmente IA!)
- Eventos políticos podem ter viés pessimista
- Depende da "temperatura emocional" dos dados de treino

**Exemplo**:
```
"Qual o futuro da IA?"
Resposta comum: [Cenários predominantemente positivos]

Razão: Textos sobre IA na internet tendem ao entusiasmo
```

### Vieses Estruturais dos Próprios Dados

#### Sub-representação
- Conteúdo em inglês domina treinamento
- Perspectivas do Sul Global são minoritárias
- Vozes marginalizadas aparecem menos

#### Viés Temporal
- Modelos "congelam" vieses da época de treinamento
- Não acompanham mudanças sociais recentes
- Podem perpetuar visões ultrapassadas

#### Viés de Plataforma
- Reddit, Twitter, sites de notícias têm demografias específicas
- Perspectivas de usuários de internet ≠ população geral
- Vieses de classe e educação

### O Problema da Amplificação

LLMs não apenas replicam vieses — eles podem **amplificá-los**:

**Mecanismo**:
1. Modelo aprende correlação fraca nos dados
2. Ao gerar texto, reforça essa correlação
3. Texto gerado pode treinar próxima geração de modelos
4. Viés se fortalece em loop de feedback

**Exemplo**:
```
Dados: 60% dos CEOs em textos são homens
Modelo aprende: CEO → provavelmente homem
Modelo gera: Textos onde 80% dos CEOs são homens
Loop: Viés aumentou de 60% para 80%
```

## 🔍 Exemplo Prático

**Experimento: Teste de Associação Implícita em LLMs**

```
Teste 1: Complete as frases

"O engenheiro negro..."
"O engenheiro asiático..."
"O engenheiro branco..."

Analise: As continuações diferem em tom ou conteúdo?

Teste 2: Analogias

"Homem : Forte :: Mulher : ?"
"Médico : Homem :: Enfermeira : ?"

Resultado esperado: Modelos podem reproduzir estereótipos

Teste 3: Perspectiva Cultural

"Explique a importância da família"
(Resposta tende a refletir valores ocidentais individualist as?)

"Descreva um jantar típico"
(Assume culinária americana/europeia?)
```

### Como Investigadores Medem Vieses

**1. Testes de Associação Implícita (IAT)**
- Medem tempo de resposta para associações
- Adaptados para embeddings de IA

**2. Análise de Corpus**
- Examinar grandes volumes de saídas do modelo
- Identificar padrões sistemáticos

**3. Testes Contrafactuais**
```
"João é um excelente programador" vs
"Maria é uma excelente programadora"

Modelo completa diferente?
```

**4. Benchmarks de Fairness**
- Datasets especializados (WinoBias, BBQ, etc.)
- Métricas quantitativas de viés

## 🤔 Questões para Reflexão

1. Se LLMs apenas refletem vieses humanos existentes, corrigi-los é uma forma de censura ou de justiça social? Onde está a linha?

2. É possível criar um modelo "sem vieses"? Ou todo recorte de dados necessariamente representa alguma perspectiva?

3. Como psicólogo, você reconhece seus próprios vieses nos textos que escreve? LLMs nos dão um espelho objetivo de nossos pontos cegos coletivos?

4. Vieses podem ser úteis? Exemplo: viés de sobrevivência nos ajuda a aprender com sucessos. Quando vieses são adaptativos vs. prejudiciais?

5. Se treinarmos LLMs em textos "corrigidos" para remover vieses, estamos criando representação mais justa da realidade ou uma versão idealizada que não existe?

6. Como lidar com vieses culturais quando IA é usada globalmente? Valores ocidentais devem ser "padrão"?

## 📚 Referências

**Papers Fundamentais**:
- "Man is to Computer Programmer as Woman is to Homemaker?" (Bolukbasi et al., 2016)
- "Gender Shades: Intersectional Accuracy Disparities" (Buolamwini & Gebru, 2018)
- "On the Dangers of Stochastic Parrots" (Bender et al., 2021)
- "Examining Gender and Race Bias in Large Language Models" (Liang et al., 2022)

**Livros**:
- "Weapons of Math Destruction" - Cathy O'Neil
- "Algorithms of Oppression" - Safiya Noble
- "Thinking, Fast and Slow" - Daniel Kahneman (vieses cognitivos humanos)

**Ferramentas**:
- [Hugging Face Evaluate - Fairness Metrics](https://huggingface.co/spaces/evaluate-measurement/fairness)
- [AI Fairness 360](https://aif360.mybluemix.net/) - IBM
- [What-If Tool](https://pair-code.github.io/what-if-tool/) - Google

**Organizações**:
- Partnership on AI
- AI Now Institute
- Algorithmic Justice League

## ➡️ Próximos Passos

- **Aprofunde**: Leia sobre [Ética no Uso de IA](11-ética-no-uso-de-ia)
- **Conecte**: Veja [Antropomorfização de IAs](09-antropomorfizacao-de-ias.md) - outro viés psicológico
- **Pratique**: Teste vieses usando prompts contrafactuais

---

**Autor**: Gabriel - Arquiteto Cognitivo  
**Última atualização**: Janeiro 2025
