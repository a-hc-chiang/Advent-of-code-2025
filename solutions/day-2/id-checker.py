import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))
from parser import get_input

example_case = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
input = get_input("day-2.txt", ",")

'''
IDs have no leading 0s 
find invalid IDs where: 

an ID has a sequence of when a digit is repeated twice
we can skip on anything that does not have an even placement 
if x log 10 is even then we can skip evaluation 
except im lazy im going to just convert this to a string and count the length LOL
'''

input_as_list = example_case.split(",")
res = set()

for ids in input:
  start_and_end = ids.split("-")
  start = start_and_end[0]
  end = start_and_end[1]

  start_num = int(start)
  end_num = int(end)
  for i in range(start_num, end_num + 1):
    as_str = str(i)
    if len(as_str) % 2 != 0:
      continue
    first_half = as_str[:int(len(as_str)/2)]
    second_half = as_str[int(len(as_str)/2):]
    if first_half == second_half:
      res.add(i)
print(sum(res)) #YIPPEE ACCEPTED!