import unittest
from src.DiGraph import DiGraph
class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.g = DiGraph()

    def test_add_node(self):
        for x in range(1,6):
            self.assertTrue(self.g.add_node(x))
        for x in range(1,6):
            self.assertFalse(self.g.add_node(x))
        self.assertEqual(5,self.g.get_mc())
        self.assertEqual(5, self.g.v_size())
        self.assertEqual(0, self.g.e_size())

    def test_v_size(self):
        self.assertTrue(self.g.add_node(1))
        self.assertFalse(self.g.add_node(1))
        self.assertFalse(self.g.add_node(1))
        self.assertFalse(self.g.add_node(1))
        self.assertTrue(self.g.add_node(2))
        self.assertTrue(self.g.remove_node(2))
        self.assertFalse(self.g.remove_node(2))
        self.assertTrue(self.g.add_node(2))
        self.assertTrue(self.g.add_node(3))

        self.assertEqual(self.g.v_size(),3)

    def test_e_size(self):
        for x in range(6):
            self.assertTrue(self.g.add_node(x))

        for x in range(0,6,2):
            self.assertTrue(self.g.add_edge(x,x+1,7))
        self.assertEqual(self.g.get_mc(),9)
        self.assertEqual(self.g.e_size(),3)

        self.assertFalse(self.g.add_edge(0,1,6))
        self.assertFalse(self.g.add_edge(0,10,6))
        self.assertFalse(self.g.add_edge(10,10,6))
        self.assertFalse(self.g.add_edge(1,1,6))
        self.assertFalse(self.g.add_edge(10,0,6))

        self.assertFalse(self.g.add_edge(1, 0, -1))
        self.assertTrue(self.g.add_edge(1, 0, 1))


    def test_get_mc(self):
        for x in range(6):
            self.assertTrue(self.g.add_node(x))

        for x in range(0, 6, 2):
            self.assertTrue(self.g.add_edge(x, x + 1, 7))
        self.assertEqual(self.g.get_mc(), 9)
        self.assertEqual(self.g.e_size(), 3)

        self.assertFalse(self.g.add_edge(0, 1, 6))
        self.assertFalse(self.g.add_edge(0, 10, 6))
        self.assertFalse(self.g.add_edge(10, 10, 6))
        self.assertFalse(self.g.add_edge(1, 1, 6))
        self.assertFalse(self.g.add_edge(10, 0, 6))

        self.assertFalse(self.g.add_edge(1, 0, -1))
        self.assertTrue(self.g.add_edge(1, 0, 1))

        self.assertEqual(self.g.get_mc(), 10)

    def test_add_edge(self):
        for x in range(6):
            self.assertTrue(self.g.add_node(x))

        for x in range(0, 6, 2):
            self.assertTrue(self.g.add_edge(x, x + 1, 7))
        self.assertEqual(self.g.get_mc(), 9)
        self.assertEqual(self.g.e_size(), 3)

        self.assertFalse(self.g.add_edge(0, 1, 6))
        self.assertFalse(self.g.add_edge(0, 10, 6))
        self.assertFalse(self.g.add_edge(10, 10, 6))
        self.assertFalse(self.g.add_edge(1, 1, 6))
        self.assertFalse(self.g.add_edge(10, 0, 6))

        self.assertFalse(self.g.add_edge(1, 0, -1))
        self.assertTrue(self.g.add_edge(1, 0, 1))
        self.assertEqual(self.g.e_size(), 4)

        for x in range(6,10):
            self.assertTrue(self.g.add_node(x))
        for x in range(6,10, 2):
            self.assertTrue(self.g.add_edge(x, x + 1, 7))

        self.assertEqual(self.g.e_size(), 6)


    def test_remove_node(self):
        for x in range(6):
            self.assertTrue(self.g.add_node(x))

        for x in range(0, 6, 2):
            self.assertTrue(self.g.add_edge(x, x + 1, 7))
        self.assertEqual(self.g.get_mc(), 9)
        self.assertEqual(self.g.e_size(), 3)

        self.assertFalse(self.g.add_edge(0, 1, 6))
        self.assertFalse(self.g.add_edge(0, 10, 6))
        self.assertFalse(self.g.add_edge(10, 10, 6))
        self.assertFalse(self.g.add_edge(1, 1, 6))
        self.assertFalse(self.g.add_edge(10, 0, 6))

        self.assertFalse(self.g.add_edge(1, 0, -1))
        self.assertTrue(self.g.add_edge(1, 0, 1))
        self.assertEqual(self.g.e_size(), 4)

        for x in range(6, 10):
            self.assertTrue(self.g.add_node(x))
        for x in range(6, 10, 2):
            self.assertTrue(self.g.add_edge(x, x + 1, 7))

        self.assertEqual(self.g.e_size(), 6)

        self.assertEqual(self.g.v_size(),10)

        self.assertTrue(self.g.remove_node(1))

        self.assertEqual(self.g.e_size(), 4)

        self.assertEqual(self.g.v_size(), 9)

        self.assertFalse(self.g.remove_node(1))

    def test_remove_edge(self):
        for x in range(6):
            self.assertTrue(self.g.add_node(x))

        for x in range(0, 6, 2):
            self.assertTrue(self.g.add_edge(x, x + 1, 7))
        self.assertEqual(self.g.get_mc(), 9)
        self.assertEqual(self.g.e_size(), 3)

        self.assertFalse(self.g.add_edge(0, 1, 6))
        self.assertFalse(self.g.add_edge(0, 10, 6))
        self.assertFalse(self.g.add_edge(10, 10, 6))
        self.assertFalse(self.g.add_edge(1, 1, 6))
        self.assertFalse(self.g.add_edge(10, 0, 6))

        self.assertFalse(self.g.add_edge(1, 0, -1))
        self.assertTrue(self.g.add_edge(1, 0, 1))
        self.assertEqual(self.g.e_size(), 4)

        for x in range(6, 10):
            self.assertTrue(self.g.add_node(x))
        for x in range(6, 10, 2):
            self.assertTrue(self.g.add_edge(x, x + 1, 7))

        self.assertEqual(self.g.e_size(), 6)

        for x in range(0, 6, 2):
            self.assertTrue(self.g.remove_edge(x, x + 1))

        for x in range(6, 10, 2):
            self.assertTrue(self.g.remove_edge(x, x + 1))

        self.assertEqual(self.g.e_size(), 1)


    def test_get_all_v(self):
        for x in range(6):
            self.assertTrue(self.g.add_node(x))

        for x in range(0, 6, 2):
            self.assertTrue(self.g.add_edge(x, x + 1, 7))
        self.assertEqual(self.g.get_mc(), 9)
        self.assertEqual(self.g.e_size(), 3)

        self.assertFalse(self.g.add_edge(0, 1, 6))
        self.assertFalse(self.g.add_edge(0, 10, 6))
        self.assertFalse(self.g.add_edge(10, 10, 6))
        self.assertFalse(self.g.add_edge(1, 1, 6))
        self.assertFalse(self.g.add_edge(10, 0, 6))

        self.assertFalse(self.g.add_edge(1, 0, -1))
        self.assertTrue(self.g.add_edge(1, 0, 1))
        self.assertEqual(self.g.e_size(), 4)

        for x in range(6, 10):
            self.assertTrue(self.g.add_node(x))
        for x in range(6, 10, 2):
            self.assertTrue(self.g.add_edge(x, x + 1, 7))

        self.assertEqual(self.g.e_size(), 6)

        self.assertEqual(self.g.v_size(), 10)

        self.assertTrue(self.g.remove_node(1))

        self.assertEqual(self.g.e_size(), 4)

        self.assertEqual(self.g.v_size(), 9)

        self.assertFalse(self.g.remove_node(1))

        i=0
        for x in self.g.get_all_v().keys():
            if i!=1:
                self.assertEqual(i,x)
            else:
                i += 1
            i += 1


    def test_all_in_edges_of_node(self):
        for x in range(10):
            self.assertTrue(self.g.add_node(x))
        for x in range(1,10):
            self.assertTrue(self.g.add_edge(x,0,7))
        self.assertEqual(self.g.e_size(),9)
        i = 1
        for x in self.g.all_in_edges_of_node(0):
            self.assertEqual(x, i)
            i+=1
        for x in range(1,10):
            self.assertEqual( self.g.all_in_edges_of_node(x),dict())

    def test_all_out_edges_of_node(self):

        for x in range(10):
            self.assertTrue(self.g.add_node(x))
        for x in range(1,10):
            self.assertTrue(self.g.add_edge(0,x,7))
        self.assertEqual(self.g.e_size(),9)
        i = 1
        for x in self.g.all_out_edges_of_node(0):
            self.assertEqual(x, i)
            i+=1
        for x in range(1,10):
            self.assertEqual( self.g.all_out_edges_of_node(x),dict())

if __name__ == '__main__':
    unittest.main()