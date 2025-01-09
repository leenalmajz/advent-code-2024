from typing import List, Tuple
from exercise_1 import read_input

def total_similarity_score(list1: List[int], list2: List[int]) :
    ''' Calculate the sum of the product of the number of times each number in list1 appears in list2 and the number
        for example: if list1 = [1,2,3] and list2 = [1,1,2,2,2,3], the similarity score will be 1*2 + 2*3 + 3*1 = 11'''

    similarity_score = 0
    for number in list1:
        similarity_score += list2.count(number) * number
    
    return(similarity_score)

if __name__ == "__main__":

    list1, list2 = read_input('day-1/input.txt')
    similarity_score = total_similarity_score(list1,list2)

    print(similarity_score)
