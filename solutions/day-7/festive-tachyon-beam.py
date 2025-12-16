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

# example_case = example_case.split("\n")
input = get_input("day-7.txt", "\n")
res = 0

s_idx = find_s_idx(input[0])
print(s_idx)

beam_idx = [[s_idx]]

for line in input[1:]:
  print(beam_idx)
  if "^" not in line:
    print("HELLO")
    beam_idx.append(beam_idx[-1])
    continue

  to_add = set()
  for i in beam_idx[-1]:
    # print("to_add", to_add)
    if line[i] == "^":
      if line[i-1] == ".":
        to_add.add(i-1)
        flag1 = True
      if line[i+1] == ".":
        to_add.add(i+1)
        flag2 = True
      res += 1
  beam_idx.append(list(to_add))
  
# print(example_case)
# print(beam_idx)
print(res) # ANSWER TOO SMALL!!
# print(sum(res))
