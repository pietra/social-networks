from igraph import *
import sys
import ast

# Graphs
film = sys.argv[1]

graph = Graph.Read_Ncol("graphs/"+film+".ncol", names=True,directed=False,weights=True)

# Adding gender to vertices
genders_file = open("gender/"+film+".txt", "r")

for line in genders_file:
    line = line.replace("\n", "").split(" ")
    vertex = graph.vs.find(name=line[0])
    vertex["gender"] = line[1]

# Coloring edges
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

# Coloring vertices
color_dict = {"M": "green", "F": "orange"}
graph.vs["color"] = [color_dict[gender] for gender in graph.vs["gender"]]

# Plot
#print(graph.es["weight"])
plot(graph, vertex_label=graph.vs["name"])
