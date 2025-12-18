import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))
from parser import get_input

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
# input = get_input("day-7.txt", "\n")
res = 0

s_idx = find_s_idx(example_case[0])
beam_idx = [[s_idx]]

for line in example_case[1:]:
  if "^" not in line:
    continue

  to_add = set()
  for i in beam_idx[-1]:
    # print("to_add", to_add)
    flag1, flag2 = False, False
    if line[i] == "^":
      if line[i-1] == ".":
        if line[i-1] not in to_add:
          to_add.add(i-1)
          res += 1
        flag1 = True
      if line[i+1] == ".":
        if line[i+1] not in to_add:
          to_add.add(i+1)
          res += 1
        flag2 = True
    else:
      to_add.add(i)
    # if flag1 and flag2: 
    #   res += 2
    # if flag1 or flag2:
    #   res += 1
  if list(to_add) not in beam_idx:
    beam_idx.append(list(to_add))

print(beam_idx)
res2 = 0

for beam in beam_idx:
  res2 += len(beam)
print(res)
print(res2)
# print(sum(res))
