import bisect

if __name__ == "__main__":
    first = input().strip()
    scores_desc = list(map(int, first.split())) if first else []
    limit = int(input().strip())

    scores_asc = list(reversed(scores_desc))

    pos = bisect.bisect_left(scores_asc, limit)

    count = len(scores_asc) - pos
    print(count)
