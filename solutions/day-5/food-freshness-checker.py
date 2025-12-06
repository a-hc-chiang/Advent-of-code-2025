import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))
from parser import get_input

example_case = "3-5\n10-14\n16-20\n12-18\n\n1\n5\n8\n11\n17\n32"
example_case = example_case.split("\n")
input = get_input("day-5.txt", "\n")

print(example_case)

res = 0
ranges = []
ids = []
is_range = True

for range in input: 
  if range == "":
    is_range = False
    continue

  if is_range:
    nums = range.split("-")
    to_add = (int(nums[0]), int(nums[1]))
    ranges.append(to_add)
  else: 
    ids.append(int(range))

print(ranges)
print(ids)

for id in ids: 
  for range in ranges:
    if range[0] <= id and range[1] >= id:
      res += 1 
      break

print(res) # YIPPEE ACCEPTED!