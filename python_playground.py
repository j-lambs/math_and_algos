from advent_of_code.MinHeap import MinHeap

h1 = MinHeap(heap=[0])
h1.add_node(1)
h1.add_node(10)
h1.add_node(5)
h1.add_node(15)
h1.display()
h1.extract_min()
h1.display()
h1.extract_min()
h1.display()
