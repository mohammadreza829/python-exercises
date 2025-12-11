users = {
    "Ali": ["ورزش", "تکنولوژی", "سینما", "سفر"],
    "Sara": ["سفر", "تکنولوژی", "تاریخ", "موسیقی"],
    "Reza": ["ورزش", "سینما", "سفر", "طبیعت"],
    "Niloofar": ["موسیقی", "نقاشی", "سینما", "تکنولوژی"],
}

new_interests_str = input().strip()

new_interests = [item.strip() for item in new_interests_str.split(",") if item.strip()]
new_set = set(new_interests)

def jaccard(a_list, b_set):
    a_set = set(a_list)
    inter = len(a_set & b_set)
    union = len(a_set | b_set)
    if union == 0:
        return 0.0
    return inter / union

best_user = None
best_score = -1.0

for name, interests in users.items():
    score = jaccard(interests, new_set)
    if score > best_score:
        best_score = score
        best_user = name

best_score_rounded = round(best_score + 1e-8, 2)

print(f"User is most similar to: {best_user} (Similarity: {best_score_rounded:.2f})")
