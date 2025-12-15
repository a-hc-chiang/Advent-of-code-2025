import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))
from parser import get_input
import re

# ChatGPT 5.2 assistance with parsing and adding padding for the input, remainder code written by myself 
input = get_input("day-6.txt")

example_case = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

lines = input.splitlines()

tokens = []
starts = []

for line in lines:
    row_tokens = []
    row_starts = []
    for m in re.finditer(r"\S+", line):
        row_tokens.append(m.group())
        row_starts.append(m.start())
    tokens.append(row_tokens)
    starts.append(row_starts)

num_rows = len(tokens)
num_cols = len(tokens[0])

max_len = [0] * num_cols
for c in range(num_cols):
    for r in range(num_rows - 1):
        max_len[c] = max(max_len[c], len(tokens[r][c]))

pad_left = [False] * num_cols
for c in range(num_cols):
    min_start = min(starts[r][c] for r in range(num_rows - 1))
    pad_left[c] = any(starts[r][c] > min_start for r in range(num_rows - 1))

for r in range(num_rows - 1):
    for c in range(num_cols):
        if pad_left[c]:
            tokens[r][c] = tokens[r][c].rjust(max_len[c], "0")
        else:
            tokens[r][c] = tokens[r][c].ljust(max_len[c], "0")

def get_max_lengths(matrix):
  max_lengths = [0] * num_cols
  for c in range(num_cols):
    for r in range(num_rows - 1):
      max_lengths[c] = max(max_lengths[c], len(matrix[r][c]))
  return max_lengths

def append_zeros(matrix, max_lengths):
  for c in range(num_cols):
    print(matrix)
    for r in range(num_rows - 1):
      while len(matrix[r][c]) < max_lengths[c]:
        if r % 2 == 0:
          matrix[r][c] += "0"
        else: 
          matrix[r][c] = "0" + matrix[r][c]

def start_operation(column_values, operand):
  if operand == "*":
    res = 1
  else:
    res = 0
  for i in range(len(column_values[0])):
    n = ""
    for val in column_values:
      if val[i] != "0":
        n += val[i]
    if operand == "*":
      res *= int(n)
      # print(res)
    else:
      res += int(n)
  return res

res = []

for c in range(num_cols):
  column_nums = [tokens[r][c] for r in range(num_rows - 1)]
  operand = tokens[-1][c]
  res.append(
    start_operation(column_nums, operand)
  )

print(res)
print(sum(res)) # YIPPEE ACCEPTED!