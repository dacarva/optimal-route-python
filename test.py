import unittest
import main

train_adj = {'A': ['B'], 'B': ['A', 'C'], 'C': ['B', 'D', 'G'], 'D': ['C', 'E'], 'E': [
    'D', 'F'], 'F': ['E', 'I'], 'G': ['C', 'H'], 'H': ['G', 'I'], 'I': ['H', 'F']}

express_stations = {'G': ['Green'], 'H': ['Red'], 'I': ['Green']}


class TestingPaths(unittest.TestCase):

    def setUp(self):
        pass

    # Check the number of express stations
    def test_express_stations_number(self):
        self.assertEqual(len(main.get_express_trains(express_stations)), 2)

    # Checks the number of nodes without express stations
    def test_path_without_express_stations(self):
        node_a = 'A'
        node_b = 'E'
        path = main.get_path(node_a, node_b, train_adj, express_stations)
        print('The path', path)
        self.assertEqual(len(path), 5)

    def test_path_with_red_express_stations(self):
        node_a = 'A'
        node_b = 'F'
        express_train = 'Red'
        path = main.get_path(node_a, node_b, train_adj,
                             express_stations, express_train)
        self.assertEqual(len(path), 6)
        print('The path', path)

    def test_path_with_green_express_stations(self):
        node_a = 'A'
        node_b = 'F'
        express_train = 'Green'
        path = main.get_path(node_a, node_b, train_adj,
                             express_stations, express_train)
        self.assertEqual(len(path), 5)
        print('The path', path)


if __name__ == '__main__':
    unittest.main()
