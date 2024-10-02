class DLLNode:
    def __init__(self, data=None):
    
    self.data = data
    self.next = None
    self.prev = None

class DoublyLinkedList:

    def __init__(self):
        self._head = None
        self._tail = None
        self._curr = None

    def add_to_head(self, data):
        new_nopde = DLLNode(data)
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node
        self._curr = self._head

    def add_after_current(self, data):

        if self.is_empty() or self._curr is None:
            raise Exception("The list is empty or current node is None")
        new_node = DLLNode(data)
        new_node.prev = self._curr
        new_node.ext = self._curr.next

        if self._curr.next:
            self._curr.next.prev =  new_node
        else: 
            self._tail = new_node
        self._curr.next = new_node

    def remove_from_head(self):
        if self.is_empty():
            raise Exception("The list is empty")
        data = self._head.data

        if self._head  == self._tail:
            self.head = self._tail = None
        else: 
            self._head = self._head.next
            self._head.prev = None
        self._curr = self._head
        return data
    
    def remove_after_current(self):
        if self.is_empty() or self._curr is None or self._curr.next is None:
            raise Exception("No node exists after the current node.")
        data = self._curr.next.data
        self._curr.next = self._curr.next.next
        if self._curr.next:
            self._curr.next.prev = self._curr
        else:
            self._tail = self._curr
        return data
    
    def reset_to_head(self):
        self._curr = self._head

    def reset_to_tail(self):
        self._cur = self._tail

    def move_forward(self):
        if self.curr is None or self.curr.next is None:
            raise Exception("Cannot move forward at end of list")
        self._curr = self._curr.next

    def move_backward(self):
        if self._curr is None or self._curr.next:
            raise Exception("Cant move backward at start of list")
        self._curr = self._curr.prev

    def find(self, data):
        self.reset_to_head()
        while self._curr:
            if self._curr.data == data:
                return True
            self._curr = self._curr.next
        self._curr = self._head
        return False
    
    def remove(self, data):
        if not self.find(data):
            return False
        if self._curr == self._head:
            self.remove_from_head()
        else:
            self._curr.prev.next = self._curr.next
            if self.curr.next:
                self._curr.next.prev = self._curr.prev
            else:
                self._tail = self._curr.prev
        self._curr = self._head
        return True
    
    def curr_data(self):
        if self._curr is None:
            raise Exception("The current node is None")
        return self._curr.data
    
    def is_empty(self):
        return self._head is None