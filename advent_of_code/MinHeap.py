class MinHeap:
    def __init__(self, heap: list) -> None:
        self.heap = heap
    
    def add_node(self, new_val: int):
        self.heap.append(new_val)
        self.__heapify(new_val)
        
    def __heapify(self, new_val):
        i = len(self.heap) - 1  # index of last available spot
        in_correct_position = False
        while (not in_correct_position) and i != 1:
            # if inserted val <= parent, swap them and continue
            parent_index = int(i // 2)
            parent = self.heap[parent_index]
            if new_val <= parent:
                dmw = parent
                self.heap[parent_index] = new_val
                self.heap[i] = dmw
                i = parent_index
            else:
                in_correct_position = True

    def extract_min(self):
        min = self.heap[1]
        if len(self.heap) == 2:
            self.heap.pop()
            return min

        # move last val in heap to front, and keep swapping him down until in correction position
        last_val = self.heap[-1]
        self.heap[1] = last_val
        self.heap.pop()

        # TODO: find issue in index checking!
        # change so that it checks first if both children exist
        i = 1
        cur_val = self.heap[i]
        in_correct_position = False
        # currently exits if 'cur' does not have both children, BUT, is wrong in case of having only 1 child
        while (not in_correct_position) and (i * 2 < len(self.heap)):
            left_i = i * 2
            right_i = i * 2 + 1
            left_val = self.heap[left_i]
            # if right child does not exist
            if i * 2 + 1 >= len(self.heap):
                if cur_val < left_val:
                    in_correct_position = True
                else:
                    dmw = cur_val
                    self.heap[i] = left_val
                    i = left_i
                    self.heap[i] = dmw
            else:
                right_val = self.heap[right_i]

                # first check if children are smaller than i
                # if not, i in correct position
                if cur_val < left_val and cur_val < right_val:
                    in_correct_position = True
                # get smaller of the two children nodes, and swap i with them
                else:
                    dmw = cur_val
                    if left_val <= right_val:
                        self.heap[i] = left_val
                        i = left_i
                    else:
                        self.heap[i] = right_val
                        i = right_i
                    self.heap[i] = dmw
        return min

    def get_min(self):
        return self.heap[1]

    def display(self):
        temp_display_list = []
        for i in self.heap:
            temp_display_list.append(i)
        print(temp_display_list)

    def get_len(self):
        return len(self.heap) - 1
