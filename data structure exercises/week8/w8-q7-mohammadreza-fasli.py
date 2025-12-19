def count_accepted(desc_scores, limit):
    left, right = 0, len(desc_scores) - 1
    last_ok = -1

    while left <= right:
        mid = (left + right) // 2
        if desc_scores[mid] >= limit:
            last_ok = mid
            left = mid + 1
        else:
            right = mid - 1

    return last_ok + 1

if __name__ == "__main__":
    line = input().strip()
    scores = list(map(int, line.split())) if line else []

    minimum_required = int(input().strip())

    result = count_accepted(scores, minimum_required)
    print(result)
