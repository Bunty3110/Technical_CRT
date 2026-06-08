class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # Delete node
    def delete(self, key):
        temp = self.head

        # If head node itself contains key
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None

        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        # Element not found
        if temp is None:
            print("Element not found")
            return

        prev.next = temp.next
        temp = None

    # Search element
    def search(self, key):
        temp = self.head

        while temp:
            if temp.data == key:
                return True
            temp = temp.next

        return False

    # Reverse linked list
    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    # Display list
    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Driver code
ll = LinkedList()

ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)

ll.insert_begin(5)

print("Linked List:")
ll.display()

print("Searching 20:", ll.search(20))

ll.delete(20)
print("After deleting 20:")
ll.display()

ll.reverse()
print("After reverse:")
ll.display()