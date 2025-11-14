from collections import defaultdict


def create_lookup(words):

    lookup = defaultdict(list)
    for word in words:
        lookup[word[0]].append(word)
    for key in lookup:
        lookup[key].sort()
    return lookup


def chain_generator(path, visited, lookup):

    yield list(path)

    last_char = path[-1][-1]
    candidates = lookup.get(last_char, [])

    for candidate_word in candidates:
        if candidate_word not in visited:
            visited.add(candidate_word)
            path.append(candidate_word)

            yield from chain_generator(path, visited, lookup)
            path.pop()
            visited.remove(candidate_word)


def solve_using_generator(start, words):

    if start not in words:
        return [start]

    word_lookup = create_lookup(words)
    best_chain_so_far = []

    initial_path = [start]
    initial_visited = {start}
    all_possible_chains = chain_generator(initial_path, initial_visited, word_lookup)

    for chain in all_possible_chains:
        if not best_chain_so_far:
            best_chain_so_far = chain
            continue

        if len(chain) > len(best_chain_so_far):
            best_chain_so_far = chain
        elif len(chain) == len(best_chain_so_far):
            if " ".join(chain) < " ".join(best_chain_so_far):
                best_chain_so_far = chain

    return best_chain_so_far


if __name__ == "__main__":
    n = int(input())
    words_set = {input() for _ in range(n)}
    start_word = input()

    final_result = solve_using_generator(start_word, words_set)
    print(" ".join(final_result))
