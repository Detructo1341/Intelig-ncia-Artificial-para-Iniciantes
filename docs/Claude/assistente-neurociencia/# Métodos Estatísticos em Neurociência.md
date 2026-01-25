# Métodos Estatísticos em Neurociência

## Estatística Frequentista

### Testes t e ANOVA
**Quando usar**: Comparação de médias entre grupos ou condições

**Pressupostos**:
- Normalidade da distribuição (especialmente importante para amostras pequenas, n < 30)
- Homogeneidade de variâncias (teste de Levene)
- Independência das observações

**ANOVA de medidas repetidas**:
- Adiciona pressuposto de esfericidade (teste de Mauchly)
- Correções de Greenhouse-Geisser ou Huynh-Feldt quando violado
- Cuidado com dados faltantes: podem violar pressupostos

**Armadilhas comuns**:
- Comparações múltiplas não corrigidas (inflar taxa de erro Tipo I)
- Ignorar violação de pressupostos sem usar alternativas não-paramétricas
- Interpretar p > 0.05 como "ausência de efeito" (ausência de evidência ≠ evidência de ausência)

### Regressão Linear e Múltipla
**Quando usar**: Modelar relações entre variáveis contínuas; identificar preditores

**Pressupostos adicionais**:
- Linearidade da relação
- Ausência de multicolinearidade (VIF < 10)
- Homocedasticidade dos resíduos
- Ausência de outliers influentes (distância de Cook)

**Interpretação**:
- Coeficientes padronizados (β) para comparar força relativa de preditores
- R² ajustado para modelos com múltiplos preditores
- Intervalos de confiança mais informativos que p-valores isolados

### Testes Não-Paramétricos
**Quando usar**: Violação de pressupostos paramétricos, dados ordinais, distribuições assimétricas

**Alternativas comuns**:
- Mann-Whitney U (alternativa ao teste t independente)
- Wilcoxon signed-rank (alternativa ao teste t pareado)
- Kruskal-Wallis (alternativa ao ANOVA one-way)
- Friedman (alternativa ao ANOVA de medidas repetidas)

**Limitações**:
- Menor poder estatístico que testes paramétricos (quando pressupostos são atendidos)
- Testam diferenças em ranks, não médias (interpretação diferente)

## Estatística Bayesiana

### Fundamentos
**Vantagens sobre abordagem frequentista**:
- Quantifica evidência a favor de hipótese nula (BF₀₁)
- Permite incorporar conhecimento prévio (priors informativos)
- Interpretação mais intuitiva (probabilidade de hipótese dados os dados)
- Não há problema de comparações múltiplas da mesma forma

**Fator de Bayes (BF₁₀)**:
- BF₁₀ > 3: Evidência moderada para H1
- BF₁₀ > 10: Evidência forte para H1
- BF₁₀ > 30: Evidência muito forte para H1
- BF₁₀ < 1/3: Evidência moderada para H0
- 1/3 < BF₁₀ < 3: Evidência inconclusiva

### Priors
**Priors não-informativos (default)**:
- Cauchy(0, r=0.707) para tamanhos de efeito (ANOVA, teste t)
- Úteis quando não há conhecimento prévio específico

**Priors informativos**:
- Incorporam conhecimento de estudos anteriores
- Devem ser justificados e reportados explicitamente
- Análise de sensibilidade: testar como resultados mudam com diferentes priors

### Estimação de Parâmetros
**Região de Credibilidade (Credible Interval)**:
- Interpretação direta: 95% CI = 95% de probabilidade de parâmetro estar naquele intervalo
- Diferente de intervalo de confiança frequentista (interpretação mais complexa)

**HDI (Highest Density Interval)**:
- Intervalo com maior densidade de probabilidade
- Preferível para distribuições assimétricas

## Modelos Mistos (Mixed-Effects Models)

### Quando usar
- Dados hierárquicos ou aninhados (ex: múltiplas medidas por participante)
- Dados longitudinais
- Estudos multi-site
- Tamanhos de amostra desiguais entre grupos/condições

### Estrutura
**Efeitos fixos**: Predizem média populacional
**Efeitos aleatórios**: Capturam variabilidade entre unidades (participantes, estímulos, locais)

**Random intercepts**: Permite que média basal varie entre unidades
**Random slopes**: Permite que efeitos de preditores variem entre unidades

### Especificação de Modelo
**Estrutura de covariância dos efeitos aleatórios**:
- Compound Symmetry: Correlações iguais entre medidas
- Unstructured: Sem restrições (mais flexível, mais parâmetros)
- Autoregressive (AR1): Correlação diminui com distância temporal
- Escolha baseada em AIC/BIC e plausibilidade teórica

**Comparação de modelos**:
- Likelihood Ratio Test (LRT) para modelos aninhados
- AIC/BIC para modelos não-aninhados
- Menor AIC/BIC indica melhor balanço ajuste-complexidade

### Armadilhas comuns
- Não incluir random slopes quando teoricamente necessário
- Overfit: Modelo muito complexo para dados disponíveis (convergence failures)
- Ignorar correlação temporal em dados longitudinais
- Não reportar estrutura completa de efeitos aleatórios

## Análises Multivariadas

### PCA (Principal Component Analysis)
**Objetivo**: Redução de dimensionalidade, identificar padrões de covariação

**Aplicações em neurociência**:
- Análise de dados de EEG/MEG (componentes espaciais ou temporais)
- Redução de baterias neuropsicológicas em construtos latentes
- Análise de conectividade funcional

**Interpretação**:
- Componentes principais são ortogonais (não correlacionados)
- Porcentagem de variância explicada por cada componente
- Loadings: correlação entre variáveis originais e componentes

**Limitações**:
- Assume relações lineares
- Componentes são combinações lineares, nem sempre interpretáveis
- Sensível a outliers e escala das variáveis (normalizar antes)

### ICA (Independent Component Analysis)
**Diferença de PCA**: Busca fontes estatisticamente independentes, não apenas ortogonais

**Aplicações principais**:
- Remoção de artefatos em EEG/fMRI (piscar, movimento)
- Identificação de redes de repouso (resting-state networks)
- Separação de sinais sobrepostos

### Análise Fatorial Confirmatória (CFA)
**Quando usar**: Testar se estrutura fatorial hipotética se ajusta aos dados

**Diferença de PCA/EFA**:
- Abordagem confirmatória (testa modelo específico)
- Distingue entre variância compartilhada e única
- Permite testar invariância entre grupos

**Índices de ajuste**:
- χ²: Sensível a tamanho de amostra
- CFI/TLI > 0.90 (preferencialmente > 0.95)
- RMSEA < 0.08 (preferencialmente < 0.06)
- SRMR < 0.08

## Correção para Comparações Múltiplas

### Problema
Aumenta probabilidade de erro Tipo I (falso positivo) à medida que número de testes aumenta
- α = 0.05 por teste
- Probabilidade de ao menos um falso positivo em 20 testes: 1 - (0.95)²⁰ ≈ 0.64

### Métodos de Correção

**Bonferroni**: α_ajustado = α / n_comparações
- Muito conservador
- Adequado quando testes são independentes
- Pode inflacionar erro Tipo II (perde poder)

**Holm-Bonferroni**: Versão sequencial menos conservadora
- Ordena p-valores, aplica correção sequencial
- Mantém controle de Family-Wise Error Rate (FWER)

**FDR (False Discovery Rate) - Benjamini-Hochberg**:
- Controla proporção de falsos positivos entre descobertas significativas
- Menos conservador que Bonferroni
- Apropriado para análises exploratórias (ex: whole-brain fMRI)

**Permutation tests**:
- Não assume distribuição específica
- Constrói distribuição nula empiricamente
- Computacionalmente intensivo, mas robusto

### Quando NÃO corrigir
- Análises exploratórias com justificativa clara
- Comparações planejadas a priori (planned contrasts)
- Análises bayesianas (tratam múltiplas comparações diferentemente)
- Replicação direta de efeito específico

## Modelagem Computacional Cognitiva

### Objetivo
Formalizar teorias cognitivas em modelos matemáticos e testar previsões quantitativas

### Procedimento Geral
1. **Especificar modelo**: Definir equações, parâmetros, predições
2. **Ajuste de parâmetros**: Maximizar verossimilhança ou posterior bayesiano
3. **Comparação de modelos**: Qual modelo descreve melhor os dados?
4. **Validação**: Generalização para novos dados/condições

### Comparação de Modelos

**AIC/BIC**: Penalizam complexidade (número de parâmetros livres)
- AIC = -2*ln(L) + 2k
- BIC = -2*ln(L) + k*ln(n)
- BIC penaliza mais fortemente modelos complexos

**Cross-validation**: Treinar em subset, testar em outro
- Leave-one-out: Treina em n-1, testa em 1 (repetido n vezes)
- K-fold: Divide dados em k partes

**Simulação**: Modelo consegue reproduzir padrões qualitativos dos dados?

### Armadilhas
- Overfitting: Modelo flexível demais, captura ruído
- Identificabilidade: Diferentes combinações de parâmetros produzem mesmas predições
- Interpretação de parâmetros: Nem sempre correspondem diretamente a construtos psicológicos

## Machine Learning em Neurociência

### Quando usar ML
- Classificação: Diagnóstico, predição de resposta a tratamento, decodificação de estados cerebrais
- Regressão: Predição de escores comportamentais, gravidade de sintomas
- Clustering: Identificar subtipos de pacientes, padrões de conectividade
- Redução de dimensionalidade: Visualizar estrutura de dados de alta dimensão

### Conceitos Fundamentais

**Overfitting vs. Underfitting**:
- Overfitting: Modelo muito complexo, performa bem em treino mas mal em teste
- Underfitting: Modelo muito simples, não captura padrões reais
- Viés-variância tradeoff: Equilíbrio entre simplicidade e flexibilidade

**Train-test split**:
- Nunca testar no mesmo conjunto usado para treino
- Típico: 70-80% treino, 20-30% teste
- Validação cruzada para amostras pequenas

**Feature selection**:
- Reduz dimensionalidade, melhora interpretabilidade
- Métodos: Filter (correlação, mutual information), Wrapper (recursive feature elimination), Embedded (LASSO)
- Risco: Feature selection no conjunto completo = data leakage

### Métricas de Avaliação

**Classificação**:
- Acurácia: Pode enganar em classes desbalanceadas
- Precisão, Recall, F1-score: Mais informativos
- ROC-AUC: Discriminação entre classes independente de threshold
- Matriz de confusão: Mostra padrão de erros

**Regressão**:
- RMSE: Penaliza erros grandes
- MAE: Menos sensível a outliers
- R²: Proporção de variância explicada

### Interpretabilidade
**Caixa-preta vs. interpretável**:
- SVM linear, regressão logística, árvores de decisão: Mais interpretáveis
- Deep learning, random forests: Mais complexos, melhor performance

**SHAP values**: Quantifica contribuição de cada feature para predição individual
**Feature importance**: Quais variáveis são mais preditivas globalmente?

### Armadilhas comuns
- Data leakage: Informação de teste vaza para treino (ex: normalização antes de split)
- Classes desbalanceadas: Acurácia de 95% pode ser trivial se classe majoritária é 95%
- Múltiplas comparações implícitas: Testar muitos algoritmos/hiperparâmetros
- Generalização: Modelo treinado em uma população pode não generalizar para outra

## Tamanho de Amostra e Poder Estatístico

### Conceitos
**Poder estatístico (1-β)**: Probabilidade de detectar efeito se ele existe
- Típico: 80% (β = 0.20)
- Determinado por: α, tamanho de efeito, tamanho de amostra, design

**Tamanho de efeito**:
- d de Cohen (diferença entre médias): pequeno (0.2), médio (0.5), grande (0.8)
- η² parcial (ANOVA): pequeno (0.01), médio (0.06), grande (0.14)
- r (correlação): pequeno (0.1), médio (0.3), grande (0.5)

### Cálculo de Amostra
**A priori**: Antes de coletar dados
- Input: α, poder desejado (1-β), tamanho de efeito esperado
- Output: n necessário

**Post-hoc (não recomendado)**: Calcular poder após coletar dados
- Não informa sobre qualidade do estudo já realizado
- p-valor já incorpora informação sobre poder
- Útil apenas para planejar replicações

### Considerações Práticas
- Estudos piloto para estimar tamanho de efeito (mas: estimativas instáveis)
- Meta-análises de literatura para estimativas mais precisas
- Planejar para efeitos menores do que esperado (proteger contra inflação de efeito)
- Estudos de neuroimagem frequentemente under-powered (amostras pequenas, múltiplas comparações)
