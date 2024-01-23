# Node 
class Node:
    # Khởi tạo đối tượng node
    def __init__(self,data):
        self.data = data # gán dữ liệu
        self.next = None # tham chiếu đến node tiếp theo

# Node of a doubly linked list
class DNode:
    # Khởi tạo đối tượng node
    def __init__(self,data):
        self.data = data # gán dữ liệu
        self.next = None # tham chiếu đến node tiếp theo
        self.prev = None # tham chiếu đến node trước đó

class LinkedList:
    # Khởi tạo đối tượng LinkedList
    def __init__(self):
        self.head = Node # Khởi tạo head node

