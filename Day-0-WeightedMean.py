import math
import os
import random
import re
import sys 
# Complete the 'weightedMean' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY X
#  2. INTEGER_ARRAY W

n = int(input().strip())

vals = list(map(int, input().rstrip().split()))

weights = list(map(int, input().rstrip().split()))


def weightedMean(X, W):
    
    l=map(lambda x,y:x*y,vals,weights)    
    weights_sum = sum(weights)
    w_sum = sum(l)
    result = (w_sum/ weights_sum)
    print("%.1f" % result)

weightedMean(vals, weights)