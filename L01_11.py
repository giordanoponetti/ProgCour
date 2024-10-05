import matplotlib.pyplot as plt
import networkx as nx
G = nx.Graph()

G.add_edge("Enrico", "Python")
G.add_edge("Claudia", "Python")
G.add_edge("Claudia", "R")
G.add_edge("Nico", "Python")
G.add_edge("Nico", "C++")
G.add_edge("Daniel", "Matlab")
G.add_edge("Daniel", "C++")
G.add_edge("Alessandra", "Matlab")
G.add_edge("Alessandra", "Python")

print(nx.shortest_path(G, "R", "C++"))


# Draw the graph
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_color='black', edge_color='gray')
plt.show()