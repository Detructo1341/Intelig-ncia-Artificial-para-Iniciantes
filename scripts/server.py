"""
Backend Flask para Dashboard de Agentes IA
Servidor para integração entre o frontend HTML e os agentes de IA
"""

from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import os
import json
from pathlib import Path
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Permitir requisições do frontend

# Configurações
BASE_DIR = Path(__file__).parent
AGENTS_DIR = BASE_DIR / 'prompts' / 'agentes'
WEB_DIR = BASE_DIR / 'web'

# Garantir que os diretórios existam
AGENTS_DIR.mkdir(parents=True, exist_ok=True)
WEB_DIR.mkdir(parents=True, exist_ok=True)

# Armazenamento de sessões (em produção, usar Redis ou banco de dados)
sessions = {}


class Agent:
    """Classe para representar um agente de IA"""
    
    def __init__(self, agent_id, name, description, prompt_file):
        self.id = agent_id
        self.name = name
        self.description = description
        self.prompt_file = prompt_file
        self.system_prompt = self._load_prompt()
    
    def _load_prompt(self):
        """Carrega o prompt do agente do arquivo"""
        try:
            with open(self.prompt_file, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"Erro ao carregar prompt do agente {self.name}: {e}")
            return "Você é um assistente útil e amigável."
    
    def to_dict(self):
        """Converte o agente para dicionário"""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }


def load_agents():
    """Carrega todos os agentes disponíveis na pasta"""
    agents = []
    
    if not AGENTS_DIR.exists():
        return agents
    
    for file_path in AGENTS_DIR.glob('*.txt'):
        agent_id = file_path.stem
        
        # Tentar carregar metadados do agente
        metadata_file = file_path.with_suffix('.json')
        
        if metadata_file.exists():
            try:
                with open(metadata_file, 'r', encoding='utf-8') as f:
                    metadata = json.load(f)
                    name = metadata.get('name', agent_id)
                    description = metadata.get('description', 'Agente de IA')
            except Exception as e:
                print(f"Erro ao carregar metadados: {e}")
                name = agent_id
                description = 'Agente de IA'
        else:
            # Usar nome do arquivo como nome do agente
            name = agent_id.replace('_', ' ').replace('-', ' ').title()
            description = 'Agente de IA'
        
        agent = Agent(agent_id, name, description, file_path)
        agents.append(agent)
    
    return agents


def simulate_ai_response(agent, message, history):
    """
    Simula uma resposta do agente de IA
    
    Em produção, você pode integrar com:
    - OpenAI API
    - Anthropic Claude API
    - Modelos locais (LLaMA, Mistral, etc.)
    - Outros serviços de IA
    """
    
    # Aqui você implementaria a lógica real de IA
    # Por enquanto, retorna uma resposta simulada
    
    responses = [
        f"Entendi sua mensagem: '{message}'. Como posso ajudar mais?",
        f"Interessante! Sobre '{message}', eu diria que...",
        f"Baseado no que você disse sobre '{message}', posso sugerir...",
        f"Ótima pergunta sobre '{message}'! Deixe-me pensar...",
    ]
    
    import random
    base_response = random.choice(responses)
    
    return f"{base_response}\n\n[Agente: {agent.name}]\n[Sistema: Esta é uma resposta simulada. Integre com sua API de IA preferida para respostas reais.]"


@app.route('/')
def index():
    """Serve a página principal do dashboard"""
    return send_from_directory(WEB_DIR, 'dashboard.html')


@app.route('/api/health', methods=['GET'])
def health_check():
    """Endpoint de verificação de saúde do servidor"""
    return jsonify({
        'status': 'ok',
        'timestamp': datetime.now().isoformat(),
        'message': 'Servidor rodando normalmente'
    })


@app.route('/api/agents', methods=['GET'])
def get_agents():
    """Retorna a lista de agentes disponíveis"""
    agents = load_agents()
    return jsonify([agent.to_dict() for agent in agents])


@app.route('/api/chat', methods=['POST'])
def chat():
    """Endpoint principal para conversação com os agentes"""
    try:
        data = request.json
        agent_id = data.get('agent_id')
        message = data.get('message')
        history = data.get('history', [])
        
        if not agent_id or not message:
            return jsonify({
                'error': 'agent_id e message são obrigatórios'
            }), 400
        
        # Carregar o agente
        agents = load_agents()
        agent = next((a for a in agents if a.id == agent_id), None)
        
        if not agent:
            return jsonify({
                'error': 'Agente não encontrado'
            }), 404
        
        # Processar mensagem e gerar resposta
        response = simulate_ai_response(agent, message, history)
        
        return jsonify({
            'response': response,
            'agent_id': agent_id,
            'timestamp': datetime.now().isoformat()
        })
    
    except Exception as e:
        print(f"Erro no chat: {e}")
        return jsonify({
            'error': 'Erro ao processar mensagem',
            'details': str(e)
        }), 500


@app.route('/api/agents/<agent_id>', methods=['GET'])
def get_agent_details(agent_id):
    """Retorna detalhes de um agente específico"""
    agents = load_agents()
    agent = next((a for a in agents if a.id == agent_id), None)
    
    if not agent:
        return jsonify({
            'error': 'Agente não encontrado'
        }), 404
    
    return jsonify({
        **agent.to_dict(),
        'system_prompt': agent.system_prompt
    })


def create_sample_agents():
    """Cria agentes de exemplo se a pasta estiver vazia"""
    if not any(AGENTS_DIR.glob('*.txt')):
        print("Criando agentes de exemplo...")
        
        # Agente 1: Assistente Geral
        with open(AGENTS_DIR / 'assistente_geral.txt', 'w', encoding='utf-8') as f:
            f.write("""Você é um assistente de IA útil, educado e amigável.
Seu objetivo é ajudar o usuário com qualquer pergunta ou tarefa que ele tenha.
Seja claro, conciso e sempre respeitoso.""")
        
        with open(AGENTS_DIR / 'assistente_geral.json', 'w', encoding='utf-8') as f:
            json.dump({
                'name': 'Assistente Geral',
                'description': 'Assistente versátil para tarefas diversas'
            }, f, ensure_ascii=False, indent=2)
        
        # Agente 2: Especialista em Programação
        with open(AGENTS_DIR / 'programador.txt', 'w', encoding='utf-8') as f:
            f.write("""Você é um especialista em programação e desenvolvimento de software.
Você domina várias linguagens como Python, JavaScript, Java, C++, e outras.
Ajude o usuário com código, debugging, boas práticas e arquitetura de software.""")
        
        with open(AGENTS_DIR / 'programador.json', 'w', encoding='utf-8') as f:
            json.dump({
                'name': 'Especialista em Programação',
                'description': 'Expert em código e desenvolvimento'
            }, f, ensure_ascii=False, indent=2)
        
        # Agente 3: Tutor Educacional
        with open(AGENTS_DIR / 'tutor.txt', 'w', encoding='utf-8') as f:
            f.write("""Você é um tutor educacional paciente e didático.
Sua missão é explicar conceitos complexos de forma simples e clara.
Use exemplos práticos e analogias para facilitar o entendimento.""")
        
        with open(AGENTS_DIR / 'tutor.json', 'w', encoding='utf-8') as f:
            json.dump({
                'name': 'Tutor Educacional',
                'description': 'Professor virtual para aprendizado'
            }, f, ensure_ascii=False, indent=2)
        
        print("Agentes de exemplo criados com sucesso!")


if __name__ == '__main__':
    print("=" * 60)
    print("🤖 Servidor Backend para Dashboard de Agentes IA")
    print("=" * 60)
    print(f"\n📁 Pasta de agentes: {AGENTS_DIR}")
    print(f"🌐 Pasta web: {WEB_DIR}")
    
    # Criar agentes de exemplo se necessário
    create_sample_agents()
    
    # Listar agentes disponíveis
    agents = load_agents()
    print(f"\n✅ {len(agents)} agente(s) carregado(s):")
    for agent in agents:
        print(f"   - {agent.name} ({agent.id})")
    
    print(f"\n🚀 Servidor rodando em: http://localhost:5000")
    print(f"📱 Dashboard disponível em: http://localhost:5000")
    print("\n💡 Dica: Adicione seus próprios agentes na pasta prompts/agentes/")
    print("=" * 60)
    print()
    
    # Iniciar servidor
    app.run(host='0.0.0.0', port=5000, debug=True)
