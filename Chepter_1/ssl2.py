
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at last
    def insert_last(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    # Insert at position
    def insert_position(self, data, pos):
        total = self.get_count()

        if pos < 1 or pos > total + 1:
            print("Invalid position")
            return

        new_node = Node(data)

        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head

        for i in range(pos - 2):
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

    # Delete at beginning
    def delete_begin(self):
        if self.head is None:
            print("Linked List is empty")
            return

        self.head = self.head.next

    # Delete at last
    def delete_last(self):
        if self.head is None:
            print("Linked List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next.next is not None:
            temp = temp.next

        temp.next = None

    # Delete at position
    def delete_position(self, pos):
        total = self.get_count()

        if pos < 1 or pos > total:
            print("Invalid position")
            return

        if pos == 1:
            self.head = self.head.next
            return

        temp = self.head

        for i in range(pos - 2):
            temp = temp.next

        temp.next = temp.next.next

    # Search
    def search(self, key):
        temp = self.head
        pos = 1

        while temp is not None:
            if temp.data == key:
                print("Value found at position", pos)
                return

            temp = temp.next
            pos += 1

        print("Value not found")

    # Count nodes
    def get_count(self):
        c = 0
        temp = self.head

        while temp is not None:
            c += 1
            temp = temp.next

        return c

    def count(self):
        print("Total nodes =", self.get_count())

    # Reverse linked list
    def reverse(self):
        prev = None
        curr = self.head

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.head = prev
        print("Linked List reversed successfully")

    # Display
    def display(self):
        if self.head is None:
            print("Linked List is empty")
            return

        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Main program
l1 = SLL()

while True:
    print("\n----- SINGLY LINKED LIST -----")
    print("1. Insert Begin")
    print("2. Insert Last")
    print("3. Insert at Position")
    print("4. Delete Begin")
    print("5. Delete Last")
    print("6. Delete at Position")
    print("7. Display")
    print("8. Count")
    print("9. Search")
    print("10. Reverse")
    print("11. Exit")

    ch = int(input("Enter your choice = "))

    if ch == 1:
        data = int(input("Enter node value = "))
        l1.insert_begin(data)

    elif ch == 2:
        data = int(input("Enter node value = "))
        l1.insert_last(data)

    elif ch == 3:
        data = int(input("Enter node value = "))
        pos = int(input("Enter position = "))
        l1.insert_position(data, pos)

    elif ch == 4:
        l1.delete_begin()

    elif ch == 5:
        l1.delete_last()

    elif ch == 6:
        pos = int(input("Enter position = "))
        l1.delete_position(pos)

    elif ch == 7:
        l1.display()

    elif ch == 8:
        l1.count()

    elif ch == 9:
        key = int(input("Enter value to search = "))
        l1.search(key)

    elif ch == 10:
        l1.reverse()

    elif ch == 11:
        print("Program Exit")
        break

    else:
        print("Invalid choice")
