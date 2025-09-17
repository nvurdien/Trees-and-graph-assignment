"""
Complete these functions. Keep neighbor order deterministic (use the given lists).
Height is measured in **edges**: a leaf has height 0.
"""

from collections import deque
from typing import Dict, List, Any, Tuple, Optional, Set

# ---------- Part 1: Graph traversals ----------

def bfs(graph: Dict[Any, List[Any]], start: Any) -> Tuple[List[Any], Dict[Any, Any]]:
    """
    Breadth-first search.
    Return (order, parent).
    - order: visitation order
    - parent: map child -> parent used to reconstruct a fewest-hop path
    """
    # TODO: implement
    order: List[Any] = []
    parent: Dict[Any, Any] = {}
    return order, parent

def reconstruct_path(parent: Dict[Any, Any], start: Any, goal: Any) -> List[Any]:
    """
    Rebuild the path from start to goal using the parent map.
    Return [] if goal is unreachable.
    """
    # TODO: implement
    return []

def dfs(graph: Dict[Any, List[Any]], start: Any) -> List[Any]:
    """
    Depth-first search (recursive or iterative). Return visitation order.
    """
    # TODO: implement
    return []

# ---------- Part 2: Binary tree utilities ----------

class Node:
    def __init__(self, value: Any, left: Optional["Node"]=None, right: Optional["Node"]=None):
        self.value = value
        self.left = left
        self.right = right

def height(root: Optional[Node]) -> int:
    """
    Number of edges on the longest root-to-leaf path.
    A leaf has height 0; an empty tree may be defined as -1.
    """
    # TODO: implement
    return -1

def preorder(root: Optional[Node]) -> List[Any]:
    """Pre-order: Node, Left, Right."""
    # TODO: implement
    return []

def inorder(root: Optional[Node]) -> List[Any]:
    """In-order: Left, Node, Right."""
    # TODO: implement
    return []

def postorder(root: Optional[Node]) -> List[Any]:
    """Post-order: Left, Right, Node."""
    # TODO: implement
    return []

# ---------- Part 3: Mini-apps ----------

def shortest_path_length(grid: List[str]) -> int:
    """
    BFS on a grid (4-direction moves). Return fewest steps from 'S' to 'T' or -1 if unreachable.
    The grid is a list of equal-length strings using: '#', '.', 'S', 'T'.
    """
    # TODO: implement
    return -1

def distance_two(graph: Dict[Any, List[Any]], person: Any) -> Set[Any]:
    """
    Return the set of nodes at exactly distance 2 from `person`, excluding `person` and direct friends.
    Treat the graph as undirected.
    """
    # TODO: implement
    return set()
