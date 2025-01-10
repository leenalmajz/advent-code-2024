from typing import List

def read_input (file_path: str) -> List[List[int]]:
    '''Read the input file and return a tuple of two sorted lists of integers'''

    with open(file_path, 'r') as file:
        data = file.readlines()

    list = []

    for location_IDs in data:
        location_ID = location_IDs.strip().split()
        location_ID = [int(x) for x in location_ID]
        list.append(location_ID)
    
    return list

def safe_reports (lists: List[List[int]]) -> int:
    '''Find the total distance between two lists of integers'''

    count_of_safe_reports = 0

    for row in lists:
        safe = True
        change = " "
        if 1 <= row[1] - row[0] <= 3:
            change = "increasing"
        elif -3 <= row[1] - row[0] <= -1:
            change = "decreasing"
        else:
            safe = False

        if safe:
            for i in range(len(row)-1):
                if 1 <= row[i+1] - row[i] <= 3:
                    difference = "increasing"
                elif -3 <= row[i+1] - row[i] <= -1:
                    difference = "decreasing"
                else:
                    safe = False
                    break

                if difference != change:
                    safe = False
                    break
        
        if safe:
            count_of_safe_reports += 1
        
    return count_of_safe_reports

if __name__ == "__main__" :

    lists = read_input('day-2/input.txt')

    count_of_safe_reports = safe_reports(lists)

    print(count_of_safe_reports)

                

                


    

