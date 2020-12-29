from typing import Union, Sequence


# Прямой путь
def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    cost = [float('inf')] * len(stairway)
    cost[0] = stairway[0]
    cost[1] = stairway[1]

    for step in range(2, len(stairway)):
        cost[step] = stairway[step] + min(cost[step - 1], cost[step - 2])

    return cost[-1]


if __name__ == '__main__':
    print(stairway_path([1, 3, 1, 5, 2, 7, 7, 8, 9, 4, 6, 3]))