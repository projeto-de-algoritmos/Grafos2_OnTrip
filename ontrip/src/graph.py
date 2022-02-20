from dataclasses import dataclass, field
from queue import Queue
from typing import List, Optional


@dataclass
class Graph:
    """
    This class implements the Graph structure in python
    """
    edges: List[tuple[str, str]]
    graph: Optional[dict] = field(default_factory=dict)

    def init_graph(self) -> None:
        """
        Created the graph dict struct with source and destination airports
        """
        for x, y in self.edges:
            self.graph.setdefault(x, list()).append(y)

    def get_edges(self) -> List[tuple[str, str]]:
        """
        Returns all airports edges connections on graph structure
        """
        return self.edges

    def get_nodes(self) -> List[str]:
        """
        Returns all airports names
        """
        return list(self.graph.keys())

    def get_graph(self) -> dict:
        """
        Returns the graph dict
        """
        return self.graph

    def bfs(self, start: str, end: str): 
        """
        Makes a BFS search on the graph
        """
        visited = {}
        parent = {}
        level = {}
        shortest_path = list()
        queue = Queue()

        if start == end:
            return [end]

        for node in self.graph.keys():
            visited[node] = False
            parent[node] = None
            level[node] = -1

        visited[start] = True
        level[start] = 0
        queue.put(start)

        while not queue.empty():
            node = queue.get()
            shortest_path.append(node)

            for neighbour in self.graph.get(node, []):
                if self.graph.get(neighbour) and not visited[neighbour]:
                    visited[neighbour] = True
                    parent[neighbour] = node
                    level[neighbour] = level[node] + 1
                    queue.put(neighbour)

        path = list()
        while end is not None:
            path.append(end)
            end = parent[end]
        path.reverse()

        if len(path) == 1:
            return None
        return path