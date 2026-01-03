import React, { useState, useEffect } from 'react';
import { Brain, Zap, Heart, MessageSquare, TrendingUp, AlertCircle, Check, X, Sparkles, Activity, Eye, ChevronRight, Target, Shield, Lightbulb } from 'lucide-react';

const IAHealthExplorer = () => {
  const [activeSection, setActiveSection] = useState('home');
  const [sentimentText, setSentimentText] = useState('');
  const [sentimentResult, setSentimentResult] = useState(null);
  const [quizScore, setQuizScore] = useState(0);
  const [quizAnswered, setQuizAnswered] = useState({});
  const [animateIn, setAnimateIn] = useState(false);

  useEffect(() => {
    setAnimateIn(true);
  }, []);

  // Análise de sentimento simulada baseada na skill
  const analyzeSentiment = (text) => {
    if (!text.trim()) return;

    const negativeWords = ['nunca', 'nada', 'não aguento', 'fracasso', 'terrível', 'ansiedade', 'deprimido', 'triste', 'desespero', 'sozinho'];
    const positiveWords = ['feliz', 'alegre', 'otimista', 'esperança', 'motivado', 'bem', 'consegui', 'sucesso'];
    const absoluteWords = ['sempre', 'nunca', 'tudo', 'nada', 'total', 'completamente'];
    const firstPerson = (text.match(/\b(eu|meu|minha|comigo)\b/gi) || []).length;

    let sentiment = 'Neutro';
    let intensity = 0;
    let distortions = [];
    
    const lowerText = text.toLowerCase();
    const negCount = negativeWords.filter(word => lowerText.includes(word)).length;
    const posCount = positiveWords.filter(word => lowerText.includes(word)).length;
    const absCount = absoluteWords.filter(word => lowerText.includes(word)).length;

    if (negCount > posCount) {
      sentiment = 'Negativo';
      intensity = Math.min(95, 60 + negCount * 10);
    } else if (posCount > negCount) {
      sentiment = 'Positivo';
      intensity = Math.min(95, 60 + posCount * 10);
    } else {
      sentiment = 'Neutro';
      intensity = 50;
    }

    if (absCount > 0) {
      distortions.push({
        name: 'Pensamento Dicotômico',
        confidence: Math.min(90, 60 + absCount * 15),
        description: 'Uso de palavras absolutas como "sempre", "nunca", "tudo" ou "nada"'
      });
    }

    if (lowerText.includes('vai ser') || lowerText.includes('será') || lowerText.includes('acabou')) {
      distortions.push({
        name: 'Catastrofização',
        confidence: 85,
        description: 'Previsão de cenários catastróficos sem base em evidências'
      });
    }

    if (firstPerson > 3) {
      distortions.push({
        name: 'Foco Excessivo no Eu',
        confidence: 70,
        description: 'Uso elevado de pronomes em primeira pessoa, possível indicador de ruminação'
      });
    }

    setSentimentResult({
      sentiment,
      intensity,
      distortions,
      wordCount: text.split(/\s+/).length,
      analysis: sentiment === 'Negativo' && intensity > 70 ? 
        'Alto indicador de sofrimento emocional. Considere buscar apoio profissional.' :
        'Análise concluída. Lembre-se: esta é apenas uma demonstração educativa.'
    });
  };

  const quizQuestions = [
    {
      id: 1,
      question: 'Qual é a principal vantagem do uso de IA em saúde mental?',
      options: [
        'Substituir completamente terapeutas humanos',
        'Monitoramento contínuo e detecção precoce de crises',
        'Eliminar a necessidade de medicamentos',
        'Tornar a terapia mais cara'
      ],
      correct: 1
    },
    {
      id: 2,
      question: 'O que é NLP (Processamento de Linguagem Natural)?',
      options: [
        'Um tipo de terapia comportamental',
        'Tecnologia que analisa texto/fala para detectar padrões emocionais',
        'Um medicamento para ansiedade',
        'Uma técnica de meditação'
      ],
      correct: 1
    },
    {
      id: 3,
      question: 'Qual é uma limitação crítica dos chatbots terapêuticos?',
      options: [
        'São muito caros',
        'Funcionam apenas em inglês',
        'Não substituem terapeutas humanos e têm dificuldade com nuances',
        'Requerem internet de alta velocidade'
      ],
      correct: 2
    },
    {
      id: 4,
      question: 'Wearables podem detectar sinais de transtornos mentais através de:',
      options: [
        'Análise de DNA',
        'Leitura de pensamentos',
        'Padrões de sono, frequência cardíaca e atividade física',
        'Raios-X do cérebro'
      ],
      correct: 2
    }
  ];

  const handleQuizAnswer = (questionId, selectedOption) => {
    const question = quizQuestions.find(q => q.id === questionId);
    const isCorrect = selectedOption === question.correct;
    
    setQuizAnswered(prev => ({
      ...prev,
      [questionId]: { selected: selectedOption, correct: isCorrect }
    }));

    if (isCorrect && !quizAnswered[questionId]) {
      setQuizScore(prev => prev + 1);
    }
  };

  const applications = [
    {
      icon: MessageSquare,
      title: 'Chatbots Terapêuticos',
      description: 'Woebot, Wysa e outros usam TCC programada e LLMs para suporte 24/7',
      color: 'from-cyan-500 to-blue-600'
    },
    {
      icon: AlertCircle,
      title: 'Detecção de Crises',
      description: 'Algoritmos monitoram redes sociais e apps para identificar sinais de risco',
      color: 'from-rose-500 to-pink-600'
    },
    {
      icon: Target,
      title: 'Personalização de Tratamento',
      description: 'IA prediz qual medicamento terá melhor resposta para cada paciente',
      color: 'from-purple-500 to-indigo-600'
    },
    {
      icon: Activity,
      title: 'Análise de Sessões',
      description: 'Transcrição automática e análise de aliança terapêutica em tempo real',
      color: 'from-emerald-500 to-teal-600'
    }
  ];

  const technologies = [
    { name: 'NLP', description: 'Análise de linguagem', progress: 90 },
    { name: 'Machine Learning', description: 'Predição de padrões', progress: 85 },
    { name: 'Deep Learning', description: 'Redes neurais complexas', progress: 75 },
    { name: 'Wearables', description: 'Monitoramento fisiológico', progress: 70 },
    { name: 'LLMs', description: 'Modelos de linguagem', progress: 80 }
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-950 via-indigo-950 to-purple-950 text-white overflow-hidden">
      {/* Background Effects */}
      <div className="fixed inset-0 opacity-30">
        <div className="absolute top-20 left-20 w-96 h-96 bg-cyan-500 rounded-full filter blur-3xl animate-pulse"></div>
        <div className="absolute bottom-20 right-20 w-96 h-96 bg-purple-500 rounded-full filter blur-3xl animate-pulse" style={{ animationDelay: '1s' }}></div>
        <div className="absolute top-1/2 left-1/2 w-96 h-96 bg-pink-500 rounded-full filter blur-3xl animate-pulse" style={{ animationDelay: '2s' }}></div>
      </div>

      {/* Header */}
      <header className="relative z-10 border-b border-white/10 backdrop-blur-xl bg-black/20">
        <div className="max-w-7xl mx-auto px-6 py-6">
          <div className="flex items-center justify-between">
            <div className={`flex items-center gap-4 transition-all duration-1000 ${animateIn ? 'translate-x-0 opacity-100' : '-translate-x-20 opacity-0'}`}>
              <div className="relative">
                <Brain className="w-12 h-12 text-cyan-400" strokeWidth={1.5} />
                <Zap className="w-6 h-6 text-yellow-400 absolute -top-1 -right-1 animate-pulse" />
              </div>
              <div>
                <h1 className="text-3xl font-bold bg-gradient-to-r from-cyan-400 via-purple-400 to-pink-400 bg-clip-text text-transparent">
                  IA & Saúde Mental
                </h1>
                <p className="text-sm text-cyan-300/60 font-light tracking-wider">EXPLORADOR INTERATIVO</p>
              </div>
            </div>
            <nav className="flex gap-2">
              {[
                { id: 'home', label: 'Início', icon: Brain },
                { id: 'sentiment', label: 'Análise', icon: Heart },
                { id: 'quiz', label: 'Quiz', icon: Lightbulb }
              ].map(({ id, label, icon: Icon }, idx) => (
                <button
                  key={id}
                  onClick={() => setActiveSection(id)}
                  className={`px-6 py-2 rounded-full flex items-center gap-2 transition-all duration-300 ${
                    activeSection === id
                      ? 'bg-gradient-to-r from-cyan-500 to-purple-600 shadow-lg shadow-cyan-500/50'
                      : 'bg-white/5 hover:bg-white/10'
                  }`}
                  style={{ animationDelay: `${idx * 100}ms` }}
                >
                  <Icon className="w-4 h-4" />
                  <span className="text-sm font-medium">{label}</span>
                </button>
              ))}
            </nav>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="relative z-10 max-w-7xl mx-auto px-6 py-12">
        {activeSection === 'home' && (
          <div className="space-y-16">
            {/* Hero Section */}
            <section className={`text-center space-y-6 transition-all duration-1000 ${animateIn ? 'translate-y-0 opacity-100' : 'translate-y-10 opacity-0'}`}>
              <div className="inline-flex items-center gap-2 px-4 py-2 bg-cyan-500/10 border border-cyan-500/30 rounded-full text-cyan-300 text-sm mb-4">
                <Sparkles className="w-4 h-4" />
                <span>Baseado na skill "ia-saude-mental"</span>
              </div>
              <h2 className="text-6xl font-bold bg-gradient-to-r from-white via-cyan-200 to-purple-200 bg-clip-text text-transparent leading-tight">
                A Revolução da IA na<br />Psicologia e Psiquiatria
              </h2>
              <p className="text-xl text-cyan-100/60 max-w-3xl mx-auto leading-relaxed">
                Explore como a Inteligência Artificial está transformando diagnóstico, tratamento e pesquisa em saúde mental
              </p>
            </section>

            {/* Applications Grid */}
            <section className="space-y-8">
              <div className="flex items-center gap-3">
                <div className="h-px flex-1 bg-gradient-to-r from-transparent via-cyan-500/50 to-transparent"></div>
                <h3 className="text-2xl font-bold text-cyan-300 flex items-center gap-2">
                  <Target className="w-6 h-6" />
                  Principais Aplicações
                </h3>
                <div className="h-px flex-1 bg-gradient-to-r from-transparent via-cyan-500/50 to-transparent"></div>
              </div>
              
              <div className="grid md:grid-cols-2 gap-6">
                {applications.map((app, idx) => {
                  const Icon = app.icon;
                  return (
                    <div
                      key={idx}
                      className="group relative bg-gradient-to-br from-white/5 to-white/0 backdrop-blur-sm border border-white/10 rounded-2xl p-8 hover:border-cyan-500/50 transition-all duration-500 hover:scale-105 hover:shadow-2xl hover:shadow-cyan-500/20 overflow-hidden"
                      style={{ animationDelay: `${idx * 150}ms` }}
                    >
                      <div className={`absolute inset-0 bg-gradient-to-br ${app.color} opacity-0 group-hover:opacity-10 transition-opacity duration-500`}></div>
                      <div className="relative z-10">
                        <div className={`w-16 h-16 rounded-2xl bg-gradient-to-br ${app.color} flex items-center justify-center mb-4 group-hover:scale-110 transition-transform duration-300`}>
                          <Icon className="w-8 h-8 text-white" />
                        </div>
                        <h4 className="text-xl font-bold mb-3 text-white">{app.title}</h4>
                        <p className="text-cyan-100/60 leading-relaxed">{app.description}</p>
                      </div>
                    </div>
                  );
                })}
              </div>
            </section>

            {/* Technologies Progress */}
            <section className="space-y-8">
              <div className="flex items-center gap-3">
                <div className="h-px flex-1 bg-gradient-to-r from-transparent via-purple-500/50 to-transparent"></div>
                <h3 className="text-2xl font-bold text-purple-300 flex items-center gap-2">
                  <Zap className="w-6 h-6" />
                  Tecnologias Fundamentais
                </h3>
                <div className="h-px flex-1 bg-gradient-to-r from-transparent via-purple-500/50 to-transparent"></div>
              </div>

              <div className="bg-gradient-to-br from-white/5 to-white/0 backdrop-blur-sm border border-white/10 rounded-2xl p-8 space-y-6">
                {technologies.map((tech, idx) => (
                  <div key={idx} className="space-y-3">
                    <div className="flex items-center justify-between">
                      <div>
                        <span className="text-lg font-semibold text-white">{tech.name}</span>
                        <span className="text-sm text-cyan-300/60 ml-3">{tech.description}</span>
                      </div>
                      <span className="text-cyan-400 font-bold">{tech.progress}%</span>
                    </div>
                    <div className="h-3 bg-white/5 rounded-full overflow-hidden">
                      <div
                        className="h-full bg-gradient-to-r from-cyan-500 to-purple-600 rounded-full transition-all duration-1000 ease-out"
                        style={{
                          width: animateIn ? `${tech.progress}%` : '0%',
                          transitionDelay: `${idx * 200}ms`
                        }}
                      ></div>
                    </div>
                  </div>
                ))}
              </div>
            </section>

            {/* Ethics Warning */}
            <section className="bg-gradient-to-br from-amber-500/10 to-orange-500/10 border border-amber-500/30 rounded-2xl p-8">
              <div className="flex items-start gap-4">
                <Shield className="w-8 h-8 text-amber-400 flex-shrink-0 mt-1" />
                <div>
                  <h4 className="text-xl font-bold text-amber-300 mb-3">Considerações Éticas Críticas</h4>
                  <ul className="space-y-2 text-amber-100/80">
                    <li className="flex items-start gap-2">
                      <ChevronRight className="w-5 h-5 flex-shrink-0 mt-0.5 text-amber-400" />
                      <span><strong>Viés Algorítmico:</strong> Modelos treinados com populações WEIRD podem falhar em contextos culturais diversos</span>
                    </li>
                    <li className="flex items-start gap-2">
                      <ChevronRight className="w-5 h-5 flex-shrink-0 mt-0.5 text-amber-400" />
                      <span><strong>Privacidade:</strong> Dados de saúde mental são extremamente sensíveis e requerem proteção máxima</span>
                    </li>
                    <li className="flex items-start gap-2">
                      <ChevronRight className="w-5 h-5 flex-shrink-0 mt-0.5 text-amber-400" />
                      <span><strong>Deshumanização:</strong> IA não substitui empatia humana genuína - manter "human in the loop"</span>
                    </li>
                  </ul>
                </div>
              </div>
            </section>
          </div>
        )}

        {activeSection === 'sentiment' && (
          <div className="space-y-8">
            <div className="text-center space-y-4 mb-12">
              <h2 className="text-5xl font-bold bg-gradient-to-r from-cyan-300 to-purple-300 bg-clip-text text-transparent">
                Análise de Sentimento
              </h2>
              <p className="text-lg text-cyan-100/60 max-w-2xl mx-auto">
                Simulador educativo de como IA detecta padrões emocionais e distorções cognitivas
              </p>
            </div>

            <div className="max-w-4xl mx-auto space-y-8">
              {/* Input */}
              <div className="bg-gradient-to-br from-white/5 to-white/0 backdrop-blur-sm border border-white/10 rounded-2xl p-8">
                <label className="block text-lg font-semibold text-cyan-300 mb-4">
                  Digite um texto para análise:
                </label>
                <textarea
                  value={sentimentText}
                  onChange={(e) => setSentimentText(e.target.value)}
                  placeholder="Exemplo: Nunca consigo fazer nada direito. Sou um fracasso total..."
                  className="w-full h-40 bg-white/5 border border-cyan-500/30 rounded-xl p-4 text-white placeholder-cyan-300/30 focus:outline-none focus:border-cyan-500 transition-colors"
                />
                <button
                  onClick={() => analyzeSentiment(sentimentText)}
                  disabled={!sentimentText.trim()}
                  className="mt-4 px-8 py-3 bg-gradient-to-r from-cyan-500 to-purple-600 rounded-xl font-semibold hover:shadow-lg hover:shadow-cyan-500/50 transition-all disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
                >
                  <Eye className="w-5 h-5" />
                  Analisar Texto
                </button>
              </div>

              {/* Results */}
              {sentimentResult && (
                <div className="space-y-6 animate-in">
                  {/* Sentiment Score */}
                  <div className="bg-gradient-to-br from-white/5 to-white/0 backdrop-blur-sm border border-white/10 rounded-2xl p-8">
                    <h3 className="text-2xl font-bold text-cyan-300 mb-6">Resultado da Análise</h3>
                    
                    <div className="grid md:grid-cols-3 gap-6 mb-6">
                      <div className="text-center">
                        <div className="text-sm text-cyan-300/60 mb-2">Sentimento Detectado</div>
                        <div className={`text-3xl font-bold ${
                          sentimentResult.sentiment === 'Positivo' ? 'text-emerald-400' :
                          sentimentResult.sentiment === 'Negativo' ? 'text-rose-400' :
                          'text-amber-400'
                        }`}>
                          {sentimentResult.sentiment}
                        </div>
                      </div>
                      <div className="text-center">
                        <div className="text-sm text-cyan-300/60 mb-2">Intensidade</div>
                        <div className="text-3xl font-bold text-purple-400">{sentimentResult.intensity}%</div>
                      </div>
                      <div className="text-center">
                        <div className="text-sm text-cyan-300/60 mb-2">Palavras Analisadas</div>
                        <div className="text-3xl font-bold text-cyan-400">{sentimentResult.wordCount}</div>
                      </div>
                    </div>

                    <div className="h-4 bg-white/5 rounded-full overflow-hidden">
                      <div
                        className={`h-full rounded-full transition-all duration-1000 ${
                          sentimentResult.sentiment === 'Positivo' ? 'bg-gradient-to-r from-emerald-500 to-teal-500' :
                          sentimentResult.sentiment === 'Negativo' ? 'bg-gradient-to-r from-rose-500 to-pink-600' :
                          'bg-gradient-to-r from-amber-500 to-orange-500'
                        }`}
                        style={{ width: `${sentimentResult.intensity}%` }}
                      ></div>
                    </div>

                    <div className="mt-6 p-4 bg-cyan-500/10 border border-cyan-500/30 rounded-xl">
                      <p className="text-cyan-100/80">{sentimentResult.analysis}</p>
                    </div>
                  </div>

                  {/* Cognitive Distortions */}
                  {sentimentResult.distortions.length > 0 && (
                    <div className="bg-gradient-to-br from-white/5 to-white/0 backdrop-blur-sm border border-white/10 rounded-2xl p-8">
                      <h3 className="text-2xl font-bold text-purple-300 mb-6">Distorções Cognitivas Detectadas</h3>
                      <div className="space-y-4">
                        {sentimentResult.distortions.map((distortion, idx) => (
                          <div key={idx} className="bg-white/5 border border-purple-500/30 rounded-xl p-6">
                            <div className="flex items-start justify-between mb-3">
                              <h4 className="text-lg font-semibold text-white">{distortion.name}</h4>
                              <span className="px-3 py-1 bg-purple-500/20 text-purple-300 rounded-full text-sm font-bold">
                                {distortion.confidence}%
                              </span>
                            </div>
                            <p className="text-purple-100/60">{distortion.description}</p>
                          </div>
                        ))}
                      </div>
                      <div className="mt-6 p-4 bg-purple-500/10 border border-purple-500/30 rounded-xl">
                        <p className="text-sm text-purple-100/80">
                          💡 <strong>Nota Educativa:</strong> A detecção de distorções cognitivas é uma aplicação real de NLP em TCC digital. 
                          Chatbots terapêuticos usam esta técnica para identificar padrões de pensamento e sugerir reestruturação cognitiva.
                        </p>
                      </div>
                    </div>
                  )}
                </div>
              )}

              {/* Example Cases */}
              <div className="bg-gradient-to-br from-white/5 to-white/0 backdrop-blur-sm border border-white/10 rounded-2xl p-8">
                <h3 className="text-xl font-bold text-cyan-300 mb-4">Exemplos para Testar:</h3>
                <div className="space-y-3">
                  {[
                    'Estou muito feliz com meu progresso na terapia. Consegui enfrentar meus medos!',
                    'Nunca consigo fazer nada direito. Sou um fracasso total.',
                    'Se eu errar essa apresentação, minha carreira acabou completamente.',
                    'Não aguento mais essa ansiedade constante. Quero sumir.'
                  ].map((example, idx) => (
                    <button
                      key={idx}
                      onClick={() => setSentimentText(example)}
                      className="w-full text-left p-4 bg-white/5 border border-cyan-500/20 rounded-lg hover:border-cyan-500/50 hover:bg-white/10 transition-all text-sm text-cyan-100/80"
                    >
                      "{example}"
                    </button>
                  ))}
                </div>
              </div>
            </div>
          </div>
        )}

        {activeSection === 'quiz' && (
          <div className="space-y-8">
            <div className="text-center space-y-4 mb-12">
              <h2 className="text-5xl font-bold bg-gradient-to-r from-purple-300 to-pink-300 bg-clip-text text-transparent">
                Quiz Interativo
              </h2>
              <p className="text-lg text-cyan-100/60 max-w-2xl mx-auto">
                Teste seus conhecimentos sobre IA e Saúde Mental
              </p>
              <div className="inline-flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-purple-500/20 to-pink-500/20 border border-purple-500/30 rounded-full">
                <TrendingUp className="w-5 h-5 text-purple-300" />
                <span className="text-2xl font-bold text-purple-300">
                  Pontuação: {quizScore}/{quizQuestions.length}
                </span>
              </div>
            </div>

            <div className="max-w-4xl mx-auto space-y-6">
              {quizQuestions.map((question, qIdx) => (
                <div
                  key={question.id}
                  className="bg-gradient-to-br from-white/5 to-white/0 backdrop-blur-sm border border-white/10 rounded-2xl p-8"
                >
                  <div className="flex items-start gap-4 mb-6">
                    <div className="w-12 h-12 rounded-full bg-gradient-to-br from-purple-500 to-pink-600 flex items-center justify-center font-bold text-xl flex-shrink-0">
                      {qIdx + 1}
                    </div>
                    <h3 className="text-xl font-semibold text-white pt-2">{question.question}</h3>
                  </div>

                  <div className="space-y-3">
                    {question.options.map((option, oIdx) => {
                      const answered = quizAnswered[question.id];
                      const isSelected = answered?.selected === oIdx;
                      const isCorrect = oIdx === question.correct;
                      const showResult = answered !== undefined;

                      return (
                        <button
                          key={oIdx}
                          onClick={() => !answered && handleQuizAnswer(question.id, oIdx)}
                          disabled={showResult}
                          className={`w-full text-left p-4 rounded-xl border-2 transition-all flex items-center justify-between group ${
                            !showResult
                              ? 'border-white/10 hover:border-purple-500/50 hover:bg-white/5'
                              : isSelected && isCorrect
                              ? 'border-emerald-500 bg-emerald-500/10'
                              : isSelected && !isCorrect
                              ? 'border-rose-500 bg-rose-500/10'
                              : isCorrect
                              ? 'border-emerald-500/50 bg-emerald-500/5'
                              : 'border-white/10 bg-white/5'
                          }`}
                        >
                          <span className={`${
                            showResult && isCorrect ? 'text-emerald-300' :
                            showResult && isSelected && !isCorrect ? 'text-rose-300' :
                            'text-cyan-100/80'
                          }`}>
                            {option}
                          </span>
                          {showResult && isCorrect && (
                            <Check className="w-6 h-6 text-emerald-400" />
                          )}
                          {showResult && isSelected && !isCorrect && (
                            <X className="w-6 h-6 text-rose-400" />
                          )}
                        </button>
                      );
                    })}
                  </div>
                </div>
              ))}

              {Object.keys(quizAnswered).length === quizQuestions.length && (
                <div className="bg-gradient-to-br from-purple-500/20 to-pink-500/20 border border-purple-500/30 rounded-2xl p-8 text-center">
                  <h3 className="text-3xl font-bold text-white mb-4">
                    {quizScore === quizQuestions.length
                      ? '🎉 Perfeito! Você domina o tema!'
                      : quizScore >= quizQuestions.length / 2
                      ? '👏 Bom trabalho! Continue aprendendo!'
                      : '📚 Continue estudando a skill!'}
                  </h3>
                  <p className="text-lg text-purple-100/80 mb-6">
                    Você acertou {quizScore} de {quizQuestions.length} questões
                  </p>
                  <button
                    onClick={() => {
                      setQuizAnswered({});
                      setQuizScore(0);
                    }}
                    className="px-8 py-3 bg-gradient-to-r from-purple-500 to-pink-600 rounded-xl font-semibold hover:shadow-lg hover:shadow-purple-500/50 transition-all"
                  >
                    Refazer Quiz
                  </button>
                </div>
              )}
            </div>
          </div>
        )}
      </main>

      {/* Footer */}
      <footer className="relative z-10 border-t border-white/10 backdrop-blur-xl bg-black/20 mt-24">
        <div className="max-w-7xl mx-auto px-6 py-8 text-center">
          <p className="text-cyan-300/60 text-sm">
            🧠 Baseado na skill <strong className="text-cyan-300">ia-saude-mental</strong> • 
            Demonstração educativa • 
            IA não substitui profissionais de saúde mental
          </p>
        </div>
      </footer>
    </div>
  );
};

export default IAHealthExplorer;
