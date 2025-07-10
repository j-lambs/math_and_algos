class LRNode:
    def __init__(self, val, left, right) -> None:
        self.val = val
        self.left = left
        self.right = right

    def get_val(self):
        return self.val
    
    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right
    