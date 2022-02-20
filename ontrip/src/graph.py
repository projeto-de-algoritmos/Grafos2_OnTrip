from math import inf
from dataclasses import dataclass, field
from queue import Queue
from typing import List, Optional


@dataclass
class Graph:
    """
    This class implements the Graph structure in python
    """
    edges: List[tuple[str, str , int]]
    graph: Optional[dict] = field(default_factory=dict)

    def init_graph(self) -> None:
        """
        Created the graph dict struct with source and destination airports
        """
        for x, y, _ in self.edges:
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

    def dijkstra(self, start):
        nodes = self.get_nodes()
        distances = {}
        adjacents = {n: {} for n in nodes}

        for first, second, distance in self.edges:
            distances[first] = (inf, None)
            distances[second] = (inf, None)
            adjacents.setdefault(first, dict())[second] = distance
            adjacents.setdefault(second, dict())[first] = distance
        distances[start] = (0, start)

        temporary_nodes = [n for n in nodes]
        while len(temporary_nodes) > 0:
            upper_bounds = {n: distances[n] for n in temporary_nodes}
            lower_bound = min(upper_bounds, key=lambda v: upper_bounds.get(v)[0])
            temporary_nodes.remove(lower_bound)

            for node, distance in adjacents[lower_bound].items():
                new_distance = (distances[lower_bound][0] + distance, lower_bound)
                distances[node] = min(distances[node], new_distance, key=lambda v:v[0])

        return distances

    # def find_shortest_path(self, start, end):
    #     dijkstra_dict = self.dijkstra(start=start)
    #     path = list()

    #     end_tuple = dijkstra_dict.get(end)
    #     while end_tuple[1] != start