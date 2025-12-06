import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))
from parser import get_input

example_case = "123 328  51 64 \n 45 64  387 23 \n  6 98  215 314 \n*   +   *   +  "
example_case = example_case.split("\n")
input = get_input("day-6.txt", "\n")

res = 0
nums = []
opreands = []
first_iteration = True

for line in input: 
  as_list = line.split()
  if first_iteration: 
    first_iteration = False
    for i in as_list: 
      if i == "*" or i == "+":
        opreands.append(i)
      else:
        nums.append([int(i)])
    continue
  for i in range(len(as_list)):
    if as_list[i] == "*" or as_list[i] == "+":
      opreands.append(as_list[i])
    else:
      nums[i].append(int(as_list[i]))

res = [0] * len(opreands)
for i in range(len(opreands)):
  if opreands[i] == "*":
    res[i] = 1
    for j in range(len(nums[0])):
      # print(i, j, res)
      res[i] *= nums[i][j]
  if opreands[i] == "+":
    for j in range(len(nums[0])):
      res[i] += nums[i][j]

# print(nums)
# print(opreands)
# print(res)
print(sum(res)) # ACCEPTED YIPPEE!!