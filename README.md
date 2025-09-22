# Trees & Graphs — Post‑Class Assignment

Welcome! Clone this repo and complete the **single file** at `src/assignment.py`.  
Then run the provided scripts to verify you’re done.

---

## What to implement

### Solve 5 graph problems (in `src/assignment.py`)
1. **Dijkstra shortest paths** (weighted, non-negative; return dist and parent) — `src/assignment.py:dijkstra`
2. **Minimum Spanning Tree (Kruskal)** using **Union–Find** — `src/assignment.py:kruskal_mst`
3. **Topological order (DAG)** — `src/assignment.py:topo_order_dag`
4. **Shortest paths on a DAG** (relax edges in topo order) — `src/assignment.py:dag_shortest_paths`
5. **Bipartite check** (BFS 2-color) **and/or** **Connected components** — `src/assignment.py:is_bipartite`, `count_components`

### Implement a Trie-based autocomplete
- Build a `Trie` with `insert`, `search`, `starts_with`, and `suggest(prefix, k)` — `src/trie.py`
- See tests in `tests/test_assignment.py` for expected behavior.

> All tests must pass (`python scripts/run_all.py`) to complete the assignment.

---

## How to run (no deps needed)

```bash
# Optional: create a virtual environment
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows PowerShell
# .venv\Scripts\Activate.ps1

# Run everything (tests + README checks)
python scripts/run_all.py
# Or use the convenience scripts:
# macOS/Linux
bash scripts/run_all.sh
# Windows
scripts\run_all.bat
```

The command must end with **"ALL CHECKS PASSED"** to be complete.

---

## Class Questions (fill in below)

Replace each placeholder with 1‑3 sentences.  
The `scripts/check_readme.py` script fails if any placeholder remains.

1. **When do you pick BFS vs DFS?**  
   YOUR ANSWER HERE

2. **Why does BFS find the fewest number of edges (hops) in an unweighted graph?**  
   YOUR ANSWER HERE

3. **Adjacency list vs adjacency matrix — when is each preferable, and what’s the space cost?**  
   YOUR ANSWER HERE

4. **Define the height of a binary tree (edges vs nodes).**  
   YOUR ANSWER HERE

5. **Given the graph**  
   ```
   A: [B, C]
   B: [A, D]
   C: [A, E]
   D: [B, F]
   E: [C]
   F: [D]
   ```  
   **What BFS path from A to F do you reconstruct using the parent map?**  
   YOUR ANSWER HERE

---

## Hints
- Mark nodes **visited at first discovery** to avoid duplicates.
- Keep neighbor order deterministic so tests are reproducible.
- Grid BFS: bounds check, skip walls `#`, don’t revisit cells.

---

## CI (GitHub Actions)

After you push this repo to GitHub, your tests will run automatically on each push and pull request.

**Optional badge** (replace `OWNER` and `REPO` with your GitHub org/user and repository name):

```
[![CI](https://github.com/OWNER/REPO/actions/workflows/ci.yml/badge.svg)](https://github.com/OWNER/REPO/actions/workflows/ci.yml)
```


---

## Test discovery (FYI)
We use unittest discovery so tests under `tests/` are always found:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```
