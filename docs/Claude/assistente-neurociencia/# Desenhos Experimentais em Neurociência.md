# Desenhos Experimentais em Neurociência

## Estudos Comportamentais

### Experimentos Laboratoriais Controlados
**Características**:
- Alto controle sobre variáveis
- Aleatorização de participantes e ordem de condições
- Manipulação experimental direta

**Desenhos comuns**:
- **Between-subjects**: Cada grupo recebe uma condição diferente
  - Vantagens: Evita efeitos de ordem, aprendizado
  - Desvantagens: Requer mais participantes, diferenças individuais entre grupos
  
- **Within-subjects (medidas repetidas)**: Mesmo participante em todas as condições
  - Vantagens: Maior poder estatístico, controla diferenças individuais
  - Desvantagens: Efeitos de ordem, fadiga, aprendizado
  - Soluções: Contrabalanceamento, intervalos entre sessões

- **Mixed design**: Combinação de fatores between e within
  - Exemplo: Grupo clínico vs. controle (between) x pré vs. pós-tratamento (within)

### Tarefas Cognitivas Clássicas
**Tempo de Reação (RT)**:
- Simples vs. escolha vs. go/no-go
- Paradigma de Stroop: Interferência, controle atencional
- Paradigma de flanker: Controle de conflito
- Simon task: Compatibilidade estímulo-resposta

**Memória**:
- Recall livre vs. com pistas vs. reconhecimento
- Working memory: N-back, span tasks
- Codificação vs. recuperação: Dissociar processos

**Atenção**:
- Busca visual: Detecção de alvos, efeito de set size
- Tarefa de Posner: Atenção espacial endógena vs. exógena
- Attentional blink: Limitações temporais

### Controles Experimentais Críticos
- **Baseline apropriado**: Condição controle que isola processo de interesse
- **Contrabalanceamento**: Ordem de condições, mapeamento estímulo-resposta
- **Catch trials**: Detectar participantes desatentos ou não-complacentes
- **Prática**: Reduzir efeitos de aprendizado, estabilizar performance

## Estudos Neuropsicológicos

### Estudos de Lesão
**Lógica**: Dano em região X causa déficit em função Y → Região X é necessária para função Y

**Tipos de lesão**:
- Acidente vascular cerebral (AVC): Mais comum, heterogeneidade anatômica
- Trauma crânio-encefálico (TCE): Difuso, frontal/temporal mais vulneráveis
- Neurocirurgia: Remoção controlada (epilepsia, tumor)
- Degeneração focal: Variante comportamental de demência frontotemporal

**Análise de dissociações**:
- **Dissociação simples**: Lesão em X prejudica tarefa A, mas não tarefa B
  - Problema: Pode ser diferença de sensibilidade das tarefas
- **Dupla dissociação**: Lesão em X prejudica A (não B); Lesão em Y prejudica B (não A)
  - Mais forte: Evidencia independência de sistemas

**Limitações**:
- Raramente lesões são focais (afetam conexões)
- Plasticidade e reorganização cerebral
- Tempo desde lesão: Agudo vs. crônico
- Viés de amostra: Lesões em certas regiões são mais letais

### Estudos de Caso Único
**Quando usar**: Déficits raros, perfis neuropsicológicos únicos

**Abordagem**:
- Descrição detalhada e multifacetada
- Comparação com normativas (z-scores)
- Comparação com grupo controle pareado
- Análise de padrão: Perfil de preservado vs. prejudicado

**Critério de anormalidade**:
- Déficit: Escore < percentil 5 ou z < -1.65
- Dissociação: Diferença significativa entre tarefas (modified t-test)

**Limitações**:
- Generalização limitada (n=1)
- Deve ser complementado por estudos de grupo

### Baterias de Avaliação Neuropsicológica
**Domínios cognitivos**:
- Atenção e velocidade de processamento
- Memória (verbal, visual, trabalho)
- Linguagem (compreensão, produção, nomeação)
- Funções executivas (flexibilidade, inibição, planejamento)
- Habilidades visuoespaciais e visuoconstrutivas
- Cognição social (teoria da mente, reconhecimento de emoções)

**Instrumentos padronizados**:
- WAIS/WISC: QI e índices cognitivos
- WMS: Memória
- Stroop, TMT, Wisconsin Card Sorting: Executivas
- Boston Naming Test: Linguagem
- Rey-Osterrieth Complex Figure: Visuoespacial

**Interpretação**:
- Comparação com normas estratificadas (idade, escolaridade)
- Análise de padrão entre domínios
- Considerar esforço e motivação (testes de validade)

## Estudos Eletrofisiológicos (EEG/ERP)

### Desenho de ERP (Event-Related Potentials)
**Princípios básicos**:
- Promediar múltiplas tentativas para aumentar razão sinal-ruído
- Mínimo 20-30 trials por condição (ideal: 50+)
- Intervalos inter-estímulos (ISI) adequados: Evitar sobreposição

**Paradigmas clássicos**:
- **Oddball**: Estímulos frequentes vs. raros
  - P300: Detecção de alvo, atualização de contexto (~300ms)
- **Go/No-go**: Inibição de resposta
  - N2: Detecção de conflito (~200-300ms)
  - P3: Inibição motora
- **MMN (Mismatch Negativity)**: Detecção automática de mudança (~100-200ms)
  - Não requer atenção consciente
- **N400**: Incongruência semântica (~400ms)
- **ERN (Error-Related Negativity)**: Monitoramento de erros (~50ms pós-erro)

**Componentes ERP**:
- **Latência**: Tempo de pico (ms) - Quando processo ocorre
- **Amplitude**: Magnitude (μV) - Intensidade do processo
- **Topografia**: Distribuição no escalpo - Localização aproximada de fontes

**Análise de componentes**:
- Definir janela temporal e eletrodos a priori (evitar cherry-picking)
- Peak amplitude vs. mean amplitude (mais robusta)
- Analisar latência e amplitude separadamente
- Diferenças de onda (ex: N400 = incongruente - congruente)

### Análise Tempo-Frequência
**Quando usar**: Processos que envolvem sincronização neural, oscilações

**Bandas de frequência**:
- Delta (0.5-4 Hz): Sono profundo, processos atencionais
- Theta (4-8 Hz): Memória de trabalho, navegação espacial
- Alpha (8-13 Hz): Inibição cortical, estado de repouso
- Beta (13-30 Hz): Controle motor, manutenção de estado
- Gamma (30-100 Hz): Integração de informação, atenção

**Medidas**:
- **Potência**: Amplitude da oscilação em banda específica
- **Coerência/Sincronização**: Comunicação entre regiões
- **Event-Related Synchronization/Desynchronization (ERS/ERD)**

**Análise**:
- Baseline correction: Período pré-estímulo
- Morlet wavelets ou filtros para decompor sinal
- Comparar condições ou grupos

### Limitações e Considerações
**Temporal**:
- Excelente resolução temporal (milissegundos)
- Pode dissociar processos temporalmente próximos

**Espacial**:
- Baixa resolução espacial (problema inverso)
- Source localization: Estimativa computacional de fontes corticais (requer IRM)
- Topografia: Informação aproximada, não localização precisa

**Artefatos**:
- Movimento ocular: ICA para remoção
- Movimento muscular: Filtros, rejeição de trials
- Artefatos de linha elétrica (50/60 Hz): Filtros notch

## Estudos de Neuroimagem Funcional (fMRI)

### Desenho de fMRI
**Considerações hemodinâmicas**:
- Sinal BOLD reflete atividade neural indiretamente (via fluxo sanguíneo)
- Resposta hemodinâmica demora ~5-6 segundos para pico
- Baixa resolução temporal (2-3 segundos por volume)

**Desenhos de bloco**:
- Blocos alternados de condições (15-30s cada)
- Vantagens: Maior poder estatístico, mais robusto
- Desvantagens: Não permite dissociar eventos individuais, efeitos de antecipação

**Desenhos relacionados a eventos (event-related)**:
- Eventos breves espaçados temporalmente
- Vantagens: Permite dissociar tipos de trials, modelar erros
- Desvantagens: Menor poder estatístico, requer mais trials
- ITI (inter-trial interval) variável (jittering): Aumenta eficiência

**Desenhos mistos**:
- Combina blocos e eventos
- Exemplo: Blocos de tarefa, analisar trials corretos vs. errados

### Análises de fMRI
**Whole-brain vs. ROI**:
- **Whole-brain**: Exploratória, identifica regiões não previstas
  - Correção para comparações múltiplas (FWE, FDR, cluster-based)
- **ROI (Region of Interest)**: Hipótese-dirigida, maior sensibilidade
  - Definir ROI a priori (anatomicamente ou funcionalmente)

**Análise de primeira ordem (single-subject)**:
- GLM (General Linear Model): Modela resposta BOLD esperada
- Contraste entre condições: A > B, A > baseline

**Análise de segunda ordem (group-level)**:
- One-sample t-test: Ativação consistente no grupo
- Two-sample t-test: Diferença entre grupos
- ANOVA: Múltiplos grupos ou condições
- Regressão: Correlação com variável contínua (ex: idade, escore comportamental)

**Conectividade funcional**:
- **Seed-based**: Correlação temporal entre ROI seed e resto do cérebro
- **ICA**: Identificar redes funcionais (resting-state networks)
- **Análise de grafos**: Medidas de hub, modularidade, eficiência
- **Dynamic connectivity**: Variabilidade temporal de conectividade

### Considerações Práticas
**Movimento de cabeça**:
- Principal fonte de artefato
- Realinhamento durante pré-processamento
- Regressores de movimento no GLM
- Scrubbing: Remover volumes com movimento excessivo

**Normalização espacial**:
- Alinhamento a template padrão (MNI, Talairach)
- Permite comparação entre participantes

**Suavização espacial (smoothing)**:
- Filtro gaussiano (FWHM 6-8mm típico)
- Aumenta SNR, facilita normalização
- Reduz resolução espacial

## Estimulação Cerebral Não-Invasiva

### TMS (Transcranial Magnetic Stimulation)
**Lógica**: Pulso magnético induz corrente elétrica, despolariza neurônios

**Aplicações**:
- **Single-pulse**: Disrupção temporal focal (virtual lesion)
  - Timing: Quando região é crítica para tarefa?
- **Repetitive TMS (rTMS)**: Modulação prolongada de excitabilidade
  - Alta frequência (>5 Hz): Facilitação
  - Baixa frequência (1 Hz): Inibição
- **Paired-pulse**: Investigar mecanismos de inibição/facilitação

**Desenho experimental**:
- Controle sham: Bobina rotacionada ou afastada
- Localização guiada por neuronavegação (com IRM individual)
- Testar múltiplos sites: Especificidade anatômica
- Testar múltiplos timings: Especificidade temporal

**Limitações**:
- Penetração limitada (~2-3cm): Regiões superficiais
- Afeta rede conectada, não apenas local estimulado
- Desconforto (sensação de batida, contração muscular)
- Contraindicações (epilepsia, implantes metálicos)

### tDCS (Transcranial Direct Current Stimulation)
**Lógica**: Corrente contínua modula potencial de membrana (não induz potencial de ação)

**Polaridade**:
- Anodal: Aumenta excitabilidade
- Catodal: Diminui excitabilidade

**Parâmetros**:
- Corrente: 1-2 mA típico
- Duração: 10-30 minutos
- Tamanho e posicionamento de eletrodos: Define distribuição de corrente

**Desenho experimental**:
- Controle sham: Rampa curta de corrente inicial
- Online vs. offline: Durante vs. após estimulação
- Efeitos podem durar horas após estimulação

**Limitações**:
- Baixa resolução espacial (distribuição ampla)
- Alta variabilidade inter-individual
- Mecanismos neurais não completamente compreendidos
- Difícil replicação

## Estudos Clínicos e de Intervenção

### Ensaios Clínicos Randomizados (RCT)
**Padrão ouro** para testar eficácia de intervenções

**Componentes**:
- Aleatorização: Minimiza vieses de seleção
- Controle: Grupo sem intervenção ou tratamento padrão
- Cegamento: Single-blind (participante) ou double-blind (participante + avaliador)

**Desenhos**:
- **Parallel-group**: Grupos independentes, cada um recebe uma condição
- **Crossover**: Cada participante recebe ambas as condições (com washout entre)
  - Vantagens: Maior poder, controla diferenças individuais
  - Limitações: Efeitos de ordem, carry-over

**Medidas de desfecho**:
- **Primária**: Objetivo principal (ex: redução de sintomas)
- **Secundária**: Objetivos adicionais (qualidade de vida, efeitos adversos)
- **Subjetiva** (auto-relato) vs. **objetiva** (performance, biomarcadores)

### Estudos Longitudinais
**Objetivo**: Examinar mudanças ao longo do tempo, trajetórias de desenvolvimento/declínio

**Desenhos**:
- **Prospectivo**: Acompanha mesma coorte ao longo do tempo
  - Vantagens: Mudança intra-individual, sequência temporal
  - Limitações: Custoso, atrito (dropout), efeitos de prática
- **Retrospectivo**: Reconstrói história a partir de registros
- **Acelerado**: Múltiplas coortes de diferentes idades, sobreposição

**Análise**:
- Curvas de crescimento (growth curve modeling)
- Modelos mistos para dados longitudinais
- Trajetórias individuais vs. grupo

**Ameaças à validade**:
- Atrito não-aleatório: Quem abandona estudo?
- Efeitos de prática: Aprendizado das tarefas
- Efeitos de coorte: Gerações diferentes

### Estudos de Caso-Controle
**Desenho retrospectivo**: Compara grupo com condição (casos) vs. sem condição (controles)

**Quando usar**:
- Condições raras
- Doenças com longa latência
- Estudos exploratórios ou pilotos

**Pareamento**:
- Casos e controles pareados por variáveis confundidoras (idade, sexo, educação)
- Pareamento um-para-um ou um-para-muitos

**Limitações**:
- Viés de seleção (quem é selecionado como controle?)
- Viés de recall (diferenças na memória de eventos passados)
- Não estabelece causalidade (apenas associação)

## Estudos de fNIRS (Functional Near-Infrared Spectroscopy)

### Princípios
- Mede oxigenação cerebral via absorção de luz infravermelha
- Resolução temporal intermediária (~100ms)
- Resolução espacial limitada (~1cm)
- Penetração ~2-3cm (córtex superficial)

### Vantagens
- Portabilidade: Ambulatório, hiperescaneamento (dois participantes simultaneamente)
- Menos sensível a movimento que fMRI
- Tolerável para crianças e populações clínicas
- Custo menor que fMRI

### Limitações
- Alcance limitado (regiões superficiais: frontal, parietal, temporal)
- Sinal contaminado por hemodinâmica extracraniana (couro cabeludo)
- Menor SNR que fMRI

### Aplicações
- Estudos de interação social naturalística
- Estudos de desenvolvimento infantil
- Monitoramento durante reabilitação

## Modelagem Computacional e Simulações

### Quando usar
- Testar previsões quantitativas de teorias
- Explorar espaço de parâmetros além do empiricamente acessível
- Integrar múltiplos níveis de análise (neurônios → redes → comportamento)

### Tipos de Modelos
**Modelos de decisão**: DDM (Drift Diffusion Model), LCA
- Explicam tempo de reação e precisão
- Parâmetros: Drift rate (qualidade de informação), threshold (speed-accuracy tradeoff), non-decision time

**Modelos de aprendizado por reforço**:
- Q-learning, actor-critic, model-based vs. model-free
- Parâmetros: Taxa de aprendizado, desconto temporal, temperatura (exploração vs. exploração)

**Modelos de rede neural**:
- Simulam populações de neurônios, conectividade
- Exploram como propriedades emergentes surgem de interações

### Análise de Modelos
**Model recovery**: Simular dados com modelo conhecido, recuperar parâmetros
- Testa se método de ajuste funciona

**Parameter recovery**: Recuperar parâmetros verdadeiros de dados simulados
- Avalia identifiability e confiabilidade de estimativas

**Model comparison**: BIC, AIC, cross-validation
- Qual modelo explica melhor padrão de dados?

## Considerações Gerais de Desenho

### Validade Interna
- Controle de variáveis confundidoras
- Aleatorização adequada
- Manipulação experimental clara
- Medidas confiáveis e sensíveis

### Validade Externa
- Generalização para outras populações
- Generalização para contextos fora do laboratório
- Validade ecológica: Quão naturalístico é o paradigma?

### Trade-offs Comuns
- Controle experimental vs. validade ecológica
- Simplicidade (interpretabilidade) vs. realismo
- Número de condições vs. número de trials por condição
- Profundidade (poucos participantes, muitas medidas) vs. amplitude (muitos participantes, poucas medidas)

### Replicabilidade e Pré-registro
- Especificar hipóteses, métodos e análises a priori
- Distinguir análises confirmatórias (pré-registradas) de exploratórias
- Compartilhar dados, código, materiais (Open Science)
