def build_trie_from_dict(words):

    trie_root = {}
    for word in words:
        node = trie_root
        for char in word:

            node = node.setdefault(char, {})
        node["_end_"] = True
    return trie_root


def find_words_from_trie_node(node, prefix, results):

    if node.get("_end_"):
        results.append(prefix)

    for char, child_node in sorted(node.items()):
        if char != "_end_":
            find_words_from_trie_node(child_node, prefix + char, results)


def find_longest_chain_iterative(start_word, all_words):

    if start_word not in all_words:
        return [start_word]

    trie = build_trie_from_dict(all_words)

    stack = [([start_word], {start_word})]

    best_path = [start_word]

    while stack:
        current_path, visited_words = stack.pop()

        if len(current_path) > len(best_path):
            best_path = list(current_path)
        elif len(current_path) == len(best_path) and " ".join(current_path) < " ".join(
            best_path
        ):
            best_path = list(current_path)

        last_word = current_path[-1]
        last_char = last_word[-1]

        candidate_node = trie.get(last_char)

        if candidate_node:
            candidate_words = []
            find_words_from_trie_node(candidate_node, last_char, candidate_words)

            for word in reversed(candidate_words):
                if word not in visited_words:
                    new_path = current_path + [word]
                    new_visited = visited_words.union({word})
                    stack.append((new_path, new_visited))

    return best_path


if __name__ == "__main__":

    try:
        n_str = input()
        if n_str:
            num_words = int(n_str)
            word_set = {input() for _ in range(num_words)}
            start_word = input()

            final_chain = find_longest_chain_iterative(start_word, word_set)
            print(" ".join(final_chain))

    except (ValueError, IndexError) as e:

        pass
