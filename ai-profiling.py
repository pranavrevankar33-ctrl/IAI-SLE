import time
from collections import deque
 
INITIAL_STATE = (1, 2, 3, 4, 0, 5, 6, 7, 8)
GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 0)
 
 
def get_neighbors(state):
    neighbors = []
    idx = state.index(0)
    row, col = divmod(idx, 3)
 
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in moves:
        r, c = row + dr, col + dc
        if 0 <= r < 3 and 0 <= c < 3:
            new_idx = r * 3 + c
            state_list = list(state)
            state_list[idx], state_list[new_idx] = state_list[new_idx], state_list[idx]
            neighbors.append(tuple(state_list))
    return neighbors
 
 
def solve_bfs(start, goal):
    queue = deque([start])
    visited = {start}
    nodes_expanded = 0
 
    while queue:
        current = queue.popleft()
        nodes_expanded += 1
 
        if current == goal:
            return nodes_expanded
 
        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
 
    return nodes_expanded
 
 
def solve_dfs(start, goal):
    stack = [start]
    visited = {start}
    nodes_expanded = 0
 
    while stack:
        current = stack.pop()
        nodes_expanded += 1
 
        if current == goal:
            return nodes_expanded
 
        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
 
    return nodes_expanded
 
 
def run_experiments():
    bfs_times, dfs_times = [], []
 
    for _ in range(3):
        start_t = time.perf_counter()
        bfs_nodes = solve_bfs(INITIAL_STATE, GOAL_STATE)
        bfs_times.append((time.perf_counter() - start_t) * 1000)
 
        start_t = time.perf_counter()
        dfs_nodes = solve_dfs(INITIAL_STATE, GOAL_STATE)
        dfs_times.append((time.perf_counter() - start_t) * 1000)
 
    avg_bfs_time = sum(bfs_times) / len(bfs_times)
    avg_dfs_time = sum(dfs_times) / len(dfs_times)
 
    print("\n" + "=" * 50)
    print("SLE-2 PROFILING RESULTS (8-PUZZLE)")
    print("=" * 50)
    print(f"BFS Avg Time    : {avg_bfs_time:.3f} ms")
    print(f"BFS Nodes       : {bfs_nodes}")
    print(f"DFS Avg Time    : {avg_dfs_time:.3f} ms")
    print(f"DFS Nodes       : {dfs_nodes}")
    print("=" * 50)
 
 
if __name__ == "__main__":
    run_experiments()
 
