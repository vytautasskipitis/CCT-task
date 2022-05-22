from typing import List
import math


def find_maximum_distance(number_of_cities: int, cities_with_train_station: List[int]) -> int:
    # TODO: Replace this with real implementation:

    distances_between = []
    distances_single_way = []
    index = -1

    for i in cities_with_train_station:
        distances_between.append(i - cities_with_train_station[index])
        index += 1
    distances_between.pop(0)

    distances_single_way.append(cities_with_train_station[0])

    distances_single_way.append((number_of_cities - cities_with_train_station[-1]) - 1)

    if all(x is None for x in distances_between):
        return max(distances_single_way)
    elif (max(distances_single_way) * 2) > max(distances_between):
        return max(distances_single_way)
    else:
        return math.trunc(max(distances_between) / 2)


if __name__ == "__main__":
    # These are some of test cases. When evaluating the task, more will be added:
    assert find_maximum_distance(number_of_cities=3, cities_with_train_station=[1]) == 1
    assert find_maximum_distance(number_of_cities=4, cities_with_train_station=[3]) == 3
    assert find_maximum_distance(number_of_cities=5, cities_with_train_station=[0, 4]) == 2
    assert find_maximum_distance(number_of_cities=30, cities_with_train_station=[0, 4, 15, 22, 26]) == 5
    assert find_maximum_distance(number_of_cities=10, cities_with_train_station=[2, 8]) == 3
    assert find_maximum_distance(number_of_cities=10, cities_with_train_station=[0]) == 9
    assert find_maximum_distance(number_of_cities=100000, cities_with_train_station=[0]) == 99999
    assert find_maximum_distance(number_of_cities=10, cities_with_train_station=[9]) == 9

    print("ALL TESTS PASSED")
