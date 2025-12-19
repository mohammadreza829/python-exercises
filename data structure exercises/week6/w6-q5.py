class TreeTraversal:
    def __init__(self, arr):
        self.data = arr

    def traverse_pre(self, idx):
        if idx >= len(self.data) or self.data[idx] is None:
            return []

        res = [self.data[idx]]
        l = 2 * idx + 1
        r = 2 * idx + 2

        res.extend(self.traverse_pre(l))
        res.extend(self.traverse_pre(r))

        return res

    def traverse_mid(self, idx):
        if idx >= len(self.data) or self.data[idx] is None:
            return []

        l = 2 * idx + 1
        r = 2 * idx + 2

        res = self.traverse_mid(l)
        res.append(self.data[idx])
        res.extend(self.traverse_mid(r))

        return res

    def traverse_post(self, idx):
        if idx >= len(self.data) or self.data[idx] is None:
            return []

        l = 2 * idx + 1
        r = 2 * idx + 2

        res = self.traverse_post(l)
        res.extend(self.traverse_post(r))
        res.append(self.data[idx])

        return res


inp = (
    input()
    .replace(",", " ")
    .replace("[", " ")
    .replace("]", " ")
    .replace("'", "")
    .split()
)

tree_data = []
for t in inp:
    if t.lower() == "none":
        tree_data.append(None)
    elif t:
        tree_data.append(t)

tt = TreeTraversal(tree_data)

pre = tt.traverse_pre(0)
In_o = tt.traverse_mid(0)
post = tt.traverse_post(0)

print("In_Order: [" + ", ".join(In_o) + "]")
print("Pre_Order: [" + ", ".join(pre) + "]")
print("Post_Order: [" + ", ".join(post) + "]")
