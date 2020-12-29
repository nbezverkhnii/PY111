from typing import Hashable, List
from collections import deque

import networkx as nx
import matplotlib.pyplot as plt


def draw(g: nx.Graph):
    nx.draw(g, with_labels=True)
    plt.show()


def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an breadth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node for search
    :return: list of nodes in the visited order
    """
    was_visited = set()
    queue = deque()
    path = []

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
