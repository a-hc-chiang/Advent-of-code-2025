import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))
from parser import get_input

example_case = '''aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out'''

# input = example_case.split("\n")
input = get_input("day-11.txt", "\n")
paths = []

res = 0
def dfs(start, adj_list):
  global res
  if start == "out":
    res += 1
    return
  node_adj_list = adj_list[start]
  if "you" in node_adj_list or not node_adj_list:
    return
  for node in node_adj_list:
    dfs(node, adj_list)

# creating adjacency list
adj_list = {} # parent node : set of children nodes

for line in input:
  as_list = line.split(":")
  parent_node = as_list[0]
  children = set()

  to_children = as_list[1].split()
  for child in to_children: 
    children.add(child)
  adj_list[parent_node] = children

# print(adj_list)
# we start with you and end with out
# res = 0
start = "you"

dfs(start, adj_list)
print(res) # YIPPEE ACCEPTED