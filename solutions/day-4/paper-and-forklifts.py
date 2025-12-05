import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))
from parser import get_input

# example_case = "..@@.@@@@.\n@@@.@.@.@@\n@@@@@.@.@@\n@.@@@@..@.\n@@.@@@@.@@\n.@@@@@@@.@\n.@.@.@.@@@\n@.@@@.@@@@\n.@@@@@@@@.\n@.@.@@@.@."
# example_case = example_case.split("\n")
input = get_input("day-4.txt", "\n")

ROLL = "@"
res = 0
input_as_matrix = []

def count_adjacent_at(matrix, i, j):
  rows = len(matrix)
  cols = len(matrix[0])
  directions = [
    (-1, 0),   # up
    (1, 0),    # down
    (0, -1),   # left
    (0, 1),    # right
    (-1, -1),  # up-left
    (-1, 1),   # up-right
    (1, -1),   # down-left
    (1, 1)     # down-right
  ]
  count = 0
  for di, dj in directions:
    ni, nj = i + di, j + dj
    if 0 <= ni < rows and 0 <= nj < cols:
      if matrix[ni][nj] == ROLL:
        count += 1
  return count

for row in input: 
  row_as_list = []
  for c in row: 
    row_as_list.append(c)
  input_as_matrix.append(row_as_list)

# print(input_as_matrix)

for i in range(len(input_as_matrix)): 
  for j in range(len(input_as_matrix[0])):
    if input_as_matrix[i][j] == ROLL:
      count = count_adjacent_at(input_as_matrix, i, j)
      # print(count, res, i, j)
      if count < 4: 
        res += 1
print(res) #YIPPEE ACCEPTED!