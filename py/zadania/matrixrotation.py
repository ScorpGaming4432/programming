ans_matrix = (
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
    ), (
    [7, 4, 1], 
    [8, 5, 2], 
    [9, 6, 3]
)

def rotate_matrix(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[j][i], len(str(arr[j][i])))
            if len(str(arr[j][i])) > 2:
                arr[i][j] = arr[i][j], arr[j][i][0]
            arr[i][j] = arr[i][j], arr[j][i]
            print(arr[i][j])

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate_matrix(matrix)
print(matrix)  # Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
for ln in matrix:
    print(ln)