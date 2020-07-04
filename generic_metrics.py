from igraph import *
import sys

movies = ["capita_marvel",
            "catwoman",
            "elektra",
            "enrolados",
            "frozen",
            "mulan",
            "mulher_maravilha",
            "shrek_cintia",
            "shrek2",
            "valente_cintia"]

total_red = 0
total_blue = 0
total_green = 0
total_yellow = 0
total_black = 0

total_vertices = 0

for movie in movies:
    graph = Graph.Read_Ncol("graphs/"+movie+".ncol", names=True,directed=False,weights=True)

    red_edges = len(graph.es.select(weight=1))
    blue_edges = len(graph.es.select(weight=2))
    green_edges = len(graph.es.select(weight=3))
    yellow_edges = len(graph.es.select(weight=4))
    black_edges = len(graph.es.select(weight=5))
    total = len(graph.es)
    vertices = len(graph.vs)

    print("------------------------------------------------")
    print(f"Filme: {movie}")
    print(f"Vertices: {vertices}")
    print(f"Tipo 1: {red_edges} \t Tipo 2: {blue_edges} \t Tipo 3: {green_edges} \t Tipo 4: {yellow_edges} \t Tipo 5: {black_edges} \t Total: {total}")
    print(f"Tipo 1: {red_edges/total*100:.2f}% \t Tipo 2: {blue_edges/total*100:.2f}% \t Tipo 3: {green_edges/total*100:.2f}% \t Tipo 4: {yellow_edges/total*100:.2f}% \t Tipo 5: {black_edges/total*100:.2f}%")

    total_red += red_edges
    total_blue += blue_edges
    total_green += green_edges
    total_yellow += yellow_edges
    total_black += black_edges

    total_vertices += vertices

total = total_black + total_blue + total_green + total_red + total_yellow
print(f"================Total================")
print(f"Vertices: {total_vertices}")
print(f"Tipo 1: {total_red} \t Tipo 2: {total_blue} \t Tipo 3: {total_green} \t Tipo 4: {total_yellow} \t Tipo 5: {total_black} \t Total: {total}")
print(f"Tipo 1: {total_red/total*100:.2f} \t Tipo 2: {total_blue/total*100:.2f} \t Tipo 3: {total_green/total*100:.2f} \t Tipo 4: {total_yellow/total*100:.2f} \t Tipo 5: {total_black/total*100:.2f}")