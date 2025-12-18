import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))
from parser import get_input
from collections import defaultdict

example_case = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""

def find_s_idx(s):
  for i in range(len(s)):
    if s[i] == "S":
      return i
  return -1

example_case = example_case.split("\n")
input = get_input("day-7.txt", "\n")
res = 0

s_idx = find_s_idx(input[0])
curr = {s_idx:1}

for line in input[1:]:
  if "^" not in line:
    continue
  to_add = defaultdict(int)
  for i in curr:
    if line[i] == "^":
      if line[i-1] == ".":
        to_add[i-1] += curr[i]
      if line[i+1] == ".":
        to_add[i+1] += curr[i]
    else:
      to_add[i] += curr[i]
  curr = to_add

# print(beam_idx)
for k in curr: 
  res += curr[k]

print(res) # YIPPEE ACCEPTED!
# print(curr)
