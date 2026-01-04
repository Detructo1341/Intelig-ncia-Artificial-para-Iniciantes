# Padrões de Design de Agentes

## 🎨 Arquiteturas Comprovadas

### Padrão 1: Agente Linear
**Uso**: Tarefas com fluxo fixo

```markdown
## PROCESSO
1. Input → Validação
2. Processamento → Transformação  
3. Output → Formatação
4. Validação → Entrega
```

**Exemplo**: Tradutor, Resumidor, Conversor

### Padrão 2: Agente Iterativo
**Uso**: Refinamento progressivo

```markdown
## CICLO
GERAR → AVALIAR → REFINAR → REPETIR

Critério de parada:
- Qualidade atingida OU
- Máximo de iterações
```

**Exemplo**: Editor, Revisor, Otimizador

### Padrão 3: Agente Ramificado
**Uso**: Decisões baseadas em contexto

```markdown
## FLUXO CONDICIONAL
IF contexto == A:
    → Metodologia 1
ELIF contexto == B:
    → Metodologia 2
ELSE:
    → Metodologia padrão
```

**Exemplo**: Tutor adaptativo, Diagnóstico

### Padrão 4: Agente Modular
**Uso**: Combinar sub-agentes

```markdown
## COMPOSIÇÃO
Agente Mestre:
    → Sub-agente 1 (análise)
    → Sub-agente 2 (síntese)
    → Sub-agente 3 (validação)
```

**Exemplo**: Sistema complexo, Pipeline

### Padrão 5: Agente Metacognitivo
**Uso**: Auto-reflexão e melhoria

```markdown
## META-LOOP
1. Execute tarefa
2. Avalie próprio output
3. Identifique fraquezas
4. Proponha melhorias
5. Re-execute (opcional)
```

**Exemplo**: Auto-crítico, Pesquisador

## 📊 Quando Usar Cada Padrão?

| Padrão | Melhor Para | Evite Se |
|--------|-------------|----------|
| **Linear** | Processos claros e fixos | Precisa adaptação |
| **Iterativo** | Qualidade > velocidade | Tempo limitado |
| **Ramificado** | Múltiplos contextos | Fluxo é sempre igual |
| **Modular** | Sistemas complexos | Tarefa é simples |
| **Metacognitivo** | Máxima qualidade | Recursos limitados |

## 🛠️ Template Universal

```markdown
# [Nome do Agente]

## PADRÃO: [Linear/Iterativo/...]

## IDENTIDADE
[Quem é]

## EXPERTISE  
[O que sabe]

## METODOLOGIA ([PADRÃO ESCOLHIDO])
[Implementação específica do padrão]

## VALIDAÇÃO
[Critérios de qualidade]

## FORMATO
[Como responde]
```

## ➡️ Próximo: [Cap. 7: Especializações](07-especializacoes.md)
