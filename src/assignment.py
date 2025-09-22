"""
Extra graph problems for the post-class work:
- Dijkstra shortest paths (non-negative edge weights)
- Kruskal's Minimum Spanning Tree (MST) using Union-Find
- Topological order (DAG) and DAG shortest paths
- Bipartite check (BFS 2-coloring)
- Connected components count (undirected)
"""

from typing import Dict, List, Tuple, Any, Optional, Set
import heapq
from collections import deque

# ----- Dijkstra -----
def dijkstra(adj: Dict[Any, List[Tuple[Any, int]]], start: Any) -> Tuple[Dict[Any, int], Dict[Any, Any]]:
    """
    Input: adjacency list with weights: node -> list of (neighbor, weight).
    Return: (dist, parent) where dist[v] is the minimum total cost from start to v,
    and parent maps v -> previous node on a shortest path. Assumes non-negative weights.
    """
    # TODO: implement (use a min-heap / priority queue)
    return {}, {}

# ----- Union-Find (Disjoint Set) -----
class UnionFind:
    def __init__(self, items: Optional[List[Any]] = None):
        self.parent = {}
        self.rank = {}
        if items:
            for x in items:
                self.parent[x] = x
                self.rank[x] = 0

    def find(self, x: Any) -> Any:
        # TODO: implement path compression
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
        return x

    def union(self, a: Any, b: Any) -> bool:
        """
        Union by rank. Return True if merged (were different), False if already in same set.
        """
        # TODO: implement
        return False

# ----- Kruskal's MST -----
def kruskal_mst(vertices: List[Any], edges: List[Tuple[int, Any, Any]]) -> List[Tuple[int, Any, Any]]:
    """
    vertices: list of nodes
    edges: list of edges as (weight, u, v)
    Return: list of edges in the MST (same (w,u,v) format), not necessarily unique ordering.
    Assumes the graph is connected; if not, returns a Minimum Spanning Forest.
    """
    # TODO: implement using UnionFind
    return []

# ----- Topological order (DAG) -----
def topo_order_dag(adj: Dict[Any, List[Any]]) -> List[Any]:
    """
    Kahn's algorithm (in-degree) or DFS finishing times.
    Return a list of nodes in topological order.
    Raise ValueError if a cycle is detected.
    """
    # TODO: implement
    return []

def dag_shortest_paths(adj_w: Dict[Any, List[Tuple[Any, int]]], start: Any) -> Tuple[Dict[Any, int], Dict[Any, Any]]:
    """
    Shortest paths on a DAG with (non-negative/any) weights using topological order.
    Return (dist, parent) like Dijkstra.
    """
    # TODO: implement
    return {}, {}

# ----- Bipartite check -----
def is_bipartite(adj: Dict[Any, List[Any]]) -> bool:
    """
    BFS 2-coloring on each component. Return True if bipartite, else False.
    """
    # TODO: implement
    return False

# ----- Connected components count -----
def count_components(adj: Dict[Any, List[Any]]) -> int:
    """
    Treat as undirected. Return the number of connected components.
    """
    # TODO: implement
    return 0