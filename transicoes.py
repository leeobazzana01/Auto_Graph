import pandas as pd
from pyvis.network import Network

#função que cria transições a partir de um dataframe
def cria_transicoes(dataframe):
    #inicializando um dicionário de transições vazio
    transicoes = {}

    #itera sobre todas as linhas do dataframe criando um dicionário
    for _, row in dataframe.iterrows():
        #a coluna δ ccontém os estados 
        estado_atual = row['δ']
        transicoes[estado_atual] = {}

        #tratamento para casos que a transição resulta em nada
        for simbolo in dataframe.columns[1:]:
            destino = row[simbolo]
            if pd.isna(destino) or destino == "_":
                estados_destino = []
            else:
                estados_destino = [s.strip() for s in str(destino).split(',')]
            transicoes[estado_atual][simbolo] = estados_destino
    return transicoes