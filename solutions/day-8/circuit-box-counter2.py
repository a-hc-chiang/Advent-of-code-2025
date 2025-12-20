import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))
from parser import get_input
import heapq
import math
from ordered_set import OrderedSet

example_case = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""
example_case = example_case.split("\n")

def find_distance(a, b):
  return math.sqrt(sum((b[i] - a[i])**2 for i in range(3)))

def add_new_group(a, b):
  group = {a, b}
  idx = len(groups)
  groups.append(group)
  node_to_group[a] = idx
  node_to_group[b] = idx

def add_to_group(node, group_idx):
  groups[group_idx].add(node)
  node_to_group[node] = group_idx

def merge_groups(idx1, idx2):
  if idx1 == idx2:
    return
  if len(groups[idx1]) < len(groups[idx2]):
    idx1, idx2 = idx2, idx1
  for node in groups[idx2]:
    groups[idx1].add(node)
    node_to_group[node] = idx1

  groups[idx2].clear()

# input = get_input("day-8.txt", "\n")
nodes = {}
for i in range(len(example_case)):
  as_list = example_case[i].split(",")
  node = (int(as_list[0]), int(as_list[1]), int(as_list[2]))
  nodes[i] = node

# print(nodes)
adj_list = []
# distances to node 
for i in range(len(nodes)-1): 
  for j in range(i+1, len(nodes)): 
    distance = find_distance(nodes[i], nodes[j])
    adj_list.append((distance, i, j))
# print(adj_list)

heapq.heapify(adj_list)
groups = []
node_to_group = {}
visited = OrderedSet()

dist, x, y = heapq.heappop(adj_list)
add_new_group(x, y)
visited.update([x, y])

# ChatGPT 5.2 Assisted in creating the loop conditions + additional helper functions:
while adj_list and len(visited) != len(example_case):
  dist, a, b = heapq.heappop(adj_list)
  print(dist, a, nodes[a], b, nodes[b], visited)
  visited.update([a, b])
  g1 = node_to_group.get(a)
  g2 = node_to_group.get(b)
  
  if g1 is not None and g2 is not None:
    if g1 == g2:
      continue
    merge_groups(g1, g2)
  elif g1 is not None:
    add_to_group(b, g1)
  elif g2 is not None:
    add_to_group(a, g2)
  else:
    add_new_group(a, b)
groups = [g for g in groups if g]

print(visited)
print(len(visited))

last_node = visited[-1]
last_node2 = visited[-2]

print(nodes[last_node], nodes[last_node2])
print(nodes[last_node][0]*nodes[last_node2][0])

for k in visited: 
  print(nodes[k])
print(groups)