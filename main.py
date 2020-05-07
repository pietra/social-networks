from igraph import *

# Graphs

graph = Graph.Read_Ncol("graphs/teste.ncol",names=True,directed=False,weights=True)

# Coloring vertex

# Weight = 5
graph.es["color"] = "black"

# Weight = 1
red_edges = graph.es.select(weight=1)
red_edges["color"] = "red"

# Weight = 2
blue_edges = graph.es.select(weight=2)
blue_edges["color"] = "blue"

# Weight = 3
green_edges = graph.es.select(weight=3)
green_edges["color"] = "green"

# Weight = 4
yellow_edges = graph.es.select(weight=4)
yellow_edges["color"] = "yellow"

# Plot

#print(graph.vs["name"])
#print(graph.es["weight"])
plot(graph, vertex_label=graph.vs["name"])
