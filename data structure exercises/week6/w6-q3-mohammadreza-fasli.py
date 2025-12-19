class Node:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.next = None
        self.prev = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, id, name):

        node = self.head
        if node:
            while True:
                if node.id == id or node.name == name:
                    print("Duplicate id or spell name")
                    return
                node = node.next
                if node == self.head:
                    break

        new_node = Node(id, name)

        if not self.head:
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
            print(f"Spell {name} with id {id} successfully added")
            return

        node = self.head
        inserted = False
        while True:
            if id < node.id:
                break
            node = node.next
            if node == self.head:
                break

        prev_node = node.prev
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = node
        node.prev = new_node

        if id < self.head.id:
            self.head = new_node
        print(f"Spell {name} with id {id} successfully added")

    def remove(self, id):
        if not self.head:
            print("empty")
            return
        node = self.head
        found = False
        while True:
            if node.id == id:
                found = True
                break
            node = node.next
            if node == self.head:
                break
        if not found:
            print("Invalid id")
            return
        name = node.name
        if node.next == node:
            self.head = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            if node == self.head:
                self.head = node.next
        print(f"Spell {name} removed successfully")

    def find(self, name):
        if not self.head:
            print("False")
            return
        node = self.head
        while True:
            if node.name == name:
                print("True")
                return
            node = node.next
            if node == self.head:
                break
        print("False")

    def display(self):
        if not self.head:
            print("No spells to display")
            return
        node = self.head
        while True:
            print(
                f"Spell: {node.name}, id: {node.id}, prev: {node.prev.id}, next: {node.next.id}"
            )
            node = node.next
            if node == self.head:
                break


cdll = CircularDoublyLinkedList()
while True:
    inp = input().strip().split()
    if not inp:
        continue
    if inp[0] == "EXIT":
        break
    elif inp[0] == "INSERT":
        if len(inp) != 3:
            print("Invalid input")
            continue
        try:
            id = int(inp[1])
            name = inp[2]
            cdll.insert(id, name)
        except:
            print("Invalid input")
    elif inp[0] == "REMOVE":
        if len(inp) != 2:
            print("Invalid input")
            continue
        try:
            id = int(inp[1])
            cdll.remove(id)
        except:
            print("Invalid input")
    elif inp[0] == "FIND":
        if len(inp) != 2:
            print("Invalid input")
            continue
        cdll.find(inp[1])
    elif inp[0] == "DISPLAY":
        cdll.display()
    else:
        print("Invalid input")
