from pyvis.network import Network
import pandas as pd

def cria_transicoes(dataframe):
    transicoes = {}
    for _, row in dataframe.iterrows():
        estado_atual = row['δ']
        transicoes[estado_atual] = {}
        for simbolo in dataframe.columns[1:]:
            destino = row[simbolo]
            if pd.isna(destino) or destino == "_":
                estados_destino = []
            else:
                estados_destino = [s.strip() for s in str(destino).split(',')]
            transicoes[estado_atual][simbolo] = estados_destino
    return transicoes

def cria_arestas(net, transicoes):
    todos_estados = list(transicoes.keys())
    #adicionando nós
    for i, estado in enumerate(todos_estados):
        cor = "#fe0c35" if i == len(todos_estados)-1 else "#0c35fe"
        net.add_node(estado, label=estado, color=cor)
    #adicionando arestas
    for origem, destinos in transicoes.items():
        for simbolo, lista_destinos in destinos.items():
            for destino in lista_destinos:
                net.add_edge(origem, destino, label=str(simbolo))

def main():
    dataframe = pd.read_excel("Autômato.xlsx")
    print("DataFrame lido:\n", dataframe.head())
    net = Network(notebook=True, cdn_resources="remote")
    transicoes = cria_transicoes(dataframe)
    print("Transições estruturadas:\n", transicoes)
    cria_arestas(net, transicoes)
    net.show("nodes.html")
    print("Grafo gerado em nodes.html")

if __name__ == "__main__":
    main()
