import unittest

from src.assignment import (
    bfs, reconstruct_path, dfs,
    Node, height, preorder, inorder, postorder,
    shortest_path_length, distance_two
)

class TestGraphsTrees(unittest.TestCase):
    def setUp(self):
        # Deterministic neighbor order
        self.graph = {
            'A': ['B', 'C'],
            'B': ['A', 'D'],
            'C': ['A', 'E'],
            'D': ['B', 'F'],
            'E': ['C'],
            'F': ['D'],
        }

    def test_bfs_and_path(self):
        order, parent = bfs(self.graph, 'A')
        self.assertEqual(order, ['A', 'B', 'C', 'D', 'E', 'F'])
        path = reconstruct_path(parent, 'A', 'F')
        self.assertEqual(path, ['A', 'B', 'D', 'F'])

    def test_dfs(self):
        order = dfs(self.graph, 'A')
        self.assertEqual(order, ['A', 'B', 'D', 'F', 'C', 'E'])

    def test_tree_utils(self):
        #       4
        #      / \
        #     2   6
        #    / \   \
        #   1   3   7
        n1 = Node(1); n3 = Node(3); n7 = Node(7)
        n2 = Node(2, n1, n3)
        n6 = Node(6, None, n7)
        root = Node(4, n2, n6)
        self.assertEqual(height(root), 2)  # edges
        self.assertEqual(preorder(root), [4, 2, 1, 3, 6, 7])
        self.assertEqual(inorder(root),  [1, 2, 3, 4, 6, 7])
        self.assertEqual(postorder(root),[1, 3, 2, 7, 6, 4])

    def test_maze_and_friends(self):
        grid = [
            "S..#.",
            ".#.#.",
            "..#..",
            "#....",
            "...#T",
        ]
        self.assertEqual(shortest_path_length(grid), 8)

        g = {
            'P': ['A', 'B'],
            'A': ['P', 'C'],
            'B': ['P', 'D'],
            'C': ['A'],
            'D': ['B', 'E'],
            'E': ['D'],
        }
        self.assertEqual(distance_two(g, 'P'), {'C', 'D'})

if __name__ == "__main__":
    unittest.main()
