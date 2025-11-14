# -*- coding: utf-8 -*-

# گره درخت به صورت یک دیکشنری ساده نمایش داده می‌شود
def create_node(isbn, title):
    return {"isbn": isbn, "title": title, "left": None, "right": None}

def insert_node(root, isbn, title):
    if not root:
        print(f"Book {isbn} {title} added")
        return create_node(isbn, title)
    
    node = root
    while True:
        if isbn < node["isbn"]:
            if not node["left"]:
                node["left"] = create_node(isbn, title)
                print(f"Book {isbn} {title} added")
                break
            node = node["left"]
        elif isbn > node["isbn"]:
            if not node["right"]:
                node["right"] = create_node(isbn, title)
                print(f"Book {isbn} {title} added")
                break
            node = node["right"]
        else:
            print("Book already exists")
            break
    return root

def search_node(root, isbn):
    node = root
    path = []
    while node:
        path.append(str(node["isbn"]))
        if isbn == node["isbn"]:
            print(f"Found: {node['isbn']} {node['title']}")
            print(f"Path: {', '.join(path)}")
            return
        node = node["left"] if isbn < node["isbn"] else node["right"]
    print("Not found")

def delete_node(root, isbn):
    parent, node = None, root
    while node and node["isbn"] != isbn:
        parent = node
        node = node["left"] if isbn < node["isbn"] else node["right"]

    if not node:
        print("Book not found")
        return root

    print(f"Book {node['isbn']} {node['title']} removed")
    
    # مدیریت حذف
    if not node["left"] or not node["right"]:
        child = node["left"] or node["right"]
        if not parent: return child
        if parent["left"] == node: parent["left"] = child
        else: parent["right"] = child
    else:
        succ_parent, succ = node, node["right"]
        while succ["left"]:
            succ_parent, succ = succ, succ["left"]
        
        node["isbn"], node["title"] = succ["isbn"], succ["title"]
        if succ_parent["left"] == succ: succ_parent["left"] = succ["right"]
        else: succ_parent["right"] = succ["right"]
        
    return root

def display_inorder(root):
    if not root:
        print("No books in library")
        return
        
    stack, books_output = [], []
    node = root
    print("Books:")
    while stack or node:
        while node:
            stack.append(node)
            node = node["left"]
        node = stack.pop()
        books_output.append(f"{node['isbn']} {node['title']}")
        node = node["right"]
    print("\n".join(books_output))


def main_loop():
    """حلقه اصلی برای پردازش دستورات با رویکرد تابعی."""
    library_root = None
    while True:
        try:
            line = input()
            if not line.strip(): continue
            parts = line.split()
            command = parts[0]
            
            if command == "exit": break
            if command == "add" and len(parts) == 3:
                library_root = insert_node(library_root, int(parts[1]), parts[2])
            elif command == "find" and len(parts) == 2:
                search_node(library_root, int(parts[1]))
            elif command == "remove" and len(parts) == 2:
                library_root = delete_node(library_root, int(parts[1]))
            elif command == "show" and len(parts) == 1:
                display_inorder(library_root)
            else:
                print("invalid input")
        except (ValueError, IndexError):
            print("invalid input")
        except EOFError:
            break

if __name__ == "__main__":
    main_loop()

