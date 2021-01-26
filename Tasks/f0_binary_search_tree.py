"""
You can do it either with networkx ('cause tree is a graph)
or with dicts (smth like {'key': 0, value: 123, 'left': {...}, 'right':{...}})
"""
import math
from typing import Any, Optional, Tuple, Dict
# import networkx as nx
bts: Dict = {}


def insert(key: int, value: Any) -> None:
    """
    Insert (key, value) pair to binary search tree

    :param key: key from pair (key is used for positioning node in the tree)
    :param value: value associated with key
    :return: None
    """
    if not bts:
        bts[0] = {'key': key, 'value': value}
        bts[1] = {}
        bts[2] = {}
    else:
        for index in bts:
            if bts[index] and (key > bts[index]['key'] and not bts[2 * index + 2]):
                bts[2 * index + 2] = {'key': key, 'value': value}
                bts[2 * (2 * index + 2) + 1] = {}
                bts[2 * (2 * index + 2) + 2] = {}
                break
            elif bts[index] and (key < bts[index]['key'] and not bts[2 * index + 1]):
                bts[2 * index + 1] = {'key': key, 'value': value}
                bts[2 * (2 * index + 1) + 1] = {}
                bts[2 * (2 * index + 1) + 2] = {}
                break


def remove(key: int) -> Optional[Tuple[int, Any]]:
    """
    Remove key and associated value from the BST if exists

    :param key: key to be removed
    :return: deleted (key, value) pair or None
    """
    root = 0
    h_tree = int(math.log2(len(bts) + 1))
    for _ in range(h_tree):
        if bts[root] and bts[root]['key'] == key:
            bts[root] = {}
            break
        elif bts[root] and key > bts[root]['key']:
            root = 2 * root + 2
        elif bts[root] and key < bts[root]['key']:
            root = 2 * root + 1


def find(key: int) -> Optional[Any]:
    """
    Find value by given key in the BST

    :param key: key for search in the BST
    :return: value associated with the corresponding key
    """
    root = 0
    h_tree = int(math.log2(len(bts)+1))
    for _ in range(h_tree):
        if bts[root] and bts[root]['key'] == key:
            return bts[root]['value']
        elif bts[root] and key > bts[root]['key']:
            root = 2 * root + 2
        elif bts[root] and key < bts[root]['key']:
            root = 2 * root + 1
    else:
        raise KeyError()


def clear() -> None:
    """
    Clear the tree

    :return: None
    """
    bts.clear()


if __name__ == '__main__':
    print(bts)
    insert(4, 'root')
    print(bts)
    insert(10, 'right_children')
    print(bts)
    insert(2, 'left_children')
    print(bts)
    insert(13, "And again")
    print(find(13))
    print(bts)
    remove(13)
    print(bts)

