from typing import Callable

def find_dfs_way(g_adj : Callable[[int], list[int]], v0 : int, v1 : int) -> list[int]:
    visited = set()
    path = []

    def dfs(v: int) -> bool:
        if v == v1:
            path.append(v)
            return True
        visited.add(v)
        path.append(v)
        for u in g_adj(v):
            if u not in visited:
                if dfs(u):
                    return True
        path.pop()
        return False
    if dfs(v0):
        return path  
    return []