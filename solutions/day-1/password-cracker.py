import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))
from parser import get_input

example_case = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']
input = get_input("day-1.txt")

# range = [0, 99]
start = 50
MIN = 1
MAX = 100
res = 0

for turn in input: 
  direction = turn[0]
  value = int(turn[1:]) % 100
  if direction == "L": 
    if start + value > MAX: 
      start += (value - MAX) 
    else: 
      start += value
  else: 
    if start - value < MIN: 
      start = MAX + (start - value)
    else: 
      start -= value
  if start == MAX: 
    res += 1
print(res)