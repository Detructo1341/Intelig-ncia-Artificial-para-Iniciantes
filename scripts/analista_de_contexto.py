#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
👁️‍🗨️ Analista de Contexto Multimodal com Gemini 3 Flash
Analisa imagens, PDFs e texto, gerando insights claros para iniciantes.
"""

import os
import google.generativeai as genai
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.prompt import Prompt
from rich.spinner import Spinner

# Necessário para processar PDF (instale com `pip install pypdf`)
try:
    from pypdf import PdfReader
except ImportError:
    PdfReader = None
    print("⚠️  Aviso: 'pypdf' não está instalado. Análise de PDF não disponível. Instale com 'pip install pypdf'")

# Configuração da Interface
console = Console()

# ============================================================================
# SYSTEM PROMPT (A Mente do Analista)
# ============================================================================
SYSTEM_PROMPT = """Você é um Analista de Contexto Multimodal para Iniciantes em IA.
Sua missão: Receber um conteúdo (texto, imagem, PDF) e extrair os pontos mais importantes, explicando de forma didática e acionável.
Foque nos seguintes pontos:
1.  **Resumo Essencial:** O que é o conteúdo em poucas palavras.
2.  **Pontos Chave:** Quais são as ideias principais ou elementos visuais importantes.
3.  **Implicações Práticas:** Como um iniciante em IA pode usar essa informação ou o que ela significa para um projeto.
4.  **Próximos Passos Sugeridos:** O que o usuário pode fazer a seguir com base nessa análise.

Se for imagem, descreva o que vê e qual o possível contexto.
Se for texto/PDF, sintetize as ideias centrais.

Seu Estilo: Didático, objetivo, encorajador e sem jargões desnecessários."""

# ============================================================================
# LÓGICA DO ANALISTA
# ============================================================================

class AnalistaMultimodal:
    def __init__(self, api_key):
        try:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel(
                model_name='gemini-3-flash', # Usando o modelo mais recente e poderoso
                system_instruction=SYSTEM_PROMPT
            )
            self.historico = [] # Manter histórico de análises para possível salvamento
            console.print("[bold green]✅ Analista Multimodal (Gemini 3 Flash) Ativado![/bold green]")
        except Exception as e:
            console.print(f"[bold red]❌ Erro na configuração do Analista:[/bold red] {e}")

    def _extrair_texto_pdf(self, path_pdf):
        """Extrai texto de um arquivo PDF."""
        if not PdfReader:
            console.print("[bold red]❌ pypdf não instalado. Não é possível ler PDFs.[/bold red]")
            return None
        try:
            reader = PdfReader(path_pdf)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or "" # Garante que não adicione None
            return text
        except Exception as e:
            console.print(f"[bold red]❌ Erro ao ler PDF:[/bold red] {e}")
            return None

    def analisar(self, caminho_arquivo, pergunta_adicional=""):
        partes = []
        tipo_conteudo = ""

        if not os.path.exists(caminho_arquivo):
            console.print(f"[bold red]❌ Arquivo não encontrado: {caminho_arquivo}[/bold red]")
            return "Arquivo não encontrado."

        if caminho_arquivo.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
            tipo_conteudo = "imagem"
            partes.append(genai.upload_file(caminho_arquivo))
            console.print(f"[bold yellow]🖼️ Carregando imagem:[/bold yellow] {caminho_arquivo}")
        elif caminho_arquivo.lower().endswith('.pdf'):
            tipo_conteudo = "PDF"
            console.print(f"[bold yellow]📄 Lendo PDF:[/bold yellow] {caminho_arquivo}")
            pdf_text = self._extrair_texto_pdf(caminho_arquivo)
            if pdf_text:
                partes.append(pdf_text)
            else:
                return "Falha ao extrair texto do PDF."
        elif caminho_arquivo.lower().endswith(('.txt', '.md', '.log', '.csv')): # Adicione outros tipos de texto se quiser
            tipo_conteudo = "texto"
            try:
                with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                    partes.append(f.read())
                console.print(f"[bold yellow]📝 Lendo arquivo de texto:[/bold yellow] {caminho_arquivo}")
            except Exception as e:
                console.print(f"[bold red]❌ Erro ao ler arquivo de texto:[/bold red] {e}")
                return "Falha ao ler arquivo de texto."
        else:
            return f"Tipo de arquivo '{os.path.splitext(caminho_arquivo)[1]}' não suportado ainda. Tente imagem, PDF ou texto."

        # O prompt que direciona o Gemini
        prompt_final = f"Analise este conteúdo ({tipo_conteudo}). {pergunta_adicional}"
        partes.insert(0, prompt_final) # Adiciona o prompt no início das partes

        with console.status("[bold green]🧠 Analisando com Gemini 3 Flash...[/bold green]", spinner="dots"):
            try:
                response = self.model.generate_content(partes)
                return response.text
            except Exception as e:
                return f"[bold red]❌ Erro na API do Gemini:[/bold red] {e}"

# ============================================================================
# INTERFACE PRINCIPAL
# ============================================================================

def exibir_status_sistema():
    data_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    modelo_ativo = "Gemini 3 Flash (v. Dez/2025)"
    
    console.print(Panel(
        f"📅 [bold]Data do Sistema:[/bold] {data_atual}\n"
        f"🧠 [bold]Modelo Ativo:[/bold] {modelo_ativo}\n"
        f"🌐 [bold]Status:[/bold] [green]Conectado à Fronteira da IA Multimodal[/green]",
        title="[bold blue]SYSTEM CHECK[/bold blue]",
        border_style="cyan"
    ))

def main():
    console.clear()
    exibir_status_sistema()

    console.print(Panel.fit(
        "👁️‍🗨️ [bold yellow]ANALISTA DE CONTEXTO MULTIMODAL[/bold yellow] 👁️‍🗨️\n[italic]Entenda qualquer conteúdo com o Gemini 3 Flash[/italic]",
        border_style="gold"
    ))

    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        api_key = Prompt.ask("[bold yellow]Insira sua Gemini API Key[/bold yellow]", password=True)

    if not api_key:
        console.print("[red]❌ Chave API é necessária para iniciar o Analista.[/red]")
        return

    analista = AnalistaMultimodal(api_key)

    while True:
        caminho_arquivo = Prompt.ask("\n[bold green]📁 Caminho do arquivo para analisar[/bold green] (ex: 'imagem.png', 'doc.pdf', 'texto.txt' ou 'sair')")

        if caminho_arquivo.lower() == 'sair':
            console.print("[italic]Encerrando o Analista... Até a próxima descoberta, Gabriel![/italic]")
            break
        
        if not caminho_arquivo:
            console.print("[yellow]⚠️ Por favor, insira um caminho de arquivo válido.[/yellow]")
            continue

        pergunta_adicional = Prompt.ask("[bold magenta]❓ Pergunta adicional (opcional)[/bold magenta] (ex: 'Quais os riscos aqui?', 'Como otimizar?')", default="")

        resultado_analise = analista.analisar(caminho_arquivo, pergunta_adicional)
        
        console.print("\n[bold gold]✨ Análise do Analista Multimodal:[/bold gold]")
        console.print(Markdown(resultado_analise))
        console.print("=" * 60)

if __name__ == "__main__":
    main()
