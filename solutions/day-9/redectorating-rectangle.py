import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))
from parser import get_input

example_case = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""

# input = example_case.split("\n")
input = get_input("day-9.txt", "\n")

res = []

for i in range(len(input)):

  for j in range(len(input)):
    if i == j: 
      continue
    as_list_i = input[i].split(",")
    as_list_j = input[j].split(",")
    x_diff = abs(int(as_list_i[0])-int(as_list_j[0])) + 1
    y_diff = abs(int(as_list_i[1])-int(as_list_j[1])) + 1
    res.append(x_diff*y_diff)

print(res)
print(max(res)) # YIPPEE ACCEPTED!