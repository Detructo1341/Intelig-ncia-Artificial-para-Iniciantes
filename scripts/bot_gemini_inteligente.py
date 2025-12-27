#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🚀 Coach de Fluência em IA - Edição Visionária
Versão otimizada com Gemini 1.5 Flash e Interface Rich.
"""

import os
import google.generativeai as genai
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.prompt import Prompt
from rich.status import Status

# Configuração da Interface
console = Console()

# ============================================================================
# SYSTEM PROMPT (A Alma do Negócio)
# ============================================================================
SYSTEM_PROMPT = """Você é um Coach de Fluência em Inteligência Artificial.
Sua missão: Ajudar profissionais a desenvolver pensamento estratégico sobre IA através do Framework dos 4Ds:
1. DISCERNIMENTO (Por que usar?)
2. DESCRIÇÃO (Como pedir?)
3. DELEGAÇÃO (O que automatizar?)
4. DILIGÊNCIA (Como validar?)

Estilo: Empático, questionador, rigoroso e nunca ofereça respostas prontas. Incentive a reflexão."""

# ============================================================================
# LOGICA DO BOT
# ============================================================================

class CoachIA:
    def __init__(self, api_key):
        try:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel(
                model_name='gemini-1.5-flash',
                system_instruction=SYSTEM_PROMPT
            )
            self.chat = self.model.start_chat(history=[])
            self.historico = []
        except Exception as e:
            console.print(f"[bold red]❌ Erro na configuração:[/bold red] {e}")

    def responder(self, pergunta):
        with console.status("[bold green]O Coach está processando seu pensamento...[/bold green]"):
            response = self.chat.send_message(pergunta)
            return response.text

    def salvar_log(self):
        if not self.historico:
            return
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"docs/conversa_{timestamp}.md" # Salvando direto na pasta docs
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"# Log de Fluência em IA - {timestamp}\n\n")
            for item in self.historico:
                f.write(f"### 👤 Usuário\n{item['user']}\n\n")
                f.write(f"### 🤖 Coach\n{item['bot']}\n\n---\n")
        console.print(f"\n[bold cyan]✅ Insight documentado em:[/bold cyan] {filename}")

# ============================================================================
# INTERFACE PRINCIPAL
# ============================================================================

def main():
    console.clear()
    console.print(Panel.fit(
        "🚀 [bold azure1]COACH DE FLUÊNCIA EM IA[/bold azure1] 🚀\n[italic]Poder tecnológico com pensamento humano[/italic]",
        border_style="bright_blue"
    ))

    api_key = os.getenv('GOOGLE_API_KEY') or Prompt.ask("[bold yellow]Insira sua Gemini API Key[/bold yellow]", password=True)

    if not api_key:
        console.print("[red]Chave necessária para decolar.[/red]")
        return

    coach = CoachIA(api_key)

    while True:
        user_input = Prompt.ask("\n[bold green]Sua reflexão[/bold green] (ou 'sair'/'salvar')")

        if user_input.lower() == 'sair':
            break
        
        if user_input.lower() == 'salvar':
            coach.salvar_log()
            continue

        resposta = coach.responder(user_input)
        
        # Salva no histórico interno
        coach.historico.append({"user": user_input, "bot": resposta})
        
        console.print("\n[bold blue]🤖 Coach de Fluência:[/bold blue]")
        console.print(Markdown(resposta))
        console.print("-" * 40)

if __name__ == "__main__":
    main()
