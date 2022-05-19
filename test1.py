from typing import List
import math


def find_maximum_distance(
        number_of_cities: int, cities_with_train_station: List[int]
) -> int:
    # TODO: Replace this with real implementation:

    longest_distance = []
    cities_with_train_station.sort()
    distance = -1
    two_directions = False

    for i in range(0, number_of_cities):
        if not two_directions:
            distance += 1

            if i in cities_with_train_station:
                print(math.trunc(distance), "km to the station")
                longest_distance.append(math.trunc(distance))
                distance = 0
                two_directions = True

        elif two_directions:
            distance += 0.5

            if i in cities_with_train_station:
                print(math.trunc(distance), "km to the station")
                longest_distance.append(math.trunc(distance))
                distance = 0
            if cities_with_train_station[-1] == i:
                two_directions = False

        else:
            print("error")
    print(longest_distance)

    return max(longest_distance)


if __name__ == "__main__":
    # These are some of test cases. When evaluating the task, more will be added:
    assert find_maximum_distance(number_of_cities=3, cities_with_train_station=[1]) == 1
    assert find_maximum_distance(number_of_cities=4, cities_with_train_station=[3]) == 3
    assert find_maximum_distance(number_of_cities=5, cities_with_train_station=[0, 4]) == 2
    assert find_maximum_distance(number_of_cities=30, cities_with_train_station=[0, 4, 15, 22, 26]) == 6
    assert find_maximum_distance(number_of_cities=10, cities_with_train_station=[2, 8]) == 3

    print("ALL TESTS PASSED")
