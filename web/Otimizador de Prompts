<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gerenciador de Prompts (Local Storage)</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        /* Estilo para quebrar linha no textarea e cards */
        .whitespace-pre-wrap {
            white-space: pre-wrap;
        }
        /* Efeito de foco simples para input/textarea */
        #promptInput:focus {
            outline: none;
            box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.5); /* Indigo 500 com transparência */
        }
    </style>
</head>
<body class="bg-gray-50 min-h-screen font-sans antialiased p-4 sm:p-8">

    <script>
        // =======================================================
        // 🚨 CONFIGURAÇÃO DA API GEMINI 🚨
        // =======================================================
        
        // Sua chave de API para o Gemini (Opcional - Necessário para aprimorar/resumir prompts)
        // Deixe em branco ("") para desabilitar as funções de IA.
        const apiKey = ""; 
        const GEMINI_MODEL = 'gemini-2.5-flash-preview-09-2025';
        const apiUrl = (model) => 
            `https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${apiKey}`;

        // =======================================================
        // VARIÁVEIS DE ESTADO E PERSISTÊNCIA LOCAL
        // =======================================================
        let allPrompts = [];
        const LOCAL_STORAGE_KEY = 'localPrompts';

        // 1. Funções de Persistência (LocalStorage)

        // Carrega prompts do LocalStorage e atualiza a UI
        const loadPromptsFromLocalStorage = () => {
            try {
                const storedPrompts = localStorage.getItem(LOCAL_STORAGE_KEY);
                if (storedPrompts) {
                    // Carrega e ordena por timestamp (mais recente primeiro)
                    allPrompts = JSON.parse(storedPrompts).sort((a, b) => b.timestamp - a.timestamp);
                } else {
                    allPrompts = [];
                }
                filterPrompts();
            } catch (e) {
                console.error("Erro ao carregar prompts do LocalStorage:", e);
                document.getElementById('status').textContent = "ERRO: Falha ao carregar dados do armazenamento local.";
                allPrompts = [];
            }
        };

        // Salva o array de prompts no LocalStorage
        const savePromptsToLocalStorage = () => {
            try {
                localStorage.setItem(LOCAL_STORAGE_KEY, JSON.stringify(allPrompts));
            } catch (e) {
                console.error("Erro ao salvar prompts no LocalStorage:", e);
                document.getElementById('status').textContent = "ERRO: Falha ao salvar dados no armazenamento local.";
            }
        };

        // 2. Inicialização do Aplicativo (Substituindo initFirebase)
        const initApp = () => {
            // O ID do usuário agora é apenas um indicador local
            const userId = 'local_user';
            document.getElementById('userIdDisplay').textContent = `Usuário ID: ${userId} (Armazenamento Local)`;
            document.getElementById('status').textContent = "Pronto. Os prompts são salvos neste navegador.";
            document.getElementById('status').classList.remove('text-red-600');
            document.getElementById('status').classList.add('text-green-600');
            
            // Carrega os dados
            loadPromptsFromLocalStorage();
        };

        // 3. Funções de Ação

        // Adicionar Prompt
        window.savePrompt = () => {
            const promptInput = document.getElementById('promptInput');
            const promptText = promptInput.value.trim();

            if (!promptText) {
                showModal('Erro', 'O prompt não pode estar vazio.');
                return;
            }

            const saveBtn = document.getElementById('saveBtn');
            saveBtn.disabled = true;
            saveBtn.textContent = 'Salvando...';

            try {
                // Cria um novo prompt com ID único e timestamp
                const newPrompt = {
                    id: crypto.randomUUID(), // Função moderna para IDs únicos
                    text: promptText,
                    timestamp: Date.now() 
                };
                
                allPrompts.unshift(newPrompt); // Adiciona no início (mais recente)
                savePromptsToLocalStorage();
                filterPrompts(); // Atualiza a lista
                
                promptInput.value = '';
                showModal('Sucesso', 'Prompt salvo com sucesso no Local Storage!');
            } catch (error) {
                console.error("Erro ao salvar prompt no Local Storage:", error);
                showModal('Erro', 'Ocorreu um erro ao salvar o prompt.');
            } finally {
                saveBtn.disabled = false;
                saveBtn.textContent = 'Salvar Prompt';
            }
        };

        // Deletar Prompt
        const deletePrompt = (promptId) => {
            try {
                // Filtra para remover o prompt
                allPrompts = allPrompts.filter(p => p.id !== promptId);
                
                savePromptsToLocalStorage();
                filterPrompts(); // Atualiza a lista
                
                showModal('Sucesso', 'Prompt excluído!');
            } catch (error) {
                console.error("Erro ao deletar prompt:", error);
                showModal('Erro', 'Ocorreu um erro ao excluir o prompt.');
            } finally {
                document.getElementById('customModal').classList.add('hidden');
            }
        };

        // Funções de utilidade e LLM (Mantidas)
        
        // Função para renderizar um subconjunto de prompts
        const renderPrompts = (promptsToRender) => {
            const promptsList = document.getElementById('promptsList');
            promptsList.innerHTML = ''; 

            if (promptsToRender.length === 0) {
                const searchInput = document.getElementById('searchInput');
                const message = searchInput.value.trim() 
                    ? `Nenhum prompt encontrado para "${searchInput.value.trim()}".` 
                    : 'Nenhum prompt salvo ainda. Comece a adicionar!';

                promptsList.innerHTML = `<p class="text-center text-gray-500 p-4">${message}</p>`;
                return;
            }

            promptsToRender.forEach((prompt) => {
                createPromptCard(promptsList, prompt.id, prompt.text);
            });
        };

        // Função para filtrar os prompts na UI
        window.filterPrompts = () => {
            const searchInput = document.getElementById('searchInput');
            const searchText = searchInput.value.toLowerCase().trim();

            if (!searchText) {
                // Garante que a lista está ordenada antes de renderizar (caso tenha sido modificada)
                allPrompts.sort((a, b) => b.timestamp - a.timestamp);
                renderPrompts(allPrompts);
                return;
            }

            const filteredPrompts = allPrompts.filter(prompt => 
                prompt.text.toLowerCase().includes(searchText)
            );

            renderPrompts(filteredPrompts);
        };

        // Função utilitária para criar o card do prompt na UI
        const createPromptCard = (container, id, text) => {
            const card = document.createElement('div');
            card.setAttribute('data-prompt-id', id); 
            card.className = 'prompt-card bg-white shadow-lg rounded-xl p-4 transition duration-300 ease-in-out hover:shadow-xl flex flex-col space-y-3';
            
            const promptText = document.createElement('p');
            promptText.className = 'text-gray-700 whitespace-pre-wrap flex-grow';
            promptText.textContent = text;
            
            const controls = document.createElement('div');
            controls.className = 'flex flex-wrap justify-end space-x-2 border-t pt-3 mt-3';
            
            const summaryDisplay = document.createElement('p');
            summaryDisplay.id = `summary-${id}`;
            summaryDisplay.className = 'w-full text-sm text-gray-500 italic mt-2 mb-3';
            
            const summarizeBtn = document.createElement('button');
            summarizeBtn.textContent = '✨ Resumir Prompt';
            summarizeBtn.className = 'text-sm font-medium py-2 px-3 rounded-lg bg-green-100 text-green-700 hover:bg-green-200 transition mb-2 sm:mb-0';
            summarizeBtn.onclick = () => generateSummary(text, id, summarizeBtn);

            const copyBtn = document.createElement('button');
            copyBtn.textContent = 'Copiar';
            copyBtn.className = 'text-sm font-medium py-2 px-3 rounded-lg bg-indigo-100 text-indigo-700 hover:bg-indigo-200 transition mb-2 sm:mb-0';
            copyBtn.onclick = () => copyToClipboard(text);

            const deleteBtn = document.createElement('button');
            deleteBtn.textContent = 'Excluir';
            deleteBtn.className = 'text-sm font-medium py-2 px-3 rounded-lg bg-red-100 text-red-700 hover:bg-red-200 transition mb-2 sm:mb-0';
            deleteBtn.onclick = () => showDeleteConfirmation(id);
            
            controls.appendChild(summarizeBtn);
            controls.appendChild(copyBtn);
            controls.appendChild(deleteBtn);
            
            card.appendChild(promptText);
            card.appendChild(summaryDisplay); 
            card.appendChild(controls);
            container.appendChild(card);
        };

        // Função LLM para refinar/expandir um prompt
        window.enhancePrompt = async () => {
            const promptInput = document.getElementById('promptInput');
            const originalPrompt = promptInput.value.trim();
            
            if (!originalPrompt) {
                showModal('Atenção', 'Digite um rascunho de prompt para ser aprimorado.');
                return;
            }
            
            if (apiKey === "") {
                showModal('Atenção', 'A chave Gemini API não foi configurada. A função de aprimoramento está desativada.');
                return;
            }


            const enhanceBtn = document.getElementById('enhanceBtn');
            const originalText = enhanceBtn.textContent;
            
            enhanceBtn.disabled = true;
            enhanceBtn.textContent = 'Aprimorando...';
            
            try {
                const userQuery = `Refine e expanda o seguinte rascunho de prompt para torná-lo mais detalhado, completo e eficaz. Apresente apenas o novo prompt melhorado:\n\n${originalPrompt}`;
                
                const payload = {
                    contents: [{ parts: [{ text: userQuery }] }],
                    systemInstruction: {
                        parts: [{ text: "Você é um assistente de engenharia de prompt de IA. Sua única tarefa é pegar um rascunho de prompt e torná-lo um prompt de nível profissional, completo e detalhado. Responda APENAS com o texto do prompt aprimorado." }]
                    },
                };

                const response = await fetchWithRetry(apiUrl(GEMINI_MODEL), {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });

                const result = await response.json();
                const newPrompt = result.candidates?.[0]?.content?.parts?.[0]?.text;
                
                if (newPrompt) {
                    promptInput.value = newPrompt.trim();
                    showModal('Sucesso', 'Prompt aprimorado pelo Gemini! Revise e salve.');
                } else {
                    showModal('Erro', 'Aprimoramento falhou. Tente novamente.');
                }
            } catch (error) {
                console.error("Erro ao aprimorar prompt:", error);
                showModal('Erro', 'Erro de conexão com o Gemini API.');
            } finally {
                enhanceBtn.disabled = false;
                enhanceBtn.textContent = originalText;
            }
        };

        // Função LLM para gerar um resumo
        const generateSummary = async (promptText, id, button) => {
            const summaryDisplay = document.getElementById(`summary-${id}`);
            const originalButtonText = button.textContent;
            
            if (summaryDisplay.textContent && summaryDisplay.textContent !== 'Gerando resumo...') {
                 summaryDisplay.textContent = ''; 
                 button.textContent = originalButtonText;
                 return;
            }

            if (apiKey === "") {
                showModal('Atenção', 'A chave Gemini API não foi configurada. A função de resumo está desativada.');
                return;
            }

            button.textContent = 'Gerando resumo...';
            summaryDisplay.textContent = 'Gerando resumo...';
            
            try {
                const userQuery = `Gere um resumo conciso e de uma frase (no máximo 15 palavras) para o seguinte prompt. Comece com "Resumo:".\n\nPrompt: "${promptText}"`;
                
                const payload = {
                    contents: [{ parts: [{ text: userQuery }] }],
                    systemInstruction: {
                        parts: [{ text: "Você é um assistente conciso. Sua única tarefa é resumir o texto fornecido em uma única frase. Responda APENAS com a frase de resumo." }]
                    },
                };

                const response = await fetchWithRetry(apiUrl(GEMINI_MODEL), {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });

                const result = await response.json();
                const summary = result.candidates?.[0]?.content?.parts?.[0]?.text;
                
                if (summary) {
                    summaryDisplay.textContent = summary.trim();
                } else {
                    summaryDisplay.textContent = 'Não foi possível gerar o resumo.';
                }
            } catch (error) {
                console.error("Erro ao gerar resumo:", error);
                summaryDisplay.textContent = 'Erro na API.';
            } finally {
                button.textContent = originalButtonText;
            }
        };

        // Exponential backoff for API calls
        const fetchWithRetry = async (url, options, maxRetries = 5) => {
            for (let i = 0; i < maxRetries; i++) {
                try {
                    const response = await fetch(url, options);
                    if (response.status !== 429) {
                        return response;
                    }
                    const delay = Math.pow(2, i) * 1000 + Math.random() * 1000;
                    await new Promise(resolve => setTimeout(resolve, delay));
                } catch (error) {
                    const delay = Math.pow(2, i) * 1000 + Math.random() * 1000;
                    await new Promise(resolve => setTimeout(resolve, delay));
                }
            }
            throw new Error('Maximum retry attempts exceeded.');
        };


        // Copiar para o Clipboard
        const copyToClipboard = (text) => {
            const tempInput = document.createElement('textarea');
            tempInput.value = text;
            document.body.appendChild(tempInput);
            tempInput.select();
            try {
                document.execCommand('copy');
                showModal('Copiado', 'Prompt copiado para a área de transferência!');
            } catch (err) {
                console.error('Falha ao copiar:', err);
                showModal('Erro', 'Falha ao copiar. Tente selecionar o texto manualmente.');
            }
            document.body.removeChild(tempInput);
        };

        // Modal Personalizado (Substitui alert/confirm)
        const showModal = (title, message, isConfirm = false, onConfirm = null) => {
            const modal = document.getElementById('customModal');
            const modalTitle = document.getElementById('modalTitle');
            const modalMessage = document.getElementById('modalMessage');
            const modalConfirmBtn = document.getElementById('modalConfirmBtn');
            const modalCancelBtn = document.getElementById('modalCancelBtn');
            
            modalTitle.textContent = title;
            modalMessage.textContent = message;

            if (isConfirm) {
                modalConfirmBtn.classList.remove('hidden');
                modalConfirmBtn.textContent = 'Confirmar';
                modalCancelBtn.classList.remove('hidden');
                modalConfirmBtn.onclick = () => { onConfirm(); modal.classList.add('hidden'); };
                modalCancelBtn.onclick = () => { modal.classList.add('hidden'); };
            } else {
                modalConfirmBtn.classList.remove('hidden');
                modalConfirmBtn.textContent = 'OK';
                modalCancelBtn.classList.add('hidden');
                modalConfirmBtn.onclick = () => { modal.classList.add('hidden'); };
            }
            
            modal.classList.remove('hidden');
        };

        window.closeModal = () => {
            document.getElementById('customModal').classList.add('hidden');
        }

        const showDeleteConfirmation = (id) => {
            showModal(
                'Confirmação', 
                'Tem certeza de que deseja excluir este prompt? Esta ação é irreversível.',
                true,
                () => deletePrompt(id)
            );
        }

        // Inicia o app no carregamento da página
        window.onload = initApp;
    </script>

    <!-- Modal Customizado (Oculto por padrão) -->
    <div id="customModal" class="hidden fixed inset-0 bg-gray-600 bg-opacity-75 flex items-center justify-center z-50 transition-opacity duration-300">
        <div class="bg-white rounded-xl shadow-2xl p-6 w-11/12 max-w-sm transform scale-100 transition-transform duration-300">
            <h3 id="modalTitle" class="text-xl font-bold text-gray-800 mb-4">Título do Modal</h3>
            <p id="modalMessage" class="text-gray-600 mb-6"></p>
            <div class="flex justify-end space-x-3">
                <button id="modalCancelBtn" onclick="closeModal()" class="hidden py-2 px-4 bg-gray-200 text-gray-700 rounded-lg hover:bg-gray-300 font-medium transition">Cancelar</button>
                <button id="modalConfirmBtn" onclick="closeModal()" class="py-2 px-4 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 font-medium transition">OK</button>
            </div>
        </div>
    </div>

    <div class="max-w-4xl mx-auto">
        
        <header class="text-center mb-8">
            <h1 class="text-4xl font-extrabold text-gray-900 mb-2">
                <span class="bg-clip-text text-transparent bg-gradient-to-r from-indigo-500 to-purple-600">
                    Prompt Manager (Local) 🚀
                </span>
            </h1>
            <p id="userIdDisplay" class="text-sm text-gray-500 mt-1">Carregando Usuário...</p>
            <p id="status" class="text-xs font-semibold mt-1 text-green-600">Iniciando aplicação...</p>
            <p class="text-xs text-red-500 font-bold mt-1">⚠️ ATENÇÃO: Os dados são salvos apenas no Local Storage deste navegador.</p>
        </header>

        <!-- Seção de Adicionar Novo Prompt -->
        <section class="bg-white p-6 sm:p-8 rounded-2xl shadow-xl mb-10 border border-gray-200">
            <h2 class="text-2xl font-semibold text-gray-800 mb-4">Novo Prompt</h2>
            
            <textarea id="promptInput" 
                      rows="4" 
                      placeholder="Cole ou escreva seu prompt genial aqui..." 
                      class="w-full p-4 border border-gray-300 rounded-xl mb-4 text-gray-700 resize-y focus:ring-4 focus:ring-indigo-200 focus:border-indigo-500 transition duration-150"></textarea>
            
            <div class="flex flex-col sm:flex-row space-y-3 sm:space-y-0 sm:space-x-3">
                <button id="enhanceBtn" 
                        onclick="enhancePrompt()" 
                        class="w-full sm:w-1/2 py-3 px-6 bg-purple-600 text-white font-bold rounded-xl shadow-md hover:bg-purple-700 transition duration-150 ease-in-out transform hover:scale-[1.01] disabled:opacity-50 disabled:cursor-not-allowed">
                    ✨ Aprimorar Prompt (Gemini)
                </button>
                <button id="saveBtn" 
                        onclick="savePrompt()" 
                        class="w-full sm:w-1/2 py-3 px-6 bg-indigo-600 text-white font-bold rounded-xl shadow-md hover:bg-indigo-700 transition duration-150 ease-in-out transform hover:scale-[1.01] disabled:opacity-50 disabled:cursor-not-allowed">
                    Salvar Prompt
                </button>
            </div>
        </section>

        <!-- Seção de Lista de Prompts -->
        <section>
            <h2 class="text-2xl font-semibold text-gray-800 mb-6">Meus Prompts Salvos</h2>

            <!-- Barra de Busca/Filtro -->
            <div class="bg-white p-4 rounded-xl shadow-md mb-6">
                <input type="text" id="searchInput" oninput="filterPrompts()"
                    placeholder="Buscar por palavras-chave ou frases..."
                    class="w-full p-3 border border-gray-300 rounded-lg text-gray-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 transition duration-150">
            </div>
            
            <div id="promptsList" class="space-y-4">
                <!-- Prompts serão carregados aqui pelo JavaScript -->
                <div class="text-center text-gray-500 p-4">Carregando seus prompts...</div>
            </div>
        </section>

    </div>

</body>
</html>
