from src.GraphAlgo import GraphAlgo
import timeit


def python(file_name):
    algo = GraphAlgo()
    algo.load_from_json(file_name)

    start = timeit.default_timer()
    p = algo.shortest_path(1, 3)
    stop = timeit.default_timer()
    print(p)
    print(" run time for shortest path python:", stop - start)

    start = timeit.default_timer()
    com = algo.connected_components()
    print(com)
    stop = timeit.default_timer()
    print(" run time for strongly connected components python:", stop - start)

    start = timeit.default_timer()
    com = algo.connected_component(1)
    print(com)
    stop = timeit.default_timer()
    print(" run time for connected_component python:", stop - start)


if __name__ == '__main__':
    python('../data/G_30000_240000_2.json')
