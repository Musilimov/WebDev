import numpy as np

rows_1 = int(input())
cols_1 = int(input())

array_1 = np.array([list(map(int, input().split())) 
    for _ in range(rows_1)])

rows_2 = int(input())
cols_2 = int(input())

array_2 = np.array([list(map(int, input().split())) 
    for _ in range(rows_2)])

concatenated_array = np.concatenate((array_1, array_2), axis=1)
print(concatenated_array)
