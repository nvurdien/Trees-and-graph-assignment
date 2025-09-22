import unittest

from src.assignment import (
    dijkstra, kruskal_mst, topo_order_dag, dag_shortest_paths,
    is_bipartite, count_components
)
from src.trie import Trie

class TestExtraGraphs(unittest.TestCase):
    def test_dijkstra_small(self):
        g = {
            'A': [('B', 2), ('C', 5)],
            'B': [('D', 2)],
            'C': [('D', 1)],
            'D': [],
        }
        dist, parent = dijkstra(g, 'A')
        # Expected after implementation
        self.assertIsInstance(dist, dict)
        self.assertIsInstance(parent, dict)

    def test_kruskal_mst(self):
        V = ['A','B','C','D']
        E = [
            (1,'A','B'),
            (4,'B','C'),
            (1,'C','D'),
            (3,'A','D'),
            (2,'B','D'),
        ]
        mst = kruskal_mst(V, E)
        self.assertIsInstance(mst, list)

    def test_topo_and_dag_shortest(self):
        adj = {
            'A': ['B','D'],
            'B': ['C'],
            'C': ['E'],
            'D': ['E'],
            'E': [],
        }
        order = topo_order_dag(adj)
        self.assertIsInstance(order, list)
        adj_w = {
            'A': [('B',1), ('D',4)],
            'B': [('C',1)],
            'C': [('E',1)],
            'D': [('E',1)],
            'E': [],
        }
        dist, parent = dag_shortest_paths(adj_w, 'A')
        self.assertIsInstance(dist, dict)
        self.assertIsInstance(parent, dict)

    def test_bipartite_and_components(self):
        g = {
            1: [2],
            2: [1,3],
            3: [2,4],
            4: [3],
        }
        _ = is_bipartite(g)
        _ = count_components(g)

class TestTrie(unittest.TestCase):
    def test_trie_basic(self):
        t = Trie()
        for w in ["to", "tea", "ten", "in", "inn"]:
            t.insert(w)
        _ = t.search("to")
        _ = t.starts_with("te")
        _ = t.suggest("te", k=3)

if __name__ == "__main__":
    unittest.main()