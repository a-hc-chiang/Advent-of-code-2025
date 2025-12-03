import math
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))
from parser import get_input

example_case = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
input = get_input("day-2.txt", ",")

input_as_list = example_case.split(",")
res = set()

def split_into_parts(s: str, n: int) -> list[str]:
  part_len = len(s) // n
  return [s[i:i + part_len] for i in range(0, len(s), part_len)]

for ids in input:
  start_and_end = ids.split("-")
  start = start_and_end[0]
  end = start_and_end[1]

  start_num = int(start)
  end_num = int(end)
  for i in range(start_num, end_num + 1):
    as_str = str(i)
    first_idx = 0
    last_idx = 0
    length = len(as_str)
    # print(length, start, end, res)
    for j in range(1, length):
      if length % j != 0:
        continue
      mult = int(length / j)
      splitted = split_into_parts(as_str, mult)
      # print(f"splitted: {splitted}")
      duplicates = set(splitted)
      if len(duplicates) == 1:
        res.add(int(as_str))
        break
# print(res)
print(sum(res))