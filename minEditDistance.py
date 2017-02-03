
# coding: utf-8

# In[1]:

import numpy as np;
from numpy import matrix;


# In[2]:

source = "drive"
target = "divers"


# In[3]:

def minEditDistance(target,source):
    n = len(target)
    m = len(source)
    dist_matrix = np.zeros(shape=(n+1,m+1))
    dist_matrix[0][0] = 0
    for i in range(1, n):
        dist_matrix[i,0] = dist_matrix[i-1,0] + 1
    for j in range(1,m):
        dist_matrix[0,j] = dist_matrix[0,j-1] + 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            row_dist = dist_matrix[i-1,j] + 1
            col_dist = dist_matrix[i,j-1] + 1
            offset = 0;
            if target[i-1:i] == source[j-1:j]:
                offset = 0
            else:
                offset = 2
            diagonal_dist = dist_matrix[i-1,j-1] + offset
            dist_matrix[i,j] = min(row_dist,col_dist,diagonal_dist)
    print dist_matrix        
    return dist_matrix[n,m];


# In[4]:

print minEditDistance(target,source);

