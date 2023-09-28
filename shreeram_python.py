import re

first_multiple_input = input().rstrip().split()
int(first_multiple_input[0])
m = int(first_multiple_input[1])


matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)


decoded_script = ""
for j in range(m):
    for i in range(n):
        decoded_script += matrix[i][j]


decoded_script = re.sub(r'(?<=[A-Za-z0-9])[^A-Za-z0-9]+(?=[A-Za-z0-9])', ' ', decoded_script)

print(decoded_script)