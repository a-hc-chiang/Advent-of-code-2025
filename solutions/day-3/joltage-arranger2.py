import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))
from parser import get_input

example_case = "234234234234278" #"987654321111111\n811111111111119\n234234234234278\n818181911112111"
# input = get_input("day-3.txt", "\n")
input = example_case.split("\n")

BATTERY_COUNT = 12
res = []