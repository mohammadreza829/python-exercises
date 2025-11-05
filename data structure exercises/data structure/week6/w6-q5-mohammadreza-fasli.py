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

tokens = (
    user_input.replace(",", " ")
    .replace("[", " ")
    .replace("]", " ")
    .replace("'", "")
    .split()
)

tree_array = []
for token in tokens:
    if token.lower() == "none":
        tree_array.append(None)
    elif token:
        tree_array.append(token)

bt = BinaryTree(tree_array)


in_result = bt.inorder(0)
pre_result = bt.preorder(0)
post_result = bt.postorder(0)

print("In_Order: [" + ", ".join(in_result) + "]")
print("Pre_Order: [" + ", ".join(pre_result) + "]")
print("Post_Order: [" + ", ".join(post_result) + "]")
