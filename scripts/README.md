# 🤖 Dashboard de Agentes IA

Dashboard moderno e responsivo para interagir com agentes de IA personalizados.

## 📋 Características

- ✨ Interface moderna e minimalista com Tailwind CSS
- 📱 Totalmente responsivo (funciona em desktop, tablet e celular)
- 🔄 Integração com backend Python (Flask)
- 🎨 Design intuitivo com sidebar para seleção de agentes
- 💬 Área de chat centralizada
- 🚀 Fácil de expandir e personalizar

## 🛠️ Instalação

### 1. Instalar dependências Python

```bash
pip install -r requirements.txt
```

Ou instale manualmente:

```bash
pip install flask flask-cors
```

### 2. Estrutura de pastas

O projeto deve ter a seguinte estrutura:

```
projeto/
├── server.py                    # Servidor backend Flask
├── requirements.txt             # Dependências Python
├── web/
│   └── dashboard.html          # Dashboard frontend
└── prompts/
    └── agentes/                # Pasta para seus agentes
        ├── agente1.txt         # Prompt do agente
        ├── agente1.json        # Metadados do agente (opcional)
        ├── agente2.txt
        └── agente2.json
```

## 🚀 Como usar

### 1. Iniciar o servidor

```bash
python server.py
```

O servidor irá:
- Criar agentes de exemplo automaticamente na primeira execução
- Iniciar na porta 5000
- Exibir os agentes carregados

### 2. Acessar o dashboard

Abra seu navegador e acesse:

```
http://localhost:5000
```

### 3. Criar seus próprios agentes

#### Opção 1: Arquivo de texto simples

Crie um arquivo `.txt` na pasta `prompts/agentes/`:

**Exemplo:** `prompts/agentes/meu_agente.txt`

```
Você é um assistente especializado em [sua especialidade].
Seu objetivo é ajudar com [descrição das tarefas].
[Adicione mais instruções conforme necessário]
```

#### Opção 2: Com metadados (recomendado)

Crie dois arquivos:

**1. Prompt:** `prompts/agentes/meu_agente.txt`

```
Você é um especialista em psicologia cognitiva.
Ajude o usuário a entender conceitos de psicologia de forma clara e acessível.
```

**2. Metadados:** `prompts/agentes/meu_agente.json`

```json
{
  "name": "Especialista em Psicologia",
  "description": "Expert em psicologia cognitiva e comportamental"
}
```

## 🔧 Personalização

### Integrar com APIs de IA reais

Edite a função `simulate_ai_response` em `server.py`:

```python
def simulate_ai_response(agent, message, history):
    # Exemplo com OpenAI
    import openai
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": agent.system_prompt},
            *[{"role": m["role"], "content": m["content"]} for m in history],
            {"role": "user", "content": message}
        ]
    )
    
    return response.choices[0].message.content
```

### Alterar porta do servidor

Edite a última linha de `server.py`:

```python
app.run(host='0.0.0.0', port=8000, debug=True)  # Mude 5000 para sua porta
```

### Personalizar estilo do dashboard

Edite o arquivo `web/dashboard.html` e modifique:
- Cores no Tailwind (ex: `bg-blue-600` → `bg-purple-600`)
- Layout e componentes
- Animações e transições

## 📱 Funcionalidades do Dashboard

### Desktop
- Sidebar sempre visível com lista de agentes
- Chat centralizado com área ampla
- Header com status de conexão

### Mobile
- Sidebar retrátil (botão de menu)
- Layout otimizado para tela pequena
- Botões de toque responsivos

### Funcionalidades gerais
- Seleção de agente via sidebar
- Envio de mensagens
- Histórico de conversação
- Indicador de status (conectado/desconectado)
- Botão "Novo Chat" para limpar conversação

## 🔐 Segurança

⚠️ **Importante:** Este é um projeto de exemplo para desenvolvimento local.

Para produção, considere:
- Implementar autenticação de usuários
- Usar HTTPS
- Adicionar rate limiting
- Validar inputs adequadamente
- Usar variáveis de ambiente para configurações sensíveis

## 🐛 Resolução de problemas

### Servidor não inicia
- Verifique se todas as dependências estão instaladas
- Confirme que a porta 5000 está disponível
- Execute: `pip install flask flask-cors`

### Agentes não aparecem
- Verifique se os arquivos estão na pasta `prompts/agentes/`
- Confirme que os arquivos têm extensão `.txt`
- Reinicie o servidor

### Dashboard não carrega
- Verifique se o servidor está rodando
- Teste: `http://localhost:5000/api/health`
- Verifique o console do navegador (F12) para erros

## 📚 Próximos passos

- [ ] Integrar com API de IA real (OpenAI, Anthropic, etc.)
- [ ] Adicionar persistência de conversas (banco de dados)
- [ ] Implementar upload de arquivos
- [ ] Adicionar suporte a markdown nas mensagens
- [ ] Criar sistema de tags para organizar agentes
- [ ] Adicionar busca de agentes
- [ ] Implementar autenticação de usuários

## 📄 Licença

Este projeto é fornecido como exemplo educacional. Sinta-se livre para usar e modificar conforme necessário.

## 🤝 Contribuindo

Sugestões e melhorias são bem-vindas! Sinta-se à vontade para personalizar o código conforme suas necessidades.

---

Desenvolvido com ❤️ para facilitar a interação com agentes de IA
