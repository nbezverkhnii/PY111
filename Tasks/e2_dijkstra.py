from typing import Hashable, Mapping, Union, Set, Dict, Deque
from collections import deque
import networkx as nx


def dijkstra_algo(g: nx.DiGraph, starting_node: Hashable) -> Mapping[Hashable, Union[int, float]]:
    """
    Count shortest paths from starting node to all nodes of graph g
    :param g: Graph from NetworkX
    :param starting_node: starting node from g
    :return: dict like {'node1': 0, 'node2': 10, '3': 33, ...} with path costs, where nodes are nodes from g
    """

    path_dict: Dict[str: float] = {node: float('inf') for node in g}
    path_dict[starting_node] = 0
    queue: Deque[Hashable] = deque([starting_node])
    visited: Set[Hashable] = set()

    while queue:
        current_node = queue.popleft()
        for neighbor in g.neighbors(current_node):
            new_distance: int = g[current_node][neighbor]['weight'] + path_dict[current_node]
            if new_distance < path_dict[neighbor]:
                path_dict[neighbor] = new_distance
            if current_node not in visited:
                queue.append(neighbor)
        visited.add(current_node)

    return path_dict


if __name__ == '__main__':
    b = nx.DiGraph()
    b.add_nodes_from("ABCDEFG")
    b.add_weighted_edges_from([
        ("A", "B", 1),
        ("B", "C", 3),
        ("C", "E", 4),
        ("E", "F", 3),
        ("B", "E", 8),
        ("C", "D", 1),
        ("D", "E", 2),
        ("B", "D", 2),
        ("G", "D", 1),
        ("D", "A", 2),
    ])

    print(dijkstra_algo(b, 'A'))
