import matplotlib.pyplot as plt
import networkx as nx
import sys

# def hidden():
#     # G = nx.Graph()
#     #
#     # G.add_edge('a', 'b', weight=0.6)
#     # G.add_edge('a', 'c', weight=0.2)
#     # G.add_edge('c', 'd', weight=0.1)
#     # G.add_edge('c', 'e', weight=0.7)
#     # G.add_edge('c', 'f', weight=0.9)
#     # G.add_edge('a', 'd', weight=0.3)
#     #
#     # elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 0.5]
#     # esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] <= 0.5]
#     #
#     # pos = nx.spring_layout(G)  # positions for all nodes
#     #
#     # # nodes
#     # nx.draw_networkx_nodes(G, pos, node_size=700)
#     #
#     # # edges
#     # nx.draw_networkx_edges(G, pos, edgelist=elarge,
#     #                        width=6)
#     # nx.draw_networkx_edges(G, pos, edgelist=esmall,
#     #                        width=6, alpha=0.5, edge_color='b', style='dashed')
#     #
#     # # labels
#     # nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
#     #
#     # plt.axis('off')
#     # plt.show()
#     print(hello)
#

def retrieveMap():
    currentMap = open("mapping.txt", "r")

    G = nx.DiGraph()
    for line in currentMap:
        mapping = line.split("_")
        start = mapping[0]
        finish = mapping[1]
        weight = float(mapping[2].split("\n")[0])
        G.add_edge(start, finish, weight = weight)
    # elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 0.2]
    # esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] <= 0.3]
    #
    # pos = nx.spring_layout(G)  # positions for all nodes
    #
    # # nodes
    # nx.draw_networkx_nodes(G, pos, node_size=700)
    #
    # # edges
    # nx.draw_networkx_edges(G, pos, edgelist=elarge,edge_color = "r",
    #                        width=6)
    # nx.draw_networkx_edges(G, pos, edgelist=esmall,
    #                        width=6, alpha=0.5, edge_color='b', style='dashed')
    #
    # # labels
    # nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
    #
    # plt.axis('off')
    # plt.show()
    return G

def main():
    print("Hello, and welcome to the path-finding map")
    G = retrieveMap()
    exit = False
    print("Would you like to list all paths of the graph, find the shortest path, or find all paths from one place?")
    while(exit != True):
        entry = input("Enter (A) for all paths, (B) for the shortest, (C) to find all paths from one place, or (exit) to close the program.\n  >> ")
        if(entry == "A"):
            allPaths(G)
        elif(entry == "B"):
            print("You have selected to find the shortest paths.")
            print(list(G.nodes))
            startingLocation = input(" Where are you starting")
            shortestPath(G)
        elif(entry == "exit"):
            exit = True

if __name__ == "__main__":
    sys.dont_write_bytecode = True
    main()
