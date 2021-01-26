from typing import Hashable, List, Set, Deque
from collections import deque

import networkx as nx


def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an breadth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node for search
    :return: list of nodes in the visited order
    """
    was_visited: Set[Hashable] = set()
    queue: Deque[Hashable] = deque()
    path: List[Hashable] = []
    queue.append(start_node)

    while queue:
        current_node = queue.popleft()
        was_visited.add(current_node)
        if current_node not in path:
            path.append(current_node)
        for neighbor in g.neighbors(current_node):
            if neighbor not in was_visited and neighbor not in queue:
                queue.append(neighbor)

    return path


if __name__ == '__main__':
    graph = nx.Graph()
    graph.add_nodes_from("ABCDEFGHIJ")
    graph.add_edges_from([
        ('A', 'B'),
        ('A', 'F'),
        ('B', 'G'),
        ('F', 'G'),
        ('G', 'C'),
        ('G', 'H'),
        ('G', 'I'),
        ('C', 'H'),
        ('I', 'H'),
        ('H', 'D'),
        ('H', 'E'),
        ('H', 'J'),
        ('E', 'D'),
    ])
    print(bfs(graph, 'A'))