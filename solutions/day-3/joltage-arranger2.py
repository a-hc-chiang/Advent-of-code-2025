import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))
from parser import get_input

example_case = """987654321111111
811111111111119
234234234234278
818181911112111"""

input = get_input("day-3.txt", "\n")
# input = example_case.split("\n")

def get_max_idx(s):
  max_val = -1
  max_idx = -1
  for i in range(len(s)):
    if int(s[i]) > max_val:
      max_val = int(s[i])
      max_idx = i
  return max_idx

BATTERY_COUNT = 12
res = []

for val in input:
  print(val)
  to_add = ""
  curr_start, curr_end = 0, len(val) - BATTERY_COUNT + 1
  for i in range(BATTERY_COUNT):
    print(curr_start, curr_end, len(val))
    sub_str = val[curr_start:curr_end]
    real_max_idx = get_max_idx(sub_str) + curr_start
    print(real_max_idx)
    to_add += val[real_max_idx]
    curr_start = real_max_idx + 1
    curr_end += 1
  res.append(int(to_add))

# print(res)
print(sum(res)) # YIPPEE ACCEPTED
