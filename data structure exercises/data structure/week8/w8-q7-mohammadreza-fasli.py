def count_accepted(desc_scores, limit):
    left, right = 0, len(desc_scores) - 1
    last_ok = -1

    while left <= right:
        mid = (left + right) // 2
        if desc_scores[mid] >= limit:
            # این دانشجو شرایط را دارد، سعی می‌کنیم ببینیم آیا سمت راست هم هنوز شرایط دارند یا نه
            last_ok = mid
            left = mid + 1
        else:
            # این نمره زیر حد است، باید سمت چپ را چک کنیم
            right = mid - 1

    # اگر هیچ‌کسی شرایط نداشت، last_ok = -1 → تعداد = 0
    return last_ok + 1


if __name__ == "__main__":
    line = input().strip()
    scores = list(map(int, line.split())) if line else []

    minimum_required = int(input().strip())

    result = count_accepted(scores, minimum_required)
    print(result)
