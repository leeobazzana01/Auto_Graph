#importando as bibliotecas e frameworks
from pyvis.network import Network
import pandas as pd
from transicoes import cria_transicoes
from arestas import cria_arestas

def main():
    #lendo o dataset
    dataframe = pd.read_excel("Autômato.xlsx")

    #mostrando o dataset
    print("DataFrame lido:\n", dataframe.head())

    #importando as redes do framework
    net = Network(notebook=True, cdn_resources="remote")

    #criando transições
    transicoes = cria_transicoes(dataframe)
    
    #mostrando transições criadas
    print("Transições estruturadas:\n", transicoes)
    
    #criando arestas
    cria_arestas(net, transicoes)

    #exibindo o resultado
    net.show("nodes.html")

if __name__ == "__main__":
    main()
