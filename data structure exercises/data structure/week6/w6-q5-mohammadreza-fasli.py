class BinaryTree:
    def __init__(self, tree_array):
        self.tree = tree_array

    def preorder(self, index):
        if index >= len(self.tree) or self.tree[index] is None:
            return []

        result = [self.tree[index]]
        left_index = 2 * index + 1
        right_index = 2 * index + 2

        result.extend(self.preorder(left_index))
        result.extend(self.preorder(right_index))

        return result

    def inorder(self, index):
        if index >= len(self.tree) or self.tree[index] is None:
            return []

        left_index = 2 * index + 1
        right_index = 2 * index + 2

        result = self.inorder(left_index)
        result.append(self.tree[index])
        result.extend(self.inorder(right_index))

        return result

    def postorder(self, index):
        if index >= len(self.tree) or self.tree[index] is None:
            return []

        left_index = 2 * index + 1
        right_index = 2 * index + 2

        result = self.postorder(left_index)
        result.extend(self.postorder(right_index))
        result.append(self.tree[index])

        return result

user_input = input()


tokens = user_input.split()
tree_array = []

for token in tokens:
    if token.lower() == "none":
        tree_array.append(None)
    else:
        tree_array.append(token)

bt = BinaryTree(tree_array)
print("In_Order:", bt.inorder(0))
print("Pre_Order:", bt.preorder(0))
print("Post_Order:", bt.postorder(0))
