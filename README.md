# Autômatos, Grafos e Python

A Fundamentação Teórica do projeto está na união de três áreas de conhecimento fundamentais de Matemática e Computação:
**-Teoria da Computação e Linguagens Formais**
**-Teoria dos Grafos**
**-Programação e manipulação de Dados com Python**

## Funcionamento

O Objetivo é, ao final do projeto, obter um software onde: o usuário insira o Autômato, o software realize o processamento do Autômato, mostrando qual o tipo e dando mais detalhes. A partir da identificação, desenvolveremos os Algoritmos de conversão do Autômato, a fim de obter sempre o Autômato Determinístico Mínimo.

## Conceitos Teóricos

### Python

**1. Fundamentos**
    Sintaxe básica 
    Estruturas de controle (if, for, while) 
    Funções.

**2. Manipulação de estruturas de dados**
    Listas 
    Dicionários 
    Tuplas 
    Conjuntos.

**3. Bibliotecas Específicas**
    Pandas: Leitura e manipulação de arquivos Excel (.xlsx), operações com DataFrames.
    Pyvis: Criação e customização de grafos interativos.

**4. Programação Orientada a Objetos**
    Classes e objetos para representar autômatos (ex: classe Automaton com estados, transições).
    Processamento de Dados
    Técnicas para limpar e estruturar dados de transições e estados.

### Teoria dos Autômatos

**1. Fundamentos**

    Definições: alfabeto, estados, transições, estado inicial, estados finais.

    Autômato Finito Determinístico (AFD).

    Autômato Finito Não Determinístico (AFN).

    AFN com transições vazias (ε-AFN).

**2. Operações e Conversões**

    ε-AFN → AFN (eliminação de ε-transições, ε-fecho).

    AFN → AFD (construção do conjunto de estados).

    Minimização de AFD (algoritmo de partição, Hopcroft).

**3. Propriedades**

    Identificação do tipo de autômato (determinístico, não determinístico, com ε).

    Acessibilidade de estados (alcançáveis ou mortos).

    Equivalência entre autômatos.
### Teoria dos Grafos
**1. Fundamentos**

    Vértices e arestas.

    Grafos direcionados e ponderados.

    Representações: matriz de adjacência, lista de adjacência.

**2. Algoritmos**

    Busca em largura (BFS).

    Busca em profundidade (DFS).

    Componentes conexos (importante para simplificação).

**Aplicação**

    Modelar estados como nós e transições como arestas.

    Analisar conectividade e minimizar grafos.

    Visualizar com pyvis.


## Projeto: Roadmap

**1. Estrutura Inicial**

1. Definir estrutura de entrada

    Leitura do arquivo .xlsx contendo estados, alfabeto, transições, estado inicial e finais.

    Normalizar o formato interno dos dados (ex.: dicionário ou classe Automato).

2. Criar representação do autômato

    Estrutura de dados para armazenar:

    Conjunto de estados

    Alfabeto

    Função de transição

    Estado inicial

    Estados finais

**2. Identificação**

1. Implementar verificação do tipo de autômato

    Verificar presença de transições vazias (ε) → se existir → ε-AFN.

    Verificar múltiplas transições para o mesmo símbolo a partir de um estado → AFN.

    Caso cada par (estado, símbolo) leve a exatamente um destino → AFD.

**3. Conversões**

1. Implementar conversão ε-AFN → AFN

    Construir ε-fecho dos estados.

    Reescrever tabela de transições eliminando movimentos vazios.

2. Implementar conversão AFN → AFD

    Algoritmo do conjunto de estados (subconjuntos).

    Produzir nova tabela determinística.

3. Implementar minimização de AFD

    Eliminar estados inalcançáveis.

    Agrupar estados equivalentes.

    Gerar AFD mínimo.

**4. Visualização**

1. Gerar visualização do autômato

    Usar biblioteca de grafos para desenhar:

        Estados como nós.

        Transições como arestas (com rótulo do símbolo).

        Estado inicial com destaque.

        Estados finais com estilo diferenciado.

2. Visualizar versões diferentes

    Autômato original (do .xlsx).

    Conversões (ε-AFN → AFN → AFD → AFD mínimo).

**5. Integração**

1. Integrar fluxo completo

    Entrada: arquivo .xlsx.

    Identificação do tipo de autômato.

    Conversões automáticas conforme necessário.

    Saída: visualizações interativas de cada versão.

2. Adicionar testes e validação

    Casos simples de cada tipo de autômato.

    Casos maiores para validar escalabilidade.

3. Empacotamento do projeto

    Criar interface de linha de comando (CLI) ou interface gráfica simples.

    Documentar uso (exemplo: python automato.py arquivo.xlsx).
