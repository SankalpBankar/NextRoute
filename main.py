import copy
import time
import networkx as nx
import matplotlib.pyplot as plt
from prettytable import PrettyTable

# Define the network graph 
graph = {
    'A': {'B': 2, 'D': 5},
    'B': {'A': 2, 'C': 3, 'E': 3},
    'C': {'B': 3, 'E': 2},
    'D': {'A': 5, 'E': 2},
    'E': {'B': 3, 'C': 2, 'D': 2}
}

# Initialize routing tables
def initialize_tables(graph):
    routing_tables = {}
    for router in graph:
        table = {}
        for dest in graph:
            if router == dest:
                table[dest] = (router, 0)
            elif dest in graph[router]:
                table[dest] = (dest, graph[router][dest])
            else:
                table[dest] = (None, float('inf'))
        routing_tables[router] = table
    return routing_tables

# Distance vector update
def update_tables(graph, routing_tables):
    updated = False
    new_tables = copy.deepcopy(routing_tables)

    for router in graph:
        for neighbor in graph[router]:
            for dest in graph:
                new_cost = graph[router][neighbor] + routing_tables[neighbor][dest][1]
                if new_cost < new_tables[router][dest][1]:
                    new_tables[router][dest] = (neighbor, new_cost)
                    updated = True
    return new_tables, updated

# Print routing tables
def print_routing_tables(routing_tables, title="Routing Tables"):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)
    for router, table in routing_tables.items():
        t = PrettyTable(["Destination", "Next Hop", "Cost"])
        for dest, (nexthop, cost) in table.items():
            cost_display = "∞" if cost == float('inf') else cost
            t.add_row([dest, nexthop if nexthop else "-", cost_display])
        print(f"\nRouter {router}:\n{t}")

# Visualize the network graph
def visualize_graph(graph, routing_tables, iteration):
    G = nx.Graph()
    for node in graph:
        for neighbor, cost in graph[node].items():
            G.add_edge(node, neighbor, weight=cost)

    pos = nx.spring_layout(G, seed=42)
    edge_labels = nx.get_edge_attributes(G, 'weight')

    plt.clf()
    nx.draw_networkx_nodes(G, pos, node_size=1000, node_color="#add8e6")
    nx.draw_networkx_edges(G, pos, width=2)
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight="bold")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

    plt.title(f"Distance Vector Routing — Iteration {iteration}")
    plt.pause(1)  # Pause to show updates visually

# Main simulation
def distance_vector_routing(graph):
    routing_tables = initialize_tables(graph)
    print_routing_tables(routing_tables, "Initial Routing Tables")
    visualize_graph(graph, routing_tables, 0)

    iteration = 0
    while True:
        iteration += 1
        routing_tables, updated = update_tables(graph, routing_tables)
        print_routing_tables(routing_tables, f"After Iteration {iteration}")
        visualize_graph(graph, routing_tables, iteration)
        if not updated:
            break

    print("\n✅ Network converged — Final Routing Tables shown above.")
    plt.title("✅ Network Converged — Final Routing Topology")
    plt.show()

# Run
if __name__ == "__main__":
    plt.ion()  # interactive mode for live updates
    distance_vector_routing(graph)
