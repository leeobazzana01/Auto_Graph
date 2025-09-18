import pandas as pd
from pyvis.network import Network

#função que cria as arestas a partir da rede e transições
def cria_arestas(net, transicoes):
    todos_estados = list(transicoes.keys())
    #adicionando nós
    for i, estado in enumerate(todos_estados):
        cor = "#fe0c35" if i == len(todos_estados)-1 else "#0c35fe" #se o estado for o final, será vermelho
        net.add_node(estado, label=estado, color=cor)
    #adicionando arestas
    for origem, destinos in transicoes.items():
        for simbolo, lista_destinos in destinos.items():
            for destino in lista_destinos:
                net.add_edge(origem, destino, label=str(simbolo))