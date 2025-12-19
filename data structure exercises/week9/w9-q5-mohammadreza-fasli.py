user_hashes = {
    "X": ["Sports Shoes", "Backpack", "Headphones"],   
    "A": ["Headphones", "Jacket", "Headphones"],
    "B": ["Backpack", "Hiking Shoes", "Headphones"],
    "C": ["Backpack", "Hiking Shoes", "Sports Shoes"]
}

hx1, hx2, hx3 = user_hashes["X"]

def similarity_with(user):
    h1, h2, h3 = user_hashes[user]
    equal_count = 0
    if h1 == hx1:
        equal_count += 1
    if h2 == hx2:
        equal_count += 1
    if h3 == hx3:
        equal_count += 1
    return equal_count / 3

best_user = None
best_sim = -1.0

for u in ["A", "B", "C"]:
    sim = similarity_with(u)
    if sim > best_sim:
        best_sim = sim
        best_user = u

print(f"User {best_user}")
