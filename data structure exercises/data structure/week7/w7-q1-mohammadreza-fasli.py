# -*- coding: utf-8 -*-

class BookManager:
    """
    یک نسخه تغییر یافته از درخت جستجوی دودویی.
    این نسخه شامل یک باگ عمدی در متد حذف است.
    """
    
    class Book:
        """کلاس داخلی برای نمایش گره‌های درخت."""
        def __init__(self, isbn, title):
            self.isbn = isbn
            self.title = title
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def add_book(self, isbn, title):
        """افزودن کتاب به صورت تکراری (iterative)."""
        new_book = self.Book(isbn, title)
        if not self.root:
            self.root = new_book
            print(f"Book {isbn} {title} added")
            return

        node = self.root
        while node:
            if isbn < node.isbn:
                if not node.left:
                    node.left = new_book
                    print(f"Book {isbn} {title} added")
                    return
                node = node.left
            elif isbn > node.isbn:
                if not node.right:
                    node.right = new_book
                    print(f"Book {isbn} {title} added")
                    return
                node = node.right
            else:
                print("Book already exists")
                return

    def find_book(self, isbn):
        """جستجوی کتاب و نمایش مسیر."""
        node = self.root
        path_str = []
        while node:
            path_str.append(str(node.isbn))
            if isbn == node.isbn:
                print(f"Found: {node.isbn} {node.title}")
                print(f"Path: {', '.join(path_str)}")
                return
            elif isbn < node.isbn:
                node = node.left
            else:
                node = node.right
        print("Not found")

    def remove_book(self, isbn):
        """حذف کتاب به صورت تکراری با یک باگ عمدی."""
        parent = None
        node = self.root
        while node and node.isbn != isbn:
            parent = node
            if isbn < node.isbn:
                node = node.left
            else:
                node = node.right

        if not node:
            print("Book not found")
            return

        book_title = node.title

        # حالت ۱ و ۲: گره یک فرزند یا هیچ فرزندی ندارد
        if not node.left or not node.right:
            child = node.left if node.left else node.right
            if not parent:
                self.root = child
            elif parent.left == node:
                parent.left = child
            else:
                parent.right = child
        # حالت ۳: گره دو فرزند دارد
        else:
            successor_parent = node
            successor = node.right
            while successor.left:
                successor_parent = successor
                successor = successor.left
            
            # کپی کردن اطلاعات جانشین
            node.isbn = successor.isbn
            node.title = successor.title
            
            # **!!! باگ عمدی !!!**
            # زیردرخت راستِ گره جانشین به درستی متصل نمی‌شود و از دست می‌رود.
            # کد صحیح باید `successor.right` را به جای گره جانشین قرار دهد.
            if successor_parent.left == successor:
                successor_parent.left = None  # به جای successor.right
            else:
                successor_parent.right = None # به جای successor.right

        print(f"Book {isbn} {book_title} removed")

    def display_all(self):
        """نمایش تمام کتاب‌ها با پیمایش میان‌ترتیب."""
        if not self.root:
            print("No books in library")
            return
            
        print("Books:")
        self._display_recursive(self.root)

    def _display_recursive(self, node):
        if node:
            self._display_recursive(node.left)
            print(f"{node.isbn} {node.title}")
            self._display_recursive(node.right)


def run_manager():
    """حلقه اصلی برای اجرای دستورات."""
    manager = BookManager()
    while True:
        try:
            command_line = input()
            if not command_line: continue
            
            tokens = command_line.split()
            cmd = tokens[0]

            if cmd == "exit": break
            elif cmd == "add": manager.add_book(int(tokens[1]), tokens[2])
            elif cmd == "find": manager.find_book(int(tokens[1]))
            elif cmd == "remove": manager.remove_book(int(tokens[1]))
            elif cmd == "show": manager.display_all()
            else: print("invalid input")

        except (IndexError, ValueError):
            print("invalid input")
        except EOFError:
            break

if __name__ == "__main__":
    run_manager()

