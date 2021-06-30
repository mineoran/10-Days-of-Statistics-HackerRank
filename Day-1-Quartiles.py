""" READ.ME : https://www.hackerrank.com/challenges/s10-quartiles/problem """

import random
from statistics import median

# s =int(input("Enter the data size:")) 
# list =[]
# for  _ in range(s):
#     data = random.randint(1,49)
#     list.append(data)
#     list.sort()
# print(f"Your sorted numerical data: {list}")
# def median(list):
#     if len(list)%2 == 0:
#         return int(sum(list[len(list)//2-1:len(list)//2+1])/2)
#     else:
#         return list[len(list)//2]

# def quartiles(s,list):
#     Q1 = median(list[:len(list)//2])
#     Q2 = median(list)
#     if s%2 == 0:
#         Q3 = median(list[len(list)//2:])
#     else:
#         Q3 = median(list[len(list)//2+1:])
#     return Q1,Q2,Q3

# quartiles(s,list)
# Q1,Q2,Q3 = quartiles(s,list)
# print(Q1)
# print(Q2)
# print(Q3)
# global variables
num = int(input())
numbers = sorted(map(int, input().split()))
mid = len(numbers) // 2 # floor division

def median(median_numbers):
    #return np.median(median_numbers) # will work if numpy import is allowed
    middle = len(median_numbers) // 2  # floor division
    if (len(median_numbers) % 2 == 0):  # even or odd
        return (median_numbers[middle-1] + median_numbers[middle]) / 2
    else:
        return median_numbers[middle]

    
# actual program starts here    
if (len(numbers) % 2 == 0):    # even or not
    Q1 = median(numbers[:mid])
    Q3 = median(numbers[mid:])
else:
    # if odd set of numbers
    Q1 = median(numbers[:mid])
    Q3 = median(numbers[mid+1:])

print(Q1)
print(median(numbers))
print(Q3)