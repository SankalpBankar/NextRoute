import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import copy
import pandas as pd
import time

st.set_page_config(page_title="Distance Vector Routing Simulator", layout="wide")

# Helper functions

def parse_edges_text(text):
    """
    Parses user input edges into a list of tuples.
    Example Input:
        A B 4
        A C 2
        B C 5
    Returns:
        [('A','B',4), ('A','C',2), ('B','C',5)]
    """
    edges = []
    for line in text.strip().splitlines():
        parts = line.split()
        if len(parts) == 3:
            u, v, w = parts
            try:
                edges.append((u, v, float(w)))
            except ValueError:
                st.warning(f"Invalid weight on line: {line}")
        else:
            st.warning(f"Invalid line format: {line}")
    return edges


def initialize_routing_table(nodes, edges):
    """
    Initialize routing table for each node.
    Distance to itself = 0, neighbors = edge weight, others = infinity.
    """
    INF = float("inf")
    routing_table = {node: {dest: INF for dest in nodes} for node in nodes}
    next_hop = {node: {dest: None for dest in nodes} for node in nodes}

    for node in nodes:
        routing_table[node][node] = 0
        next_hop[node][node] = node

    for u, v, w in edges:
        routing_table[u][v] = w
        routing_table[v][u] = w
        next_hop[u][v] = v
        next_hop[v][u] = u

    return routing_table, next_hop


def distance_vector_update(routing_table, next_hop, nodes, edges):
    """
    Perform the distance vector algorithm until convergence.
    Returns list of routing tables at each step.
    """
    history = []
    INF = float("inf")
    step = 0
    updated = True

    while updated:
        updated = False
        snapshot = copy.deepcopy(routing_table)
        history.append(snapshot)
        step += 1

        for u in nodes:
            for v in nodes:
                for w in nodes:
                    if routing_table[u][w] + routing_table[w][v] < routing_table[u][v]:
                        routing_table[u][v] = routing_table[u][w] + routing_table[w][v]
                        next_hop[u][v] = next_hop[u][w]
                        updated = True

    history.append(copy.deepcopy(routing_table))
    return history


def visualize_graph(edges, routing_table):
    """
    Draws the network graph with current shortest paths.
    """
    G = nx.Graph()
    for u, v, w in edges:
        G.add_edge(u, v, weight=w)

    pos = nx.spring_layout(G, seed=42)
    edge_labels = nx.get_edge_attributes(G, "weight")

    plt.figure(figsize=(5, 4))
    nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=2000, font_weight="bold")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    st.pyplot(plt)

# Streamlit UI

st.title("🛰️ Distance Vector Routing Algorithm Simulator")
st.markdown("Simulate how routers exchange routing information using the **Distance Vector Algorithm**.")

with st.sidebar:
    st.header("Network Input")
    edges_text = st.text_area(
        "Enter edges (Format: Node1 Node2 Weight):",
        value="A B 4\nA C 2\nB C 5\nB D 10\nC D 3"
    )
    run_button = st.button("Run Simulation 🚀")

# Main Execution
if run_button:
    edges = parse_edges_text(edges_text)
    nodes = sorted(set([u for u, v, _ in edges] + [v for u, v, _ in edges]))

    routing_table, next_hop = initialize_routing_table(nodes, edges)

    st.subheader("Network Topology")
    visualize_graph(edges, routing_table)

    st.subheader("Simulation Steps")

    history = distance_vector_update(copy.deepcopy(routing_table), copy.deepcopy(next_hop), nodes, edges)

    for step, table in enumerate(history):
        st.markdown(f"### Step {step + 1}")
        df_main = pd.DataFrame(table).T

        # ✅ FIXED: format only numeric columns to avoid ValueError
        st.dataframe(df_main.style.format(
            {col: "{:.1f}" for col in df_main.select_dtypes(include="number").columns},
            na_rep="∞"
        ))

        time.sleep(0.3)

    st.success("✅ Simulation complete! Routing tables have converged.")
else:
    st.info("Enter edges and click **Run Simulation 🚀** to begin.")

