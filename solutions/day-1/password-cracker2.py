import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))
from parser import get_input

example_case = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']
input = get_input("day-1.txt", "\n")

# range = [0, 99]
start = 50
MIN = 1
MAX = 99
res = 0

for turn in example_case:
  if start == 0:
    res += 1
  direction = turn[0]
  num = int(turn[1:])
  res += abs(num) // 100
  value = num % 100
  print(num, start, res)
  if direction == "L":
    movement = -value
  else:
    movement = value
  end = start + movement
  if direction == "L":
    if end < MIN:
      res += 1
  else:
    if end > MAX:
      res += 1
  start = end % 100
print(res) # WRONG OUTPUT FOR SOME GODDAMN REASON???