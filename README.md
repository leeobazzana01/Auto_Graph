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

**1. Conceitos Básicos**
    Definição de autômatos finitos (AFD, AFN, ε-AFN), alfabeto, estados, transições.

**2. Identificação de Tipos de Autômatos**
    Critérios para distinguir AFD, AFN e ε-AFN com base na tabela de transições.

**3.Conversões entre Autômatos**

    ε-AFN → AFN: Eliminação de transições vazias (ε-closure).

    AFN → AFD: Algoritmo de construção de subconjuntos.

    Minimização de AFD: Algoritmo de Hopcroft ou partição de estados.

**4. Propriedades e Verificações**

    Checar determinismo, acessibilidade de estados e equivalência entre autômatos.


### Teoria dos Grafos
**1. Fundamentos de Grafos**
    Representação de grafos (matriz de adjacência, lista de adjacências).
    Conceitos de vértices, arestas, direção e pesos (símbolos do autômato).

**2.Algoritmos Relevantes**

    Busca em profundidade (DFS) e largura (BFS) para análise de acessibilidade.

    Componentes fortemente conexos (para minimização de AFD).

    Visualização com Pyvis

    Mapeamento de estados e transições para nós e arestas.

    Customização de layouts e interatividade.