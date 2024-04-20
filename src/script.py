import networkx as nx
def load_edge_list(file_path):
    edges = []
    with open(file_path, 'r') as file:
        for line in file:
            edge = line.strip().split('\t')
            edges.append((int(edge[0]), int(edge[1])))
    return edges
def create_network_from_edge_list(file_path):
    edges = load_edge_list(file_path)
    G = nx.DiGraph()
    G.add_edges_from(edges)
    return G
file_path = 'ownership.txt' 
network = create_network_from_edge_list(file_path)
print(network)
nx.clustering(network)
nx.density(network)
len(nx.dominating_set(network))
import networkx as nx
import plotly.graph_objects as go

def plot_degree_dist(G):
    degrees = [G.degree(n) for n in G.nodes()]
    degree_counts = {}
    for degree in degrees:
        if degree in degree_counts:
            degree_counts[degree] += 1
        else:
            degree_counts[degree] = 1

    degrees, counts = zip(*sorted(degree_counts.items()))
    fig = go.Figure(data=[go.Bar(x=degrees, y=counts, marker=dict(color='red'))])
    fig.update_layout(
        title='Distribución de Ex-grado',
        xaxis=dict(title='Ex-grado'),
        yaxis=dict(title='Frecuencia'),
        autosize=False,
        width=800,
        height=500
    )
    fig.show()


plot_degree_dist(network)
import networkx as nx
import plotly.graph_objects as go

def plot_degree_dist(G):
    degrees = [G.degree(n) for n in G.nodes()]
    degree_counts = {}
    for degree in degrees:
        if degree in degree_counts:
            degree_counts[degree] += 1
        else:
            degree_counts[degree] = 1

    degrees, counts = zip(*sorted(degree_counts.items()))
    fig = go.Figure(data=[go.Bar(x=degrees, y=counts)])
    fig.update_layout(
        title='Distribución de Ex-grado',
        xaxis=dict(title='Ex-grado'),
        yaxis=dict(title='Frecuencia (escala logarítmica)', type='log'),
        autosize=False,
        width=800,
        height=500
    )
    fig.show()

plot_degree_dist(network)
max_value_key = max(nx.out_degree_centrality(network), key=nx.out_degree_centrality(network).get)
print("Llave con mayor centralidad de Ex-grado:", max_value_key)
max_value_key = max(nx.eigenvector_centrality(network), key=nx.eigenvector_centrality(network).get)
print("Llave con mayor centralidad de Eigenvector:", max_value_key)
max_value_key = max(nx.katz_centrality(network), key=nx.katz_centrality(network).get)
print("Llave con mayor centralidad de Katz:", max_value_key)
max_value_key = max(nx.closeness_centrality(network), key=nx.closeness_centrality(network).get)
print("Llave con mayor centralidad de Intermediación:", max_value_key)
Lambda=sum([nx.degree_histogram(network)[z]*z for z in range(1,len(nx.degree_histogram(network)))])/ len(nx.degree_histogram(network))
print(Lambda)