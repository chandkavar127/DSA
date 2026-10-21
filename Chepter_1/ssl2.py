
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

    # Insert at given position
    def insert_position(self, data, pos):
        if pos < 1:
            print("Invalid position")
            return

        new_node = Node(data)

        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head

        for i in range(pos - 2):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid position")
            return

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

    # Delete at given position
    def delete_position(self, pos):
        if self.head is None:
            print("Linked List is empty")
            return

        if pos < 1:
            print("Invalid position")
            return

        if pos == 1:
            self.head = self.head.next
            return

        temp = self.head

        for i in range(pos - 2):
            if temp.next is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp.next is None:
            print("Invalid position")
            return

        temp.next = temp.next.next

    # Display linked list
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
    print("8. Exit")

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
        print("Program Exit")
        break

    else:
        print("Invalid choice")
