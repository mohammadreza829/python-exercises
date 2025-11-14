import sys


class Node:

    def __init__(self, isbn, title, parent=None):
        self.isbn = isbn
        self.title = title
        self.parent = parent
        self.left = None
        self.right = None


class ParentAwareBST:

    def __init__(self):
        self.root = None

    def insert(self, isbn, title):
        if not self.root:
            self.root = Node(isbn, title)
            print(f"Book {isbn} {title} added")
            return

        current = self.root
        while True:
            if isbn < current.isbn:
                if not current.left:
                    current.left = Node(isbn, title, parent=current)
                    print(f"Book {isbn} {title} added")
                    return
                current = current.left
            elif isbn > current.isbn:
                if not current.right:
                    current.right = Node(isbn, title, parent=current)
                    print(f"Book {isbn} {title} added")
                    return
                current = current.right
            else:
                print("Book already exists")
                return

    def search(self, isbn):
        node = self.root
        path = []
        while node and node.isbn != isbn:
            path.append(str(node.isbn))
            node = node.left if isbn < node.isbn else node.right

        if node:
            path.append(str(node.isbn))
            print(f"Found: {node.isbn} {node.title}")
            print(f"Path: {', '.join(path)}")
        else:
            print("Not found")

    def _transplant(self, node_u, node_v):
        if not node_u.parent:
            self.root = node_v
        elif node_u == node_u.parent.left:
            node_u.parent.left = node_v
        else:
            node_u.parent.right = node_v
        if node_v:
            node_v.parent = node_u.parent

    def delete(self, isbn):
        node = self.root
        while node and node.isbn != isbn:
            node = node.left if isbn < node.isbn else node.right

        if not node:
            print("Book not found")
            return

        print(f"Book {isbn} {node.title} removed")

        if not node.left:
            self._transplant(node, node.right)
        elif not node.right:
            self._transplant(node, node.left)
        else:
            successor = node.right
            while successor.left:
                successor = successor.left

            if successor.parent != node:
                self._transplant(successor, successor.right)
                successor.right = node.right
                successor.right.parent = successor

            self._transplant(node, successor)
            successor.left = node.left
            successor.left.parent = successor

    def display(self):
        if not self.root:
            print("No books in library")
            return

        print("Books:")
        node, stack = self.root, []
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                print(f"{node.isbn} {node.title}")
                node = node.right


def main_controller():

    tree = ParentAwareBST()

    lines = sys.stdin.readlines()

    for line in lines:
        line = line.strip()
        if not line:
            continue

        parts = line.split()
        command = parts[0]

        try:
            if command == "exit":
                break
            elif command == "add":
                tree.insert(int(parts[1]), parts[2])
            elif command == "find":
                tree.search(int(parts[1]))
            elif command == "remove":
                tree.delete(int(parts[1]))
            elif command == "show":
                tree.display()
            else:
                print("invalid input")
        except (ValueError, IndexError):
            print("invalid input")


if __name__ == "__main__":
    main_controller()
