import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))
from parser import get_input

example_case = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']
input = get_input("day-1.txt", "\n")

# range = [0, 99]
curr = 50
MIN = 1
MAX = 99
res = 0

for turn in input:
  direction = turn[0]
  num = int(turn[1:])
  res += abs(num) // 100
  value = num % 100
  # print(num, curr, res)
  if direction == "L":
    movement = -value
  else:
    movement = value
  end = curr + movement
  print(end)
  if direction == "L":
    if curr == 0: 
      curr = 100 + value
      if curr < MIN:
        res += 1
    elif end < MIN:
      res += 1
  else:
    if curr == 100: 
      curr = value
      if curr > MAX:
        res += 1
    elif end > MAX:
      res += 1
  curr = end % 100
# print(curr)
print(res) # YIPPEE!!! ACCEPTED