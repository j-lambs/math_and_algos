from MinHeap import MinHeap

with open("advent_of_code/p1_sample_input.txt") as f:
  h1 = MinHeap(heap=[None])
  h2 = MinHeap(heap=[None])
  for line in f:
    first_int = int(line[0])
    second_int = int(line[4])
    h1.add_node(first_int)
    h2.add_node(second_int)
    
#TODO: fix MinHeap.extract_min() in case of h2
h1.display()
h2.display()
total_dist = 0
for i in range(1, h1.get_len()):
  min1 = h1.extract_min()
  min2 = h2.extract_min()
  dist = abs(min1 - min2)
  total_dist += dist
print(total_dist)

