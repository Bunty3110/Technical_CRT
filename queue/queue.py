class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
        print(f"Enqueued: {item}")
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        item = self.items.pop(0)
        print(f"Dequeued: {item}")
        return item
    
    def peek(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        print(f"Front element: {self.items[0]}")
        return self.items[0]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def display(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            print(f"Queue: {self.items}")
    
    def delete(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"Deleted: {item}")
        else:
            print(f"Item {item} not found in queue!")


queue = Queue()

while True:
    print("\n--- Queue Menu ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display Queue")
    print("5. Queue Size")
    print("6. Delete")
    print("7. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        item = input("Enter item to enqueue: ")
        queue.enqueue(item)
    elif choice == '2':
        queue.dequeue()
    elif choice == '3':
        queue.peek()
    elif choice == '4':
        queue.display()
    elif choice == '5':
        print(f"Queue size: {queue.size()}")
    elif choice == '6':
        item = input("Enter item to delete: ")
        queue.delete(item)
    elif choice == '7':
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please try again.")
