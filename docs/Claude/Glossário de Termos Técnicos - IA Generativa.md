# Glossário de Termos Técnicos - IA Generativa

## A

**Ativação (Activation Function)**
Função matemática usada em redes neurais que decide se um neurônio deve "disparar". Exemplos: ReLU, Sigmoid, Tanh. Sem ativações não-lineares, redes neurais seriam apenas combinações lineares.

**Alucinação (Hallucination)**
Quando um modelo de IA gera informação que parece confiável mas é falsa ou inventada. Exemplo: um modelo pode inventar um paper acadêmico com título, autores e detalhes convincentes que não existem.

**Atenção (Attention)**
Mecanismo em Transformers que permite o modelo entender quais partes do texto são mais relevantes para fazer uma previsão. Cada palavra "presta atenção" em outras palavras.

**Autocomplete**
Função básica de LLMs: prever e completar automaticamente o que você está digitando. Base de como funcionam chatbots.

## B

**Backpropagation**
Algoritmo para treinar redes neurais. Calcula como cada parâmetro da rede contribui para o erro e os ajusta. Essencial para aprendizado profundo.

**Bias (Preconceito de Dados)**
Quando um modelo reproduz preconceitos presentes nos dados de treinamento. Exemplo: um modelo treinado com mais exemplos de médicos homens pode ter viés de gênero.

**Bias (Termo em Redes Neurais)**
Parâmetro adicional em neurônios que permite ao modelo fazer previsões melhores. Diferente de "preconceito de dados".

**Benchmark**
Teste padronizado para avaliar performance de modelos. Exemplo: MMLU (teste com múltiplas escolhas em várias disciplinas).

**BERT**
Modelo de linguagem desenvolvido pelo Google (2018). Importante porque processava texto em ambas as direções (bidirecional).

**BPE (Byte Pair Encoding)**
Algoritmo para converter texto em tokens. Encontra pares de bytes mais frequentes e os substitui.

## C

**Chain-of-Thought (CoT)**
Técnica de prompt engineering onde você pede ao modelo para mostrar seu raciocínio passo a passo. Melhora muito a precisão.

**ChatGPT**
Modelo de linguagem conversacional da OpenAI (lançado em 2022). Trouxe IA generativa para o público em larga escala.

**Claude**
Modelo de linguagem desenvolvido pela Anthropic, com foco em ser seguro e útil.

**Classificação (Classification)**
Tarefa onde o modelo coloca um texto em uma ou mais categorias. Exemplo: classificar email como "spam" ou "legítimo".

**Codificador (Encoder)**
Parte de um modelo que converte dados de entrada (texto, imagens) em representação interna que a rede consegue processar.

**Contexto (Context)**
Informação anterior em uma conversa ou texto que influencia a previsão do próximo token. Modelos têm limite de contexto (janela de tokens que conseguem considerar).

## D

**DALL-E**
Modelo gerador de imagens da OpenAI. Dado um texto, gera imagens correspondentes.

**Decodificador (Decoder)**
Parte de um modelo que converte representação interna em saída (texto, imagem, áudio).

**Deepfake**
Mídia (geralmente vídeo) sintetizada por IA que imita uma pessoa real. Levanta questões éticas importantes.

**Dropout**
Técnica de regularização onde você "desativa" aleatoriamente alguns neurônios durante treinamento. Previne overfitting.

## E

**Embedding**
Representação de palavras/conceitos como vetores de números. Palavras com significado similar têm embeddings próximos. Fundamental para processamento de linguagem.

**Emergência (Emergence)**
Quando um modelo mostra capacidades não vistas durante treinamento. Exemplo: um modelo treinado para tradução começar a fazer math sem ser ensinado explicitamente.

**Encoder-Decoder**
Arquitetura que tem duas partes: encoder (processa entrada) e decoder (gera saída). Comum em modelos de tradução.

## F

**Fine-tuning**
Processo de adaptar um modelo pré-treinado para uma tarefa específica usando dados adicionais. Como uma especialização médica.

**Few-Shot Learning**
Quando você mostra alguns poucos exemplos (geralmente 1-5) ao modelo e ele consegue generalizar. Diferente de zero-shot (sem exemplos).

**Função de Perda (Loss Function)**
Métrica que mede o quão errado o modelo está. Durante treinamento, tenta-se minimizar isso.

## G

**Gemini**
Modelo multimodal do Google que consegue processar texto, imagem, áudio e vídeo.

**Gradiente (Gradient)**
Direção e magnitude de como mudar os parâmetros para melhorar o modelo. Essencial para otimização.

## H

**Hallucination** (ver Alucinação)

**Hugging Face**
Plataforma e comunidade que disponibiliza muitos modelos open-source de IA. Recurso muito importante para pesquisadores.

## I

**IA Generativa (Generative AI)**
Sistema de IA que consegue criar novo conteúdo (texto, imagem, áudio) a partir de padrões aprendidos.

**Inferência (Inference)**
Processo de usar um modelo treinado para fazer previsões em dados novos. Oposto de treinamento.

**In-Context Learning**
Capacidade de um modelo aprender a partir de exemplos fornecidos no prompt (em tempo de inferência), sem re-treinamento.

## J

**Jailbreak**
Técnica para contornar as proteções e limitações de um modelo de IA. Levanta questões de segurança.

## K

**Knowledge Cutoff**
Data até a qual um modelo foi treinado. Informação posterior é desconhecida (a menos que o modelo tenha acesso a web).

**Kernel**
Em redes neurais convolucionais, matriz pequena que desliza sobre a entrada detectando padrões.

## L

**LLM (Large Language Model)**
Modelo de linguagem grande com bilhões/trilhões de parâmetros. Exemplos: GPT-4, Claude, Gemini.

**LoRA (Low-Rank Adaptation)**
Método eficiente de fine-tuning que modifica apenas uma pequena fração dos parâmetros. Muito mais barato que fine-tuning completo.

## M

**Machine Learning (Aprendizado de Máquina)**
Campo da IA focado em algoritmos que aprendem a partir de dados.

**Multimodal**
Modelo que consegue processar múltiplos tipos de dados simultaneamente. Exemplo: texto + imagem.

**Mask Language Modeling**
Técnica de treinamento onde você oculta (máscara) algumas palavras e o modelo tenta prever. Usado em BERT.

## N

**Neurônio (Neuron)**
Unidade básica de uma rede neural. Recebe inputs, aplica operações matemáticas, produz output.

**Neural Network (Rede Neural)**
Estrutura computacional inspirada no cérebro, composta de camadas de neurônios conectados.

**Normalização (Normalization)**
Técnica de pré-processamento que coloca dados em escala similar (ex: entre 0 e 1). Melhora treinamento.

**Núcleo/Core (Core)**
Componente fundamental de uma arquitetura. Exemplo: "core do Transformer é o mecanismo de atenção".

## O

**OpenAI**
Empresa que desenvolveu GPT e ChatGPT.

**Otimizador (Optimizer)**
Algoritmo que ajusta parâmetros do modelo para minimizar a função de perda. Exemplos: SGD, Adam.

**Overfitting**
Quando um modelo memoriza dados de treinamento e não generaliza bem para dados novos. Como estudar apenas para a prova específica ao invés de aprender o conceito.

## P

**Parâmetro (Parameter)**
Número ajustável em uma rede neural. GPT-3 tem 175 bilhões de parâmetros!

**Perplexidade (Perplexity)**
Métrica que mede quão bem um modelo de linguagem prediz um texto. Quanto menor, melhor.

**Prompt**
Texto de entrada que você escreve para fazer uma requisição ao modelo de IA.

**Prompt Engineering**
Prática de escrever prompts eficazes para obter melhores respostas da IA.

## Q

**Quantização (Quantization)**
Técnica para reduzir o tamanho de um modelo convertendo números de precisão alta para precisão baixa. Torna modelos mais rápidos e eficientes.

## R

**Regularização (Regularization)**
Técnicas para prevenir overfitting. Exemplos: dropout, weight decay, early stopping.

**RNN (Recurrent Neural Network)**
Tipo de rede neural que processa sequências processando um elemento por vez, mantendo "memória" do que viu. Precursora dos Transformers.

**Retrieval-Augmented Generation (RAG)**
Técnica que combina recuperação de informação com geração. Modelo busca documentos relevantes e depois gera resposta baseada neles.

## S

**SentencePiece**
Outro algoritmo de tokenização similar a BPE.

**Soft Prompt**
Vetor de números que se comporta como um prompt implícito. Mais eficiente que escrever prompts longos.

**Softmax**
Função matemática que converte números em probabilidades que somam 1. Usada no output de classificadores.

**Sparse Transformer**
Variação de Transformer que não processa todos os pares de tokens (economia de memória).

## T

**Temperatura (Temperature)**
Parâmetro que controla criatividade vs. previsibilidade. Temperatura alta = mais criativo. Temperatura baixa = mais previsível.

**Token**
Unidade pequena de texto que o modelo processa. Pode ser uma palavra, parte de palavra, ou caractere.

**Tokenização (Tokenization)**
Processo de dividir texto em tokens.

**Top-K Sampling**
Técnica onde o modelo só considera as K palavras mais prováveis para o próximo token.

**Top-P Sampling**
Técnica onde o modelo considera palavras até acumular P probabilidade total.

**Transfer Learning**
Técnica onde você pega um modelo treinado para uma tarefa e o adapta para outra. Economiza muito tempo de treinamento.

**Transformer**
Arquitetura de rede neural proposta em 2017 ("Attention is All You Need"). Base de todos os LLMs modernos.

**Training**
Processo de ajustar parâmetros de um modelo usando dados. Oposto de inferência.

## U

**Underfitting**
Quando um modelo é muito simples e não consegue aprender padrões importantes nos dados.

**Unsupervised Learning**
Aprendizado onde não há labels corretos; o modelo encontra padrões por conta própria.

## V

**Validação (Validation)**
Processo de avaliar um modelo em dados que não foram usados no treinamento.

**Vector Database**
Banco de dados otimizado para armazenar e buscar vetores de alta dimensão (embeddings).

**Viterbi Algorithm**
Algoritmo para encontrar a sequência mais provável em modelos probabilísticos.

## W

**Weight Decay**
Técnica de regularização que penaliza parâmetros grandes. Previne overfitting.

**Weights**
Parâmetros principais de uma rede neural. Definem como inputs são transformados.

**Whisper**
Modelo de reconhecimento de fala da OpenAI. Transcreve áudio para texto.

## X

**X-Transformers**
Variação de Transformer que tenta adicionar mais capacidades ao mecanismo de atenção.

## Y

**Zero-Shot Learning**
Quando um modelo consegue fazer uma tarefa sem nenhum exemplo. Capacidade emergente de modelos grandes.

## Z

**Zone of Proximal Development (em contexto de IA)**
Conceito do psicólogo Vygotsky: tarefas que um sistema consegue fazer com ajuda. Relevante para entender capacidades de LLMs.

---

**Nota**: Este glossário está em evolução. Novos termos surgem constantemente no campo de IA Generativa!
