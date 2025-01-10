from typing import List, Tuple

def sum_of_distances(list1: List[int], list2: List[int]) -> int:
    '''Find the total distance between two lists of integers'''

    list1.sort(), list2.sort()

    difference = [abs(a-b) for a,b in zip(list1, list2)]
    
    total_distance = sum(difference)

    return total_distance

def read_input (file_path: str) -> Tuple[List[int], List[int]]:
    '''Read the input file and return a tuple of two sorted lists of integers'''

    with open(file_path, 'r') as file:
        data = file.readlines()
    
    list1 = []
    list2 = []

    for location_IDs in data:
        location_ID = location_IDs.strip().split()
        list1.append(int(location_ID[0]))
        list2.append(int(location_ID[1]))
    
    return list1, list2

if __name__ == "__main__" :
    
    list1, list2 = read_input('day-1/input.txt')

    total_distance = sum_of_distances(list1, list2)

    print(total_distance)
