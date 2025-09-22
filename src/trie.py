"""
Trie (prefix tree) for autocomplete.
Implement:
- insert(word)
- search(word) -> bool
- starts_with(prefix) -> bool
- suggest(prefix, k) -> List[str] (return up to k words with the given prefix; lexicographic order is fine)
"""

from typing import Dict, List

class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.end: bool = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # TODO: implement
        pass

    def search(self, word: str) -> bool:
        # TODO: implement
        return False

    def starts_with(self, prefix: str) -> bool:
        # TODO: implement
        return False

    def suggest(self, prefix: str, k: int) -> List[str]:
        # TODO: implement (DFS from prefix node; collect up to k)
        return []
