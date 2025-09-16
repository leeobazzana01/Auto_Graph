#importa a lib
from pyvis.network import Network

#cria a rede
net = Network(notebook=True, cdn_resources="remote")

#adicionando nós
net.add_node(1, label="qo")
net.add_node(2, label="q1")

#adicionando mais nós
net.add_nodes(
    [3,4,5],
    label=["q2", "q3", "q4"],
    color=["#3da831", "#9131a8", "#3155a8"], 
)

# criando arestas
net.add_edge(1, 2, label="0/1", value=2)
net.add_edge(2, 3, label="0/1")
net.add_edges([(2, 4), (3,1)])

#mostrando em um arquivo html
net.show("nodes.html")

