<!DOCTYPE html>
<html lang="pt-BR" class="scroll-smooth">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>IA ULTRA | A Ontologia da Inteligência Artificial</title>
    <meta name="description" content="Um tratado interativo sobre a mecânica, a filosofia e o futuro da inteligência sintética.">
    
    <!-- Open Graph -->
    <meta property="og:title" content="IA ULTRA | A Ontologia da Inteligência Artificial">
    <meta property="og:description" content="Explore os fundamentos e a fronteira da IA através de um guia interativo e imersivo.">
    <meta property="og:type" content="website">

    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
    
    <style>
      /* Estética de grão sutil para profundidade visual */
      body::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: url("https://grainy-gradients.vercel.app/noise.svg");
        opacity: 0.03;
        pointer-events: none;
        z-index: 100;
      }

      /* Custom Scrollbar */
      ::-webkit-scrollbar {
        width: 6px;
      }
      ::-webkit-scrollbar-track {
        background: #020617;
      }
      ::-webkit-scrollbar-thumb {
        background: #1e293b;
        border-radius: 10px;
      }
      ::-webkit-scrollbar-thumb:hover {
        background: #38bdf8;
      }

      /* Suavização de renderização de fontes */
      * {
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
      }
    </style>

    <script>
      tailwind.config = {
        theme: {
          extend: {
            fontFamily: {
              sans: ['Inter', 'sans-serif'],
              mono: ['JetBrains Mono', 'monospace'],
            },
            colors: {
              bg: '#0f172a',
              sidebar: '#020617',
              accent: '#38bdf8',
              text: '#e2e8f0',
              muted: '#94a3b8',
              border: '#1e293b',
              surface: '#1e293b',
            },
            animation: {
              'pulse-slow': 'pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite',
              'wave': 'wave 1.2s ease-in-out infinite',
              'float': 'float 6s ease-in-out infinite',
            },
            keyframes: {
              wave: {
                '0%, 100%': { height: '10%' },
                '50%': { height: '50%' },
              },
              float: {
                '0%, 100%': { transform: 'translateY(0)' },
                '50%': { transform: 'translateY(-20px)' },
              }
            }
          }
        }
      }
    </script>
    <script type="importmap">
    {
      "imports": {
        "react-dom/client": "https://aistudiocdn.com/react-dom@^19.2.1/client",
        "react-dom/": "https://aistudiocdn.com/react-dom@^19.2.1/",
        "@google/genai": "https://aistudiocdn.com/@google/genai@^1.31.0",
        "react/": "https://aistudiocdn.com/react@^19.2.1/",
        "react": "https://aistudiocdn.com/react@^19.2.1",
        "lucide-react": "https://aistudiocdn.com/lucide-react@^0.556.0"
      }
    }
    </script>
  </head>
  <body class="bg-bg text-text font-sans antialiased overflow-x-hidden">
    <div id="root"></div>
    <script type="module" src="index.tsx"></script>
  </body>
</html>
