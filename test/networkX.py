import json
import networkx as nx
import timeit


def network_x(file_name):
    with open(file_name) as f:
        json_data = json.loads(f.read())

    G = nx.DiGraph()

    G.add_nodes_from(
        int(elem['id'])
        for elem in json_data['Nodes']
    )
    for elem in json_data['Edges']:
        G.add_edge(int(elem['src']), int(elem['dest']), weight=float(elem['w']))

    start = timeit.default_timer()
    p = nx.shortest_path(G, source=1, target=3, weight="weight", method='dijkstra')
    stop = timeit.default_timer()
    print(p)
    print(" run time for shortest path networkx:", stop - start)

    start = timeit.default_timer()
    com = list(nx.strongly_connected_components(G))
    print(com)
    stop = timeit.default_timer()
    print(" run time for strongly connected components networkx:", stop - start)


if __name__ == '__main__':
    network_x('../data/G_30000_240000_2.json')
    # network_x G_30000_240000_2.json algo זמן
    # python G_30000_240000_2.json algo זמן
