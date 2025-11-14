# -*- coding: utf-8 -*-


class BookNode:
    """گره برای نگهداری اطلاعات کتاب."""

    def __init__(self, isbn, title):
        self.isbn = isbn
        self.title = title
        self.left_child = None
        self.right_child = None


class RecursiveBST:
    """یک پیاده‌سازی کاملاً بازگشتی از درخت جستجوی دودویی."""

    def __init__(self):
        self.tree_root = None

    def add(self, isbn, title):
        self.tree_root, message = self._add_recursive(self.tree_root, isbn, title)
        print(message)

    def _add_recursive(self, node, isbn, title):
        if not node:
            return BookNode(isbn, title), f"Book {isbn} {title} added"

        if isbn < node.isbn:
            node.left_child, msg = self._add_recursive(node.left_child, isbn, title)
        elif isbn > node.isbn:
            node.right_child, msg = self._add_recursive(node.right_child, isbn, title)
        else:
            return node, "Book already exists"

        return node, msg

    def find(self, isbn):
        path_list = []
        found_node = self._find_recursive(self.tree_root, isbn, path_list)
        if found_node:
            print(f"Found: {found_node.isbn} {found_node.title}")
            print(f"Path: {', '.join(path_list)}")
        else:
            print("Not found")

    def _find_recursive(self, node, isbn, path):
        if not node:
            return None

        path.append(str(node.isbn))
        if isbn == node.isbn:
            return node
        elif isbn < node.isbn:
            return self._find_recursive(node.left_child, isbn, path)
        else:
            return self._find_recursive(node.right_child, isbn, path)

    def remove(self, isbn):
        # برای نمایش پیام صحیح، ابتدا گره را پیدا می‌کنیم
        node_info = self._find_recursive(self.tree_root, isbn, [])
        if not node_info:
            print("Book not found")
            return

        self.tree_root = self._remove_node(self.tree_root, isbn)
        print(f"Book {isbn} {node_info.title} removed")

    def _get_min_val_node(self, node):
        current = node
        while current.left_child:
            current = current.left_child
        return current

    def _remove_node(self, node, isbn):
        if not node:
            return node

        if isbn < node.isbn:
            node.left_child = self._remove_node(node.left_child, isbn)
        elif isbn > node.isbn:
            node.right_child = self._remove_node(node.right_child, isbn)
        else:
            if not node.left_child:
                return node.right_child
            if not node.right_child:
                return node.left_child

            successor = self._get_min_val_node(node.right_child)
            node.isbn, node.title = successor.isbn, successor.title
            node.right_child = self._remove_node(node.right_child, successor.isbn)

        return node

    def show(self):
        books = []
        self._inorder_walk(self.tree_root, books.append)
        if not books:
            print("No books in library")
        else:
            print("Books:")
            print("\n".join(books))

    def _inorder_walk(self, node, callback):
        if node:
            self._inorder_walk(node.left_child, callback)
            callback(f"{node.isbn} {node.title}")
            self._inorder_walk(node.right_child, callback)


def process_commands():
    bst = RecursiveBST()
    while True:
        try:
            line = input().strip()
            if not line:
                continue

            parts = line.split()
            cmd = parts[0]

            if cmd == "exit":
                break
            if cmd == "add":
                bst.add(int(parts[1]), parts[2])
            elif cmd == "find":
                bst.find(int(parts[1]))
            elif cmd == "remove":
                bst.remove(int(parts[1]))
            elif cmd == "show":
                bst.show()
            else:
                print("invalid input")
        except (ValueError, IndexError):
            print("invalid input")
        except EOFError:
            break


if __name__ == "__main__":
    process_commands()
