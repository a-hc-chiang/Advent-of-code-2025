import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))
from parser import get_input

example_case = "987654321111111\n811111111111119\n234234234234278\n818181911112111"
input = get_input("day-3.txt", "\n")
# input = example_case.split("\n")

res = []
for battery_row in input:
  curr_max = -1 
  for i in range(99, 9, -1):
    as_str = str(i)
    first_char = as_str[0]
    second_char = as_str[1]
    first_char_idx = -1 
    second_char_idx = -1
    for k in range(len(battery_row)):
      if battery_row[k] == first_char:
        first_char_idx = k
        break
    for k in range(len(battery_row)):
      if battery_row[k] == second_char and k > first_char_idx:
        second_char_idx = k
        break
    # print(first_char, first_char_idx, second_char, second_char_idx)
    if first_char_idx == -1 or second_char_idx == -1: 
      continue
    curr_max = int(first_char+second_char)
    break
  res.append(curr_max)
# print(res)
print(sum(res)) # YIPPEE ACCEPTED!
