# -*- coding: utf-8 -*-

class BookNode:
    """
    کلاسی برای نمایش یک گره در درخت جستجوی دودویی.
    هر گره نمایانگر یک کتاب با شناسه (ISBN) و عنوان است.
    """
    def __init__(self, isbn, title):
        self.isbn = isbn
        self.title = title
        self.left = None
        self.right = None

class LibraryBST:
    """
    کلاسی برای پیاده‌سازی درخت جستجوی دودویی برای مدیریت کتابخانه.
    این کلاس شامل متدهایی برای افزودن، حذف، جستجو و نمایش کتاب‌هاست.
    """
    def __init__(self):
        self.root = None

    def add(self, isbn, title):
        """افزودن یک کتاب جدید به درخت."""
        if self.root is None:
            self.root = BookNode(isbn, title)
            return f"Book {isbn} {title} added"
        
        current = self.root
        while True:
            if isbn < current.isbn:
                if current.left is None:
                    current.left = BookNode(isbn, title)
                    return f"Book {isbn} {title} added"
                current = current.left
            elif isbn > current.isbn:
                if current.right is None:
                    current.right = BookNode(isbn, title)
                    return f"Book {isbn} {title} added"
                current = current.right
            else:  # ISBN تکراری
                return "Book already exists"

    def find(self, isbn):
        """جستجوی یک کتاب بر اساس ISBN و نمایش مسیر."""
        path = []
        current = self.root
        while current:
            path.append(str(current.isbn))
            if isbn < current.isbn:
                current = current.left
            elif isbn > current.isbn:
                current = current.right
            else:  # پیدا شد
                return f"Found: {current.isbn} {current.title}\nPath: {', '.join(path)}"
        return "Not found"

    def remove(self, isbn):
        """حذف یک کتاب از درخت."""
        # ابتدا گره را پیدا می‌کنیم تا عنوان آن را برای پیام خروجی داشته باشیم
        node_to_remove = self._find_node_for_removal(isbn)
        if not node_to_remove:
            return "Book not found"
        
        title = node_to_remove.title
        self.root = self._remove_recursive(self.root, isbn)
        return f"Book {isbn} {title} removed"

    def _find_node_for_removal(self, isbn):
        """یک تابع کمکی برای پیدا کردن گره جهت حذف."""
        node = self.root
        while node:
            if isbn < node.isbn:
                node = node.left
            elif isbn > node.isbn:
                node = node.right
            else:
                return node
        return None

    def _find_min_node(self, node):
        """پیدا کردن کوچکترین گره در یک زیردرخت (جانشین پیش‌ترتیب)."""
        current = node
        while current and current.left:
            current = current.left
        return current

    def _remove_recursive(self, node, isbn):
        """تابع بازگشتی برای حذف گره."""
        if node is None:
            return node

        if isbn < node.isbn:
            node.left = self._remove_recursive(node.left, isbn)
        elif isbn > node.isbn:
            node.right = self._remove_recursive(node.right, isbn)
        else:
            # حالت ۱: گره برگ یا یک فرزند دارد
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # حالت ۲: گره دو فرزند دارد
            temp = self._find_min_node(node.right)
            node.isbn = temp.isbn
            node.title = temp.title
            node.right = self._remove_recursive(node.right, temp.isbn)
            
        return node

    def show(self):
        """نمایش تمام کتاب‌ها به ترتیب ISBN با پیمایش میان‌ترتیب."""
        if self.root is None:
            return "No books in library"
        
        result_lines = []
        self._in_order_traversal(self.root, result_lines)
        return "Books:\n" + "\n".join(result_lines)

    def _in_order_traversal(self, node, result_lines):

        if node:
            self._in_order_traversal(node.left, result_lines)
            result_lines.append(f"{node.isbn} {node.title}")
            self._in_order_traversal(node.right, result_lines)

def main():

    library = LibraryBST()
    while True:
        try:
            line = input()
            if not line.strip():
                continue
            
            parts = line.strip().split()
            command = parts[0]

            if command == "exit" and len(parts) == 1:
                break
            elif command == "add" and len(parts) == 3:
                print(library.add(int(parts[1]), parts[2]))
            elif command == "find" and len(parts) == 2:
                print(library.find(int(parts[1])))
            elif command == "remove" and len(parts) == 2:
                print(library.remove(int(parts[1])))
            elif command == "show" and len(parts) == 1:
                print(library.show())
            else:
                print("invalid input")
        
        except (ValueError, IndexError):
            print("invalid input")
        except EOFError:
            break

if __name__ == "__main__":
    main()

