import unittest
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
class TestGraphAlgo(unittest.TestCase):

    def setUp(self) -> None:
        self.graph=DiGraph()


    def test_connect_component_and_components(self):
        for x in range(4):
            self.assertTrue(self.graph.add_node(x))

        self.assertTrue(self.graph.add_edge(0,1,5))
        self.assertTrue(self.graph.add_edge(1, 2, 5))
        self.assertTrue(self.graph.add_edge(2, 0, 5))

        algo = GraphAlgo(self.graph)
        self.assertEqual([0,1,2],algo.connected_component(0))
        self.assertEqual([1,2,0], algo.connected_component(1))
        self.assertEqual([2,0,1], algo.connected_component(2))
        self.assertEqual([3], algo.connected_component(3))
        self.assertEqual([[3], [0, 1, 2]],algo.connected_components())


    def test_load_save(self):
        algo=GraphAlgo()
        self.assertTrue(algo.load_from_json('../data/T0.JSON'))

        self.assertEqual(algo.get_graph().v_size(),4)
        self.assertEqual(algo.get_graph().e_size(), 5)

        self.assertTrue(algo.save_to_json('../data/Test.json'))

        self.assertTrue(algo.load_from_json('../data/Test.JSON'))

        self.assertEqual(algo.get_graph().v_size(),4)
        self.assertEqual(algo.get_graph().e_size(), 5)

        self.assertFalse(algo.load_from_json('../data/Test1'))

    def test_shortest_oath(self):
        algo=GraphAlgo()
        self.assertTrue(algo.load_from_json('../data/T0.JSON'))

        path=algo.shortest_path(0, 3)
        self.assertEqual(path[0], 2.8)
        self.assertEqual(path[1], [0, 1, 3])

    def test_plot(self):
        algo=GraphAlgo()
        self.assertTrue(algo.load_from_json('../data/T0.JSON'))
        algo.plot_graph()

if __name__ == '__main__':
    unittest.main()