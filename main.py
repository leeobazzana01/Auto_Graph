from pyvis.network import Network
import pandas as pd

def cria_transicoes(dataframe):
    #criando o dicionário de transições
    transicoes = {}

    for _, row in dataframe.iterrows():
        estado_atual = row['δ']  
        transicoes[estado_atual] = {}

        for simbolo in dataframe.columns[1:]:  # colunas 0,1,ε
            destino = row[simbolo]

            #celulas vazias ou '-'
            if pd.isna(destino) or destino == "_":
                estados_destino = []
            else:
                estados_destino = [s.strip() for s in str(destino).split(',')]

            transicoes[estado_atual][simbolo] = estados_destino

    return transicoes

def cria_arestas(net, transicoes):
    #adicionando arestas no grafo
    #adicionando nós
    todos_estados = set(transicoes.keys())
    for estado in todos_estados:
        net.add_node(estado, label=estado, color="#3da831")  # cor opcional
        
    for origem, destinos in transicoes.items():
        for simbolo, lista_destinos in destinos.items():
            for destino in lista_destinos:
                #caso nós n existam
                if origem not in todos_estados:
                    net.add_node(origem, label=origem)
                    todos_estados.add(origem)
                if destino not in todos_estados:
                    net.add_node(destino, label=destino)
                    todos_estados.add(destino)
                #aresta c rótulo do símbolo
                net.add_edge(origem, destino, label=simbolo)


def main():
    #lendo excel
    dataframe = pd.read_excel("Autômato.xlsx")
    print("DataFrame lido:\n", dataframe.head())

    #criando a rede
    net = Network(notebook=True, cdn_resources="remote")

    #criando dict
    transicoes = cria_transicoes(dataframe)
    print("Transições estruturadas:\n", transicoes)

    #adicionando nos
    cria_arestas(net, transicoes)

    #mostrando em html
    net.show("nodes.html")
    print("Grafo gerado em nodes.html")


if __name__ == "__main__":
    main()
