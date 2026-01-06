# Tutor de IA Generativa

---

Guia prático para entender como funcionam sistemas de IA moderna, com explicações acessíveis e analogias do mundo real.

**Recursos disponíveis:**
- **Glossário técnico completo**: `references/glossario.md` (50+ termos)
- **Papers e artigos fundamentais**: `references/papers_artigos.md`
- **Tópicos avançados**: `references/topicos.md`
- **Agentes de IA - Guia prático**: `references/agentes_ia.md` (baseado em guias oficiais Anthropic)

---

## Conceitos Fundamentais

### O Que É IA Generativa?

Sistema computacional que cria novo conteúdo aprendendo padrões de dados. Diferente de programas tradicionais (seguem regras fixas), a IA Generativa aprende padrões e os usa para gerar texto, imagens ou código.

**Analogia:** Escritor bem-lido que, após ler milhões de livros, consegue escrever histórias originais combinando padrões aprendidos (não decora, mas entende como histórias funcionam).

### Como Funcionam Modelos de Linguagem (LLMs)

**Tarefa central:** Predizer a próxima palavra baseado em padrões estatísticos.

**Processo:**
1. "O céu está..." → calcula probabilidades (azul: 60%, nublado: 20%, etc.)
2. Escolhe "azul" → "O céu está azul..."
3. Repete palavra por palavra até completar a resposta

**Treinamento:**
- Modelo vê bilhões de textos
- Aprende quais palavras aparecem juntas
- Ajusta milhões de parâmetros internos para melhorar previsões

**Analogia:** Reconhecimento de rostos - após ver milhões de fotos, aprende padrões ("olhos azuis geralmente aparecem com..."). LLMs fazem isso com relações entre palavras.

---

## Tokens: Unidade Básica de Processamento

**Token** = pequeno pedaço de texto (não necessariamente palavra inteira).

**Exemplos:**
- "Olá" = 1 token
- "ChatGPT" = 2-3 tokens (Chat|GP|T)
- "2024" = 1 token
- Emoji = 1 token

**Por que importa:**
- APIs cobram por tokens
- Modelos têm limite de contexto (ex: 128.000 tokens)
- Otimização de prompts

**Regra prática:** 1 palavra ≈ 1.3 tokens

---

## Transformers: Arquitetura Core

Base de todos os LLMs modernos (GPT, Claude, Gemini). Proposta em 2017.

**Mecanismo de Atenção (Attention):**
Cada palavra "pergunta": quais outras palavras são relevantes para mim?

**Exemplo:**
- Frase: "O gato subiu no telhado e **ele** desceu"
- Pronome "ele" presta atenção em "gato" (90% de atenção)
- Assim o modelo entende sobre quem está falando

**Analogia:** Professor que vê todos alunos simultaneamente e nota relações entre eles ("João e Maria conversam sobre o mesmo tópico").

Para detalhes técnicos: `references/topicos.md` (seção Transformers)

---

## Prompt Engineering: Comunicação Eficaz

Técnicas para instruções claras:

**1. Seja específico**
- ❌ "Explique IA"
- ✅ "Explique redes neurais em linguagem simples para iniciante"

**2. Forneça contexto**
- ❌ "O que você acha?"
- ✅ "Sou psicólogo. Como IA modela comportamento humano?"

**3. Use exemplos (Few-shot)**
```
Traduza:
- "Hello" → "Olá"
- "Good morning" → "Bom dia"
- "Thank you" → ?
```

**4. Defina estilo**
- "Explique como professor para criança de 10 anos"
- "Explique como pesquisador acadêmico"

**5. Quebre tarefas complexas**
- ✅ "1) Resuma em 3 frases. 2) Identifique argumentos. 3) Critique evidências"

**Chain-of-Thought:** Peça raciocínio passo a passo
- ✅ "Quanto é 17 × 23? Mostre seu raciocínio"
- Resultado: menos erros!

Mais técnicas: `references/topicos.md` (seção Prompt Engineering)

---

## Conceitos Técnicos Essenciais

### Fine-Tuning
Adaptar modelo pré-treinado para tarefa específica com dados adicionais.

**Analogia:** Médico generalista faz especialização em cardiologia.

**Quando usar:**
- ✅ Muitos exemplos de padrão específico
- ✅ Estilo/tom muito particular
- ❌ Se prompt engineering resolve

### Modelos Multimodais
Processam múltiplos tipos de dados: texto, imagem, áudio, vídeo.

**Exemplos:**
- GPT-4 Vision: analisa imagens
- DALL-E: texto → imagem
- Whisper: áudio → texto

**Arquitetura:**
1. Encoders convertem dados em representação numérica
2. Processador unificado analisa tudo junto
3. Decoder gera resposta

### Temperatura
Controla criatividade vs. previsibilidade.

- **Baixa (0.1):** Respostas previsíveis
- **Alta (0.9):** Respostas criativas (mas pode gerar texto estranho)

**Analogia:** Músico improvisando - baixa temperatura toca notas comuns, alta temperatura toma riscos.

### Embeddings
Representação numérica de palavras que captura significado.

**Exemplo:**
- "Rei" → [0.2, 0.8, 0.1, ...]
- "Rainha" → [0.3, 0.75, 0.2, ...]
- "Rainha" está numericamente mais perto de "Rei" (conceitos relacionados)

Detalhes matemáticos: `references/topicos.md`

---

## Agentes de IA: Além de Chamadas Únicas

**Agente:** Sistema onde LLMs direcionam dinamicamente seus próprios processos e uso de ferramentas em loop.

### Diferença: Workflows vs. Agentes

**Workflows:** LLMs e ferramentas orquestrados através de código pré-definido
- Previsíveis e consistentes
- Ideais para tarefas bem-definidas

**Agentes:** LLMs que decidem dinamicamente próximos passos
- Flexíveis e adaptáveis
- Ideais quando não é possível prever etapas necessárias

### Padrões Comuns de Workflows

**Prompt Chaining:** Sequência de passos onde cada LLM processa saída do anterior

**Routing:** Classifica input e direciona para tarefa especializada

**Parallelization:** Múltiplos LLMs trabalham simultaneamente

**Orchestrator-Workers:** LLM central delega subtarefas a workers

**Evaluator-Optimizer:** Um LLM gera, outro avalia em loop iterativo

### Quando Usar Agentes

✅ **Use quando:**
- Problema aberto (difícil prever número de passos)
- Não pode codificar caminho fixo
- Precisa escalar tarefas em ambiente confiável

❌ **Não use quando:**
- Uma chamada de LLM com retrieval é suficiente
- Previsibilidade total é crítica
- Tarefa simples e bem-definida

### Engenharia de Contexto

**Desafio:** Context rot - conforme tokens aumentam, capacidade de recall diminui.

**Solução:** Tratar contexto como recurso finito precioso. Curar menor conjunto possível de tokens de alto sinal.

**Técnicas para tarefas longas:**
- **Compaction:** Resumir e comprimir conversação próxima ao limite
- **Note-taking:** Agente escreve notas persistidas fora do contexto
- **Sub-agents:** Agentes especializados com janelas limpas

Para guia completo: `references/agentes_ia.md`

---

## Aplicações e Limitações

### Pontos Fortes
- Escrever/editar textos
- Explicar conceitos
- Gerar/debugar código
- Brainstorming
- Resumos e traduções
- Análise de dados

### Limitações Críticas
- **Alucinações:** Inventa informações com confiança (sempre verifique!)
- **Data de corte:** Conhecimento limitado à época de treinamento
- **Sem compreensão real:** Reconhece padrões, não "entende"
- **Vieses:** Reproduz preconceitos dos dados de treinamento
- **Contexto limitado:** Esquece informações antigas
- **Criatividade limitada:** Recombina padrões, não cria algo totalmente novo

**Analogia:** Loro inteligente - repete/remixa conversas impressionantemente, mas não entende verdadeiramente nem tem intuição real.

---

## Navegação e Aprofundamento

**Para conceitos específicos:** Consulte `references/glossario.md`

**Para estudos acadêmicos:** Veja papers fundamentais em `references/papers_artigos.md`

**Para tópicos avançados:** Explore RAG, RLHF, quantização, e mais em `references/topicos.md`

**Para agentes de IA:** Guia prático completo sobre construção de agentes, workflows e engenharia de contexto em `references/agentes_ia.md`

**Prática:** A melhor forma de aprender é experimentando. Teste as técnicas de prompt engineering!
