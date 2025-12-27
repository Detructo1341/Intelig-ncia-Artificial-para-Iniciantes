#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
💎 Coach de Fluência em IA - Edição 2.0/3.0 Flash
Otimizado para máxima performance e pensamento estratégico.
"""

import os
import google.generativeai as genai
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.prompt import Prompt

# Configuração da Interface
console = Console()

# ============================================================================
# SYSTEM PROMPT (A Alma Visionária)
# ============================================================================
SYSTEM_PROMPT = """Você é o Coach Supremo de Fluência em IA.
Sua missão: Transformar leigos em estrategistas através do Framework dos 4Ds:
1. DISCERNIMENTO (IA é a ferramenta certa aqui?)
2. DESCRIÇÃO (Seu prompt tem contexto, persona e critérios?)
3. DELEGAÇÃO (Isso exige julgamento humano ou é processual?)
4. DILIGÊNCIA (Como você vai auditar o que a IA entregou?)

Estilo: Provocador, socrático e profundamente ético. Nunca dê o peixe, ensine a pescar."""

class CoachIA:
    def __init__(self, api_key):
        try:
            genai.configure(api_key=api_key)
            # Usando a versão mais atual disponível (2.0 Flash)
            # Nota: Quando o 'gemini-3-flash' estiver disponível publicamente no SDK, basta alterar aqui
            self.model = genai.GenerativeModel(
                model_name='gemini-2.0-flash-exp', 
                system_instruction=SYSTEM_PROMPT
            )
            self.chat = self.model.start_chat(history=[])
            self.historico = []
        except Exception as e:
            console.print(f"[bold red]❌ Erro de Configuração:[/bold red] {e}")

    def responder(self, pergunta):
        with console.status("[bold cyan]Processando via Flash Engine...[/bold cyan]"):
            try:
                response = self.chat.send_message(pergunta)
                return response.text
            except Exception as e:
                return f"Erro na API: {str(e)}"

    def salvar_log(self):
        if not self.historico:
            console.print("[yellow]Nenhuma conversa para salvar ainda.[/yellow]")
            return
        
        # Cria a pasta docs se não existir
        if not os.path.exists('docs'):
            os.makedirs('docs')
            
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"docs/sessao_coach_{timestamp}.md"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"# 🧠 Sessão de Mentoria IA - {timestamp}\n\n")
            for item in self.historico:
                f.write(f"### 👤 Desafio do Gabriel\n{item['user']}\n\n")
                f.write(f"### 🤖 Insight do Coach\n{item['bot']}\n\n---\n")
        
        console.print(Panel(f"✅ Conversa eternizada em: [bold]{filename}[/bold]", style="green"))

def main():
    console.clear()
    console.print(Panel.fit(
        "⚡ [bold magenta]GEMINI FLASH EDITION[/bold magenta] ⚡\n[italic]Fluência em IA para Iniciantes - Repositório Detructo1341[/italic]",
        border_style="magenta"
    ))

    # Prioriza variável de ambiente por segurança
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        api_key = Prompt.ask("[bold yellow]Insira sua API Key[/bold yellow]", password=True)

    coach = CoachIA(api_key)

    while True:
        user_input = Prompt.ask("\n[bold]Pergunta[/bold] (ou [red]'sair'[/red]/[blue]'salvar'[/blue])")

        if user_input.lower() in ['sair', 'exit', 'quit']:
            console.print("[italic]Encerrando o núcleo... Até a próxima evolução, Gabriel![/italic]")
            break
        
        if user_input.lower() == 'salvar':
            coach.salvar_log()
            continue

        resposta = coach.responder(user_input)
        coach.historico.append({"user": user_input, "bot": resposta})
        
        console.print("\n[bold magenta]Coach >[/bold magenta]")
        console.print(Markdown(resposta))
        console.print("=" * 50)

if __name__ == "__main__":
    main()
