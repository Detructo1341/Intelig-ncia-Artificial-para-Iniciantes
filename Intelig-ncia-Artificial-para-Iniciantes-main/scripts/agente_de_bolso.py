#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Pocket Agent Runner - Gemini 3 Flash Edition 🚀
Transforma prompts estruturados em ferramentas de produtividade.
"""

import os
import google.generativeai as genai
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Select
from rich.markdown import Markdown

console = Console()

class AgenteDeBolso:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model_name = 'gemini-3-flash'

    def rodar_agente(self, instrucao_sistema, entrada_usuario):
        model = genai.GenerativeModel(
            model_name=self.model_name,
            system_instruction=instrucao_sistema
        )
        with console.status("[bold green]Agente a trabalhar...[/bold green]"):
            response = model.generate_content(entrada_usuario)
            return response.text

def carregar_agentes():
    # Caminho para a pasta de prompts que sugerimos criar
    pasta = "prompts/agentes/"
    if not os.path.exists(pasta):
        os.makedirs(pasta)
        # Cria um exemplo se não existir
        with open(f"{pasta}revisor_pro.md", "w", encoding="utf-8") as f:
            f.write("Tu és um Revisor de Texto Profissional. Torna o texto claro, elegante e formal.")
    
    return [f for f in os.listdir(pasta) if f.endswith('.md')]

def main():
    console.clear()
    console.print(Panel.fit("💼 [bold]AGENTE DE BOLSO - MULTI-TOOL[/bold] 💼", border_style="blue"))

    api_key = os.getenv('GOOGLE_API_KEY') or Prompt.ask("Chave API", password=True)
    agente_sys = AgenteDeBolso(api_key)

    agentes = carregar_agentes()
    if not agentes:
        console.print("[red]Nenhum agente encontrado em prompts/agentes/[/red]")
        return

    escolha = Select.ask("Escolha o Agente para ativar:", choices=agentes)
    
    with open(f"prompts/agentes/{escolha}", "r", encoding="utf-8") as f:
        instrucao = f.read()

    console.print(f"\n[bold green]Agente {escolha} Ativado![/bold green]")
    
    while True:
        entrada = Prompt.ask("\n[bold]O que devo processar?[/bold] (ou 'sair')")
        if entrada.lower() == 'sair': break
        
        resultado = agente_sys.rodar_agente(instrucao, entrada)
        console.print("\n[bold blue]Resultado:[/bold blue]")
        console.print(Markdown(resultado))
        console.print("—" * 50)

if __name__ == "__main__":
    main()
