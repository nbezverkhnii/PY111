from typing import Hashable, List
import networkx as nx


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an depth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node of search
    :return: list of nodes in the visited order
    """
    was_visited: List[Hashable] = list()
    stack: List[Hashable] = list()
    stack.append(start_node)

    while stack:
        current_value = stack.pop()
        for i in g.neighbors(current_value):
            if i not in was_visited and i not in stack:
                stack.append(i)
        was_visited.append(current_value)

    return was_visited


if __name__ == '__main__':
    graph = nx.Graph()
    graph.add_nodes_from("ABCDEFG")
    graph.add_edges_from([
        ('A', 'B'),
        ('A', 'C'),
        ('B', 'D'),
        ('B', 'E'),
        ('C', 'F'),
        ('E', 'G'),
    ])
    print(dfs(graph, 'A'))
