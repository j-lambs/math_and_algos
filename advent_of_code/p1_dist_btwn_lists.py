from MinHeap import MinHeap

def get_dist_btwn_lists(h1, h2) -> int:
  total_dist = 0
  for _ in range(1000):
    min1 = h1.extract_min()
    min2 = h2.extract_min()
    dist = abs(min1 - min2)
    total_dist += dist
  return total_dist

with open("advent_of_code/p1_input.txt") as f:
  h1 = MinHeap(heap=[0])
  h2 = MinHeap(heap=[0])
  for line in f:
    first_int = int(line[:5])
    second_int = int(line[8:])
    h1.add_node(first_int)
    h2.add_node(second_int)

# h1.display()
# h2.display()
print(get_dist_btwn_lists(h1, h2))
