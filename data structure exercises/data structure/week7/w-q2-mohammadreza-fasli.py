class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


def insert_word(root, word):
    node = root
    for char in word:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
    node.is_end_of_word = True


def _dfs_get_words(node, prefix, words_list):
    if node.is_end_of_word:
        words_list.append(prefix)

    for char in sorted(node.children.keys()):
        _dfs_get_words(node.children[char], prefix + char, words_list)


def get_words_starting_with(root, letter):
    words = []
    if letter in root.children:

        _dfs_get_words(root.children[letter], letter, words)
    return words


longest_chain_found = []


def backtrack(current_chain, used_words, trie_root):
    global longest_chain_found

    if len(current_chain) > len(longest_chain_found):
        longest_chain_found = current_chain.copy()

    elif len(current_chain) == len(longest_chain_found):
        if " ".join(current_chain) < " ".join(longest_chain_found):
            longest_chain_found = current_chain.copy()

    last_word = current_chain[-1]
    last_char = last_word[-1]

    candidate_words = get_words_starting_with(trie_root, last_char)

    for next_word in candidate_words:
        if next_word not in used_words:
            used_words.add(next_word)
            current_chain.append(next_word)

            backtrack(current_chain, used_words, trie_root)

            current_chain.pop()
            used_words.remove(next_word)


def find_longest_chain(start_word, all_words):
    global longest_chain_found

    trie_root = TrieNode()
    for word in all_words:
        insert_word(trie_root, word)

    if start_word not in all_words:
        return [start_word]

    used_words = {start_word}
    current_chain = [start_word]
    longest_chain_found = [start_word]

    backtrack(current_chain, used_words, trie_root)

    return longest_chain_found


if __name__ == "__main__":

    try:
        N = int(input())
        word_list = [input() for _ in range(N)]
        start = input()

        result_chain = find_longest_chain(start, set(word_list))
        print(" ".join(result_chain))

    except (IOError, ValueError):

        word_list = ["apple", "ear", "rat", "tiger", "rhino", "orange"]
        start = "apple"

        result_chain = find_longest_chain(start, set(word_list))
        print(" ".join(result_chain))
