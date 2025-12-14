pages = {
    "PageA": ["data", "mining", "python"],
    "PageB": ["python", "machine", "learning"],
    "PageC": ["algorithm", "data", "search"],
    "PageD": ["database", "query", "sql"],
}


def word_hash(word: str) -> int:
    total = 0
    for i, ch in enumerate(word, start=1):
        total += ord(ch) * i
    return total


def page_hash(words) -> int:
    return sum(word_hash(w) for w in words)


page_hashes = {name: page_hash(words) for name, words in pages.items()}

line = input().strip()
new_words = [w.strip() for w in line.split(",") if w.strip() != ""]
new_h = page_hash(new_words)

matched_page = None
for name, h in page_hashes.items():
    if h == new_h:
        matched_page = name
        break

if matched_page is None:
    print("No match")
else:
    print(matched_page)
