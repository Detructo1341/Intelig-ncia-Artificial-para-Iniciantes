# Context Window Explicado: A Memória Limitada da IA

## 🎯 O que você vai aprender

Context window é o **limite de memória** de um LLM — quantos tokens ele pode "lembrar" de uma vez. Entender isso é crucial para interações eficazes, especialmente em conversas longas ou análises de documentos extensos.

## 🧠 Por que isso importa?

- **Evita frustrações**: "Por que a IA esqueceu o que eu disse?"
- **Otimiza custos**: Tokens custam dinheiro em APIs
- **Melhora estratégia**: Saber quando dividir tarefas
- **Entende limitações**: IA não tem memória de longo prazo real

**Analogia cognitiva**: Context window é como **memória de trabalho** (working memory) humana — processa 5-9 itens simultâneos, depois "esquece".

---

## 📖 Explicação

### O que é Context Window?

O **número máximo de tokens** (palavras + fragmentos) que um LLM pode processar de uma vez, incluindo:

1. **Prompt de sistema** (instruções para a IA)
2. **Histórico de conversa** (mensagens anteriores)
3. **Seu prompt atual** (nova pergunta)
4. **Resposta gerada** (output da IA)

**Matemática simples**:
```
Context Window Total = Prompt Sistema + Histórico + Prompt Atual + Resposta
```

---

### Tamanhos de Context Window (2024)

| Modelo | Context Window | Equivalente em palavras |
|--------|----------------|-------------------------|
| GPT-3.5 Turbo | 16k tokens | ~12.000 palavras |
| GPT-4 | 8k / 32k tokens | ~6k / ~24k palavras |
| GPT-4 Turbo | 128k tokens | ~96.000 palavras |
| Claude 3 Opus | 200k tokens | ~150.000 palavras |
| Claude 3.5 Sonnet | 200k tokens | ~150.000 palavras |
| Gemini 1.5 Pro | 1M tokens | ~750.000 palavras |

**Referência**: 1 token ≈ 0,75 palavras em português

---

## 🔄 O que Acontece Quando o Limite é Atingido?

### Estratégias de Diferentes Modelos

#### 1. **Truncamento (Corte)**
```
Conversa: [msg 1, msg 2, msg 3, ..., msg 50]
Context cheio → Remove msg 1, msg 2...
Mantém: [msg 40, msg 41, ..., msg 50]
```
✅ Simples  
❌ Perde contexto importante do início

#### 2. **Sumarização Automática**
```
Conversa: [histórico longo]
Context cheio → Gera resumo do início
Mantém: [resumo] + [mensagens recentes]
```
✅ Preserva informação essencial  
⚠️ Pode perder nuances

#### 3. **Erro e Recusa**
```
Context cheio → "Erro: Token limit exceeded"
```
❌ Interrompe fluxo

---

## 🧠 Psicologia do Context Window

### Paralelo com Memória Humana

| Memória Humana | LLM Context Window |
|----------------|---------------------|
| **Memória de Trabalho**: 5-9 itens | Context window ativo |
| **Memória de Longo Prazo**: Ilimitada | ❌ Não existe em LLMs |
| **Chunking**: Agrupar info para lembrar mais | Técnicas de prompt design |
| **Rehearsal**: Repetir para não esquecer | Re-injetar contexto no prompt |

**Diferença crítica**: Humanos transferem memória de trabalho para longo prazo. LLMs **não**.

---

## 🛠️ Estratégias para Gerenciar Context Window

### 1. **Chunking (Divisão em Partes)**

**Problema**: Documento de 200 páginas para analisar

**Solução**:
```python
# Divide em chunks de 10 páginas
for i in range(20):
    chunk = documento[i*10:(i+1)*10]
    resposta = llm.analyze(chunk)
    resumos.append(resposta)

# Depois analisa resumos agregados
analise_final = llm.synthesize(resumos)
```

---

### 2. **Técnica do Resumo Progressivo**

**Conversa longa**:
```
Turno 1-10: Discussão sobre ansiedade
Turno 11-20: Técnicas de respiração
Turno 21-30: Exercícios práticos
```

**A cada 10 turnos**:
```
Prompt: "Resuma nossa conversa até agora em 3 frases"
[Salva resumo]
[Continua com resumo + novas mensagens]
```

---

### 3. **Prompts Autocontidos**

**❌ Dependente de contexto**:
```
Msg 1: "Analise este relatório [10k palavras]"
Msg 2: "Qual a conclusão sobre vendas?" 
```
→ Se contexto for perdido, msg 2 falha

**✅ Autocontido**:
```
Msg 1: "Analise este relatório [10k palavras]"
Msg 2: "No relatório sobre vendas Q3 2024 que enviei, 
        qual a conclusão sobre performance regional?"
```
→ Funciona mesmo se contexto anterior for truncado

---

### 4. **Uso de Memória Externa**

**Para desenvolvedores**:
```python
# Armazena contexto importante em banco de dados
memory_store = {
    "user_preferences": {...},
    "conversation_summary": "...",
    "key_facts": [...]
}

# Injeta seletivamente no prompt
prompt = f"""
Contexto relevante: {memory_store['key_facts']}
Nova pergunta: {user_input}
"""
```

---

## 🔍 Exemplo Prático: Gestão de Context Window

### Cenário: Revisão de TCC

**Documento**: 80 páginas (≈60k palavras = ~80k tokens)  
**Context window**: 32k tokens

**❌ Abordagem Ingênua**:
```
"Leia meu TCC [cola 80 páginas] e me dê feedback"
```
Resultado: Erro ou truncamento severo

**✅ Abordagem Estratégica**:

```python
# Etapa 1: Resumo por capítulo
for capitulo in tcc.capitulos:
    resumo = llm.resumir(capitulo, max_tokens=500)
    resumos.append(resumo)

# Etapa 2: Análise estrutural
prompt = f"""
Resumos dos capítulos:
{resumos}

Analise:
1. Coerência entre capítulos
2. Gaps argumentativos
3. Sugestões de melhoria
"""

# Etapa 3: Aprofundamento seletivo
"Agora leia apenas o Capítulo 3 [texto completo] e critique metodologia"
```

---

## 🤔 Questões para Reflexão

1. **Se LLMs tivessem memória infinita, isso os tornaria "conscientes"?** Ou memória é apenas parte da equação?

2. **Context window limitado é bug ou feature?** Força usuários a serem concisos?

3. **Para psicólogos**: Limite de memória humana é evolutivamente adaptativo. E para IAs?

4. **Modelos com 1M tokens (Gemini) são "melhores"?** Ou há tradeoffs de qualidade?

5. **Se você pudesse "congelar" partes do contexto (nunca esquecer), o que você congelaria?**

---

## 🧪 Experimentos

### Experimento 1: Teste de Limite
```
1. Inicie conversa
2. A cada turno, pergunte: "Você se lembra do que eu disse na mensagem 1?"
3. Continue até a IA esquecer
4. Conte quantos turnos foram necessários
```

### Experimento 2: Resumo vs. Texto Completo
```
A) Envie documento longo pedindo análise completa
B) Envie resumo do documento pedindo análise

Compare qualidade das respostas
```

### Experimento 3: Chunking Eficaz
```
Divida texto em:
A) Chunks aleatórios de 1000 tokens
B) Chunks semânticos (por seção/tópico)

Qual preserva mais coerência?
```

---

## 📚 Referências

### Papers
- **"Attention Is All You Need"** – Vaswani et al. (2017) [Base do Transformer]
- **"Long Range Arena"** – Tay et al. (2020) [Desafios de longo contexto]
- **"Lost in the Middle"** – Liu et al. (2023) [LLMs esquecem info no meio do contexto]

### Recursos Técnicos
- **OpenAI Token Counting**: [OpenAI Tokenizer](https://platform.openai.com/tokenizer)
- **LangChain Memory**: [Docs sobre gerenciamento de memória](https://python.langchain.com/docs/modules/memory/)

### Artigos
- **"Understanding Context Windows"** – Anthropic Blog
- **"Effective Context Management"** – OpenAI Cookbook

---

## ➡️ Próximos Passos

1. **[Como Funcionam os LLMs](como-funcionam-os-llms.md)** → Entenda por que contexto é limitado
2. **[Tipos de Prompting](tipos-de-prompting.md)** → Técnicas para lidar com contexto longo
3. **[RAG (Retrieval Augmented Generation)](rag-retrieval-augmented-generation.md)** → Superar limitações de contexto

---

## 🎓 Nota do Autor

Context window é a **memória de trabalho da IA**. Assim como humanos precisam de anotações para lembrar de informações complexas, LLMs precisam de estratégias de gestão de contexto.

A limitação não é fraqueza — é característica. Aprenda a trabalhar com ela, não contra ela.

Como psicólogo, você entende que limitações cognitivas moldam como pensamos. O mesmo vale para IA. Context window define **como** interagimos com ela.

---

**Escrito por Gabriel, Arquiteto Cognitivo**  
*Última atualização: Dezembro 2024*
