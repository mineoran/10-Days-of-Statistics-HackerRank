""" READ.ME : https://www.hackerrank.com/challenges/s10-quartiles/problem """
""" Instead of manually entering the data one by one, we performed quartiles on the data we brought from the interval we determined with the random method."""
import random
from statistics import median

s =int(input("Enter the data size:")) 
list =[]
for  _ in range(s):
    data = random.randint(1,49)
    list.append(data)
    list.sort()
print(f"Your sorted numerical data: {list}")
def median(list):
    if len(list)%2 == 0:
        return int(sum(list[len(list)//2-1:len(list)//2+1])/2)
    else:
        return list[len(list)//2]

def quartiles(s,list):
    Q1 = median(list[:len(list)//2])
    Q2 = median(list)
    if s%2 == 0:
        Q3 = median(list[len(list)//2:])
    else:
        Q3 = median(list[len(list)//2+1:])
    return Q1,Q2,Q3

quartiles(s,list)
Q1,Q2,Q3 = quartiles(s,list)
print(Q1)
print(Q2)
print(Q3)
