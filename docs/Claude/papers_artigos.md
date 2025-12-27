# Papers e Artigos Importantes - IA Generativa

Guia curado de pesquisas fundamentais que moldaram o campo de IA Generativa. Organizado por tópico e impacto.

---

## 🎯 Fundações (Leitura Essencial)

### 1. **"Attention Is All You Need"** (2017)
**Autores**: Vaswani et al.  
**Publicado em**: Proceedings of NeurIPS  
**Link**: https://arxiv.org/abs/1706.03762

**Por quê ler**: Define a arquitetura Transformer que é base de TODOS os LLMs modernos. Altamente impactante.

**Contexto**: Antes disso, RNNs dominavam. Este paper mostrou que você pode fazer tudo melhor com apenas atenção.

**Dificuldade**: Média-Alta. Requer conhecimento de redes neurais, mas é bem escrito.

---

### 2. **"Language Models are Unsupervised Multitask Learners"** (2019)
**Autores**: Radford et al. (OpenAI)  
**Conhecido como**: GPT-2 Paper  
**Link**: https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf

**Por quê ler**: Demonstra que modelos grandes conseguem fazer múltiplas tarefas sem treinamento específico (in-context learning).

**Contexto**: Um dos primeiros sinais de que aumentar escala gera capacidades emergentes.

**Dificuldade**: Baixa. Mais acessível que papers anteriores.

---

### 3. **"Language Models are Few-Shot Learners"** (2020)
**Autores**: Brown et al. (OpenAI)  
**Conhecido como**: GPT-3 Paper  
**Link**: https://arxiv.org/abs/2005.14165

**Por quê ler**: Mostrou que few-shot learning em larga escala é viável. Fundamentação teórica de como LLMs funcionam.

**Contexto**: GPT-3 tem 175B parâmetros. Primeiro grande modelo que mostrou verdadeiras capacidades conversacionais.

**Dificuldade**: Média. Longo mas bem organizado.

---

## 🔬 Mecanismos e Técnicas

### 4. **"BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding"** (2018)
**Autores**: Devlin et al. (Google)  
**Link**: https://arxiv.org/abs/1810.04805

**Por quê ler**: Mostrou treinamento bidirecional em larga escala. Importante para entender diferentes abordagens de treinamento.

**Contexto**: BERT foi revolucionário na época, embora GPT-style (unidirecional) tenha prevalecido para geração.

**Dificuldade**: Média.

---

### 5. **"Scaling Laws for Neural Language Models"** (2020)
**Autores**: Kaplan et al. (OpenAI)  
**Link**: https://arxiv.org/abs/2001.08361

**Por quê ler**: Estabelece padrões matemáticos de como performance melhora com tamanho de modelo, dados e computação.

**Contexto**: Explica por que "mais grande = melhor" até certo ponto. Guiou decisões de design do GPT-3.

**Dificuldade**: Média-Alta. Matemática técnica, mas insights claros.

---

### 6. **"Emergent Abilities of Large Language Models"** (2022)
**Autores**: Wei et al. (Google)  
**Link**: https://arxiv.org/abs/2206.07682

**Por quê ler**: Define e explora "emergência" - quando modelos mostram capacidades não explicitamente treinadas.

**Contexto**: Por que um modelo de 7B pode ser "burro" mas 70B é "inteligente"?

**Dificuldade**: Média.

---

### 7. **"Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"** (2022)
**Autores**: Wei et al. (Google)  
**Link**: https://arxiv.org/abs/2201.11903

**Por quê ler**: Demonstra que pedir ao modelo para "pensar em voz alta" melhora significativamente precisão em tarefas complexas.

**Contexto**: Um dos papers mais impactantes de prompt engineering.

**Dificuldade**: Baixa. Muito acessível.

---

### 8. **"Prompt Engineering for Biomedical Named Entity Recognition via LLMs"** (2023)
**Autores**: Varios  
**Contexto**: Exemplo de como técnicas de prompt engineering se aplicam a domínios específicos.

---

## 🧠 Comportamento e Interpretabilidade

### 9. **"Mechanistic Interpretability for Large Language Models"** (2023)
**Autores**: Nanda et al.  
**Link**: https://www.anthropic.com/research

**Por quê ler**: Como podemos entender o que LLMs estão fazendo internamente? Importante para segurança.

**Contexto**: Crescente foco em "interpretabilidade" - abrir a "caixa preta".

**Dificuldade**: Alta. Altamente técnico.

---

### 10. **"Constitutional AI: Harmlessness from AI Feedback"** (2022)
**Autores**: Bai et al. (Anthropic)  
**Link**: https://arxiv.org/abs/2212.08073

**Por quê ler**: Abordagem inovadora para fazer LLMs mais seguros e alinhados com valores humanos.

**Contexto**: Como treinar modelos de forma ética?

**Dificuldade**: Média.

---

## 🎨 Modelos Multimodais

### 11. **"An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale"** (2020)
**Autores**: Dosovitskiy et al.  
**Conhecido como**: Vision Transformer (ViT)  
**Link**: https://arxiv.org/abs/2010.11929

**Por quê ler**: Mostra como Transformers funcionam não apenas com texto mas com imagens também.

**Contexto**: Base teórica para modelos multimodais modernos.

**Dificuldade**: Média.

---

### 12. **"Learning Transferable Visual Models From Natural Language Supervision"** (2021)
**Autores**: Radford et al. (OpenAI)  
**Conhecido como**: CLIP  
**Link**: https://arxiv.org/abs/2103.14030

**Por quê ler**: CLIP é revolucionário para conectar visão e linguagem. Base de muitos sistemas multimodais.

**Contexto**: Como treinar um modelo com imagens + textos juntos?

**Dificuldade**: Média.

---

## 💾 Eficiência e Otimização

### 13. **"LoRA: Low-Rank Adaptation of Large Language Models"** (2021)
**Autores**: Hu et al.  
**Link**: https://arxiv.org/abs/2106.09685

**Por quê ler**: Técnica revolucionária que permite fine-tuning de modelos gigantes com fração do custo.

**Contexto**: Por quê usar LoRA em vez de fine-tuning completo?

**Dificuldade**: Média.

---

### 14. **"Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference"** (2018)
**Autores**: Jacob et al. (Google)  
**Link**: https://arxiv.org/abs/1806.08342

**Por quê ler**: Como comprimir modelos sem perder muita performance.

**Contexto**: Importante para rodar LLMs em dispositivos móveis.

**Dificuldade**: Alta. Técnico.

---

## 🔐 Segurança e Alinhamento

### 15. **"Towards a Unified Theory of Deep Undermining in Language Models"** (2023+)
**Contexto**: Crescente pesquisa em adversarial attacks contra LLMs.

---

### 16. **"Language Models Can Explain Themselves"** (2023)
**Autores**: Varios  
**Contexto**: LLMs podem explicar por que deram uma resposta? Importante para auditoria.

---

## 📊 Avaliação e Benchmarks

### 17. **"MMLU: A Massive Multitask Language Understanding"** (2020)
**Autores**: Hendrycks et al.  
**Link**: https://arxiv.org/abs/2009.03300

**Por quê ler**: Define benchmark padrão para avaliar LLMs em múltiplas disciplinas.

**Contexto**: Como comparar quantitativamente a "inteligência" de modelos?

**Dificuldade**: Baixa. Mais um dataset que paper teórico.

---

### 18. **"BIG-bench: A Benchmark for Language Models"** (2023)
**Autores**: Suzgun et al. (Google)  
**Link**: https://arxiv.org/abs/2301.12873

**Por quê ler**: Benchmark inclusivo com 200+ tarefas. Bom para ver range completo de capacidades.

**Contexto**: Mais abrangente que MMLU.

**Dificuldade**: Baixa.

---

## 🌍 Aplicações Práticas

### 19. **"GPT-3.5 Technical Report"** (ChatGPT Release)
**Disponível**: OpenAI blog

**Por quê ler**: Documenta diferenças entre GPT-3 e GPT-3.5 (que rodeia ChatGPT).

---

### 20. **"Sparks of Artificial General Intelligence: Early experiments with GPT-4"** (2023)
**Autores**: Bubeck et al. (Microsoft)  
**Link**: https://arxiv.org/abs/2303.12712

**Por quê ler**: Análise aprofundada de capacidades emergentes do GPT-4. Especulativo mas insightful.

**Contexto**: Estamos perto de AGI? Que capacidades faltam?

**Dificuldade**: Média. Mais especulativo que técnico.

---

## 🔮 Pesquisa Atual (Fronteira)

### Tópicos em Evolução Rápida (2024-2025):

- **Mixture of Experts (MoE)**: Modelos que não ativam todos os parâmetros. Mais eficientes.
- **Multimodal Alignment**: Conectar texto, imagem, áudio melhor.
- **Reasoning and Planning**: LLMs melhores em tarefas multi-step complexas.
- **Efficient Transformers**: Variações com menos complexidade computacional.
- **Retrieval-Augmented Generation (RAG)**: Combinar busca com geração.
- **Agent Systems**: LLMs como agentes autônomos que planejam e executam.

---

## 📚 Recursos para Encontrar Papers

- **ArXiv**: https://arxiv.org/ (repositório principal de papers)
- **OpenReview**: https://openreview.net/ (conferências como NeurIPS, ICLR)
- **Anthropic Research**: https://www.anthropic.com/research
- **Google AI Blog**: https://ai.googleblog.com/
- **OpenAI Research**: https://openai.com/research/
- **Papers with Code**: https://paperswithcode.com/ (papers + implementações)

---

## 🎓 Como Ler Papers Acadêmicos

1. **Começar pelo abstract e conclusão** - Entenda o objetivo e resultado
2. **Depois ler introdução** - Contexto e motivação
3. **Pular para figuras/gráficos** - Insights visuais
4. **Ler seções relevantes** - Nem sempre precisa ler tudo
5. **Ignorar math densa** - Se não entender uma equação, não é o fim do mundo
6. **Procurar no Google** - Se não entender algo, provavelmente alguém explicou em blog

**Dica de um psicólogo**: Reler papers em tempos diferentes ajuda (spaced repetition). Você vai entender mais a cada passada!

---

## 🤝 Discussões e Comunidades

- **r/MachineLearning**: Reddit com discussões técnicas
- **Papers with Code Discussions**: Comunidade comentando papers
- **Twitter/X Machine Learning**: Pesquisadores compartilhando insights
- **Hugging Face Forums**: Comunidade prática
- **Anthropic/OpenAI Communities**: Comunidades oficiais

---

**Última atualização**: Dezembro 2024

Este documento está em evolução. Novos papers fundamentais surgem frequentemente!
