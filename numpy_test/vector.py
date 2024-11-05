import numpy as np

# 创建一个行向量
vector_row = np.array([1, 2, 3, 4, 5, 6])
print(vector_row[0])
print(np.max(vector_row))
print(vector_row)

# 创建一个列向量
vector_col = np.array([
    [1],
    [2],
    [3],
    [4],
    [5],
    [6]
])
print(vector_col[0])
print(np.min(vector_col))
print(vector_col)