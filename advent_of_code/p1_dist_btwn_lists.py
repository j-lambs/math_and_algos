from MinHeap import MinHeap

# with open("p1_sample_input.txt") as f:
#   for line in f:
#     first_int = int(line[0])
#     second_int = int(line[4])
#     print(f'{first_int}, {second_int}')

h = MinHeap(heap=[None])
h.add_node(50)
h.add_node(25)
h.add_node(75)
h.add_node(5)
h.display()
h.extract_min()
h.display()
