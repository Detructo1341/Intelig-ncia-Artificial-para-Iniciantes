#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🤖 Coach de Fluência em IA - Bot Inteligente com Google Gemini
Versão Python com integração completa do Gemini AI
"""

import google.generativeai as genai
import os
from datetime import datetime

# ============================================================================
# CONFIGURAÇÃO INICIAL
# ============================================================================

def configurar_gemini(api_key):
    """Configura a API do Gemini com sua chave"""
    try:
        genai.configure(api_key=api_key)
        
        # Listar modelos disponíveis
        print("\n📋 Modelos disponíveis com generateContent:")
        modelos_disponiveis = []
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                modelos_disponiveis.append(m.name)
                print(f"   ✓ {m.name}")
        
        if not modelos_disponiveis:
            print("   ❌ Nenhum modelo disponível!")
            return None
        
        return True
    except Exception as e:
        print(f"❌ Erro ao configurar Gemini: {e}")
        return False

# ============================================================================
# SYSTEM PROMPT DO COACH
# ============================================================================

SYSTEM_PROMPT = """Você é um Coach de Fluência em Inteligência Artificial.

Sua missão: Ajudar profissionais a desenvolver pensamento estratégico sobre IA.

Framework dos 4Ds:
1. DISCERNIMENTO - Avaliar quando, por quê, para quem usar IA
   • É apropriada tecnicamente?
   • Há implicações éticas?
   • Alinha com meu propósito?

2. DESCRIÇÃO - Comunicar claramente com IA
   • Objetivo específico
   • Contexto relevante
   • Passos claros
   • Persona/role
   • Exemplo desejado
   • Background necessário
   • Limitações
   • Critério de sucesso

3. DELEGAÇÃO - Decidir o que delegar e o que manter humano
   • Exige julgamento ético? → NÃO delegue
   • Requer expertise único? → delegue parcial
   • É repetitivo/processual? → delegue
   • Posso auditar depois? → OK
   • Risco aceitável? → cuide

4. DILIGÊNCIA - Garantir ética e responsabilidade
   • Transparência com stakeholders
   • Validação de outputs
   • Documentação de decisões
   • Monitoramento de impacto

Seu Estilo:
- Ouça com empatia genuína
- Questione premissas gentilmente mas firmemente
- Ofereça framework dos 4Ds quando relevante
- Desafie suposições implícitas
- Valorize honestidade e reflexão profunda
- Reconheça trade-offs complexos
- NUNCA ofereça "respostas certas" - convide reflexão
- Conecte com contexto específico
- Aponte consequências não-óbvias
- Estimule pensamento crítico

Responda em português brasileiro, tom acessível mas rigoroso."""

# ============================================================================
# FUNÇÃO PRINCIPAL DO BOT
# ============================================================================

def executar_bot(api_key):
    """Executa o chatbot com Gemini"""
    
    # Configura Gemini
    if not configurar_gemini(api_key):
        return
    
    # Cria modelo e inicia chat
    try:
        model = genai.GenerativeModel(
            model_name='gemini-pro',
            system_instruction=SYSTEM_PROMPT
        )
        chat = model.start_chat(history=[])
    except Exception as e:
        print(f"❌ Erro ao criar modelo: {e}")
        return
    
    # ========================================================================
    # INTERFACE DO BOT
    # ========================================================================
    
    # Banner de boas-vindas
    titulo = "# 🤖 Coach de Fluência em IA - Gemini Edition #"
    print("\n" + len(titulo) * "#")
    print(titulo)
    print(len(titulo) * "#")
    print("\n✨ Bem-vindo ao seu Coach de Fluência em IA!")
    print("🔌 Conectado com Google Gemini AI")
    print("📚 Framework dos 4Ds integrado")
    print("💡 Respostas inteligentes e estratégicas")
    print("\n" + "=" * 60)
    print("Exemplos de perguntas:")
    print("  • O que é fluência em IA?")
    print("  • Como aplicar os 4Ds no meu trabalho?")
    print("  • Qual é o maior dilema ético em IA?")
    print("  • Como detectar viés em algoritmos?")
    print("  • Sou [sua profissão], como usar IA eticamente?")
    print("=" * 60)
    print("\n💬 Digite 'sair' para encerrar")
    print("📝 Digite 'salvar' para salvar conversa")
    print("")
    
    # Histórico para salvar conversa
    historico_conversa = []
    
    # ========================================================================
    # LOOP DO CHAT
    # ========================================================================
    
    while True:
        try:
            # Input do usuário
            print("\n" + "-" * 60)
            texto = input("🗣️  Sua pergunta: ").strip()
            
            if not texto:
                print("⚠️  Por favor, digite algo!")
                continue
            
            # Comando: sair
            if texto.lower() == 'sair':
                print("\n🤖 Obrigado por usar o Coach de Fluência em IA!")
                print("📚 Continue refletindo sobre como usar IA estrategicamente.")
                break
            
            # Comando: salvar
            if texto.lower() == 'salvar':
                salvar_conversa(historico_conversa)
                continue
            
            # Mostra loading
            print("\n🤖 Coach está pensando", end="", flush=True)
            
            # Envia mensagem para Gemini
            response = chat.send_message(texto)
            
            # Extrai resposta
            resposta = response.text
            
            # Mostra resposta
            print("\r" + " " * 30 + "\r", end="")  # Limpa "pensando"
            print(f"\n📖 Coach:\n{resposta}")
            
            # Salva no histórico
            historico_conversa.append({
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'usuario': texto,
                'coach': resposta
            })
            
        except KeyboardInterrupt:
            print("\n\n⏸️  Chat interrompido pelo usuário.")
            break
        except Exception as e:
            print(f"\n❌ Erro ao processar mensagem: {e}")
            print("💡 Dica: Verifique sua chave API e conexão com internet.")
            continue

# ============================================================================
# FUNÇÕES AUXILIARES
# ============================================================================

def salvar_conversa(historico):
    """Salva o histórico da conversa em arquivo"""
    if not historico:
        print("⚠️  Nenhuma conversa para salvar!")
        return
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"conversa_fluencia_{timestamp}.txt"
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("=" * 80 + "\n")
            f.write("CONVERSA COM COACH DE FLUÊNCIA EM IA\n")
            f.write(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
            f.write("=" * 80 + "\n\n")
            
            for msg in historico:
                f.write(f"[{msg['timestamp']}]\n")
                f.write(f"👤 Você: {msg['usuario']}\n")
                f.write(f"🤖 Coach: {msg['coach']}\n")
                f.write("-" * 80 + "\n\n")
        
        print(f"✅ Conversa salva em: {filename}")
    except Exception as e:
        print(f"❌ Erro ao salvar: {e}")

def obter_api_key():
    """Obtém a chave API do usuário"""
    print("\n" + "=" * 60)
    print("🔑 CONFIGURAÇÃO DA API GEMINI")
    print("=" * 60)
    print("\nVocê precisa de uma chave API do Google Gemini.")
    print("📌 Para obter:")
    print("   1. Vá para: https://ai.google.dev")
    print("   2. Clique 'Get API Key'")
    print("   3. Crie um projeto no Google AI Studio")
    print("   4. Copie a chave API\n")
    
    # Tenta obter do ambiente primeiro
    api_key = os.getenv('GOOGLE_API_KEY')
    
    if api_key:
        print(f"✅ Chave API encontrada em variável de ambiente!")
        return api_key
    
    # Se não tiver, pede ao usuário
    api_key = input("Cole sua chave API (sk-...): ").strip()
    
    if not api_key:
        print("❌ Chave API é obrigatória!")
        return None
    
    return api_key

# ============================================================================
# MAIN
# ============================================================================

def main():
    """Função principal"""
    print("\n" + "=" * 60)
    print("🤖 COACH DE FLUÊNCIA EM IA - COM GOOGLE GEMINI")
    print("=" * 60)
    
    # Obtém chave API
    api_key = obter_api_key()
    
    if not api_key:
        print("❌ Não foi possível obter a chave API.")
        print("📌 Defina a variável de ambiente GOOGLE_API_KEY ou")
        print("   forneça a chave manualmente ao executar o script.")
        return
    
    # Executa bot
    executar_bot(api_key)
    
    print("\n" + "=" * 60)
    print("Obrigado por usar o Coach de Fluência em IA!")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    main()
