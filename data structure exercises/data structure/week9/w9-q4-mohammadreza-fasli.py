users = [
    ("Ali", ["ورزش", "تکنولوژی", "سینما", "سفر"]),
    ("Sara", ["سفر", "تکنولوژی", "تاریخ", "موسیقی"]),
    ("Reza", ["ورزش", "سینما", "سفر", "طبیعت"]),
    ("Niloofar", ["موسیقی", "نقاشی", "سینما", "تکنولوژی"]),
]

inp = input().strip()
inp = inp.replace(",", "،")

new_user = set(
    interest for interest in map(str.strip, inp.split("،")) if interest != ""
)

best_user = ""
best_similarity = -1.0

for user, interests in users:
    interests_set = set(interests)
    inter = new_user & interests_set
    uni = new_user | interests_set
    similarity = 0.0 if len(uni) == 0 else len(inter) / len(uni)

    if similarity > best_similarity:
        best_similarity = similarity
        best_user = user

print(f"User is most similar to: {best_user} (Similarity: {best_similarity:.2f})")
