# Trees & Graphs — Post‑Class Assignment

Welcome! Clone this repo and complete the **single file** at `src/assignment.py`.  
Then run the provided scripts to verify you’re done.

---

## What to implement (in `src/assignment.py`)

1. **Breadth‑First Search (`bfs`)**  
   Returns `(order, parent)` where `order` is the visitation order and `parent` maps a node to its discoverer.

2. **Reconstruct Path (`reconstruct_path`)**  
   Given `parent`, `start`, `goal`, return the path `start → ... → goal` (list). If unreachable, return `[]`.

3. **Depth‑First Search (`dfs`)**  
   Return visitation order using depth‑first search.

4. **Binary Tree utilities (`height`, `preorder`, `inorder`, `postorder`)**  
   Height is measured in **edges**: a leaf has height `0`.

5. **Mini‑application A: `shortest_path_length`**  
   BFS on a grid (4‑direction moves) to return the fewest steps from `S` to `T` or `-1` if unreachable.

6. **Mini‑application B: `distance_two`**  
   Friend‑of‑friend: return the set of nodes at **exactly distance 2** from `person` in an undirected graph,
   excluding `person` and direct friends.

> You can implement both mini‑apps; tests expect at least these functions to work.

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

Replace each `YOUR ANSWER HERE` with 1‑3 sentences.  
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

## License
MIT


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
