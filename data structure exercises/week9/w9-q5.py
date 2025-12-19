hx = input().strip().split()

users = {
    "A": ["Headphones", "Jacket", "Headphones"],
    "B": ["Backpack", "Hiking Shoes", "Headphones"],
    "C": ["Backpack", "Hiking Shoes", "Sports Shoes"]
}

def jaccard_est(user_name):
    user_hash = users[user_name]
    same = sum(1 for a, b in zip(user_hash, hx) if a == b)
    return same / 3

scores = [(user, jaccard_est(user)) for user in users.keys()]

best_user, best_score = max(scores, key=lambda x: x[1])

print(f"User {best_user}")
