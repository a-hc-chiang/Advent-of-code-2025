import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))
from parser import get_input

example_case = "3-5\n10-14\n16-20\n12-18\n\n1\n5\n8\n11\n17\n32"
example_case = example_case.split("\n")
input = get_input("day-5.txt", "\n")

# print(example_case)
# learnings of this puzzle: how to merge tuples that are overlapping (thanks ChatGPT LOL)

res = 0
ranges = []
prev_ranges = []

for line in input: 
  if line == "":
    break
  nums = line.split("-")
  to_add = (int(nums[0]), int(nums[1]))
  ranges.append(to_add)

ranges.sort()
merged = [ranges[0]]

for curr in ranges[1:]:
  prev_start, prev_end = merged[-1]
  curr_start, curr_end = curr
  if curr_start <= prev_end:
    merged[-1] = (prev_start, max(prev_end, curr_end))
  else:
    merged.append(curr)

print(merged)

for pair in merged: 
  res += (pair[1] - pair[0] + 1)
print(res) # YIPPEE ACCEPTED!