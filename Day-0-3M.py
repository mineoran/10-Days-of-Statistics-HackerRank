"""https://www.hackerrank.com/challenges/s10-basic-statistics/problem"""

import random
from statistics import median
from statistics import mean
from statistics import mode
from scipy import stats
import numpy as np


s =int(input("Enter the data size:")) 
arr =[]
for  _ in range(s):
    data = random.randint(1,49)
    arr.append(data)

print(f"Your numerical data: {arr}")

mean = (int(sum(arr)/2))
print(mean)
print(np.median(arr))
print(int(stats.mode(arr)[0]))


# If you dont want random data:
#You can use this 

# import numpy as np
# from scipy import stats

# size = int(input())
# numbers = list(map(int, input().split()))
# print(np.mean(numbers))
# print(np.median(numbers))
# print(int(stats.mode(numbers)[0]))
