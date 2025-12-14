users = [
    ("Ali", ["ورزش", "تکنولوژی", "سینما", "سفر"]),
    ("Sara", ["سفر", "تکنولوژی", "تاریخ", "موسیقی"]),
    ("Reza", ["ورزش", "سینما", "سفر", "طبیعت"]),
    ("Niloofar", ["موسیقی", "نقاشی", "سینما", "تکنولوژی"])
]

s = input().strip().replace(",", "،")
parts = s.split("،")

new_user = set()
for p in parts:
    p = p.strip()
    if p != "":
        new_user.add(p)

best_name = ""
best_sim = -1.0

for name, interests in users:
    a = set(interests)
    inter = 0
    union = set()

    for x in a:
        if x in new_user:
            inter += 1
        union.add(x)
    for x in new_user:
        union.add(x)

    sim = 0.0 if len(union) == 0 else inter / len(union)

    if sim > best_sim:
        best_sim = sim
        best_name = name

print(f"User is most similar to: {best_name} (Similarity: {best_sim:.2f})")
