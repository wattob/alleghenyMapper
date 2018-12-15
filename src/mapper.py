import matplotlib.pyplot as plt
import networkx as nx
import sys

# Rowan Castellanos, Ben Watto, Nicholas Tocci, Dillon Thoma
# Created using the package networkx
# Documentation found: https://networkx.github.io/documentation/stable/index.html

def showMap(G):
    pos = nx.spring_layout(G)  # positions for all nodes

    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=700)

    # edges
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(data = True),edge_color = "b",width=8)
    # labels
    nx.draw_networkx_labels(G, pos, font_size=5, font_family='sans-serif')

    plt.axis('off')
    plt.show()

def calculatePaths(G, start, end):
    paths = nx.all_simple_paths(G, start, end)
    for path in paths:
        print(path)

def allPathsFromLocationUI(G):
    print("You have selected to find all paths from one location to another. Is this correct (Y or N)")
    print("Please enter (back) at anytime to return to the main menu")
    while(True):
        correct = input(" >> ")
        correct = correct.upper()
        if(correct == "Y"):
            break
        elif(correct == "N"):
            return
        elif(correct == "Back"):
            return
        else:
            print("You have entered a wrong keywoard, please enter a Y or N.")

    while(True):
        print(list(G.nodes))
        startingLocation = input("Where are you starting?\n >> ")
        startingLocation = startingLocation.upper()
        if(startingLocation not in G.nodes):
            print("You have entered a location that is not on the map.")
            print("If you would like to return to the menu, please enter (back).")
            print("Otherwise, please enter a correct location on the map")
        elif(startingLocation in G.nodes):
            print("You have entered the starting location of: ", startingLocation)
            break
        if(startingLocation == "Back"):
            return
    while(True):
        print(list(G.nodes))
        endingLocation = input("What is the end location for your route\n >> ")
        endingLocation = endingLocation.upper()
        if(endingLocation not in G.nodes):
            print("You have entered a location that is not on the map.")
            print("If you would like to return to the menu, please enter (back).")
            print("Otherwise, please enter a correct location on the map")
        elif(endingLocation in G.nodes):
            print("You have entered the starting location of: ", endingLocation)
            break
        if(endingLocation == "Back"):
            return
    calculatePaths(G, startingLocation, endingLocation)

def retrieveMap():
    currentMap = open("../input/alleghenyMap.txt", "r")

    G = nx.DiGraph()
    for line in currentMap:
        mapping = line.split("_")
        start = mapping[0]
        finish = mapping[1]
        weight = float(mapping[2].split("\n")[0])
        G.add_edge(start, finish, weight = weight)
    return G

def calculateShortestPath(G, start, end):
    return(nx.shortest_path(G, start, end))

def shortestPathUI(G):
    print("You have selected to find the shortest path. Is this correct (Y or N)")
    print("Please enter (back) at anytime to return to the main menu")
    while(True):
        correct = input(" >> ")
        correct = correct.upper()
        if(correct == "Y"):
            break
        elif(correct == "N"):
            return
        elif(correct == "Back"):
            return
        else:
            print("You have entered a wrong keywoard, please enter a Y or N.")

    while(True):
        print(list(G.nodes))
        startingLocation = input("Where are you starting?\n >> ")
        startingLocation = startingLocation.upper()
        if(startingLocation not in G.nodes):
            print("You have entered a location that is not on the map.")
            print("If you would like to return to the menu, please enter (back).")
            print("Otherwise, please enter a correct location on the map")
        elif(startingLocation in G.nodes):
            print("You have entered the starting location of: ", startingLocation)
            break
        if(startingLocation == "Back"):
            return
    while(True):
        print(list(G.nodes))
        endingLocation = input("What is the end location for your route\n >> ")
        endingLocation = endingLocation.upper()
        if(endingLocation not in G.nodes):
            print("You have entered a location that is not on the map.")
            print("If you would like to return to the menu, please enter (back).")
            print("Otherwise, please enter a correct location on the map")
        elif(endingLocation in G.nodes):
            print("You have entered the ending location of: ", endingLocation)
            break
        if(endingLocation == "Back"):
            return
    print(calculateShortestPath(G, startingLocation, endingLocation))

def main():
    print("Hello, and welcome to the path-finding map")
    G = retrieveMap()
    exit = False
    print("Would you like to show the map, find the shortest path, or find all paths from one place to another?")
    while(exit != True):
        entry = input("Enter (A) to show the map, (B) for the shortest, (C) to find all paths from one place to another, or (exit) to close the program.\n  >> ")
        entry = entry.upper()
        if(entry == "A"):
            showMap(G)
        elif(entry == "B"):
            shortestPathUI(G)
        elif(entry == "C"):
            allPathsFromLocationUI(G)
        elif(entry == "EXIT"):
            exit = True

if __name__ == "__main__":
    sys.dont_write_bytecode = True
    main()
