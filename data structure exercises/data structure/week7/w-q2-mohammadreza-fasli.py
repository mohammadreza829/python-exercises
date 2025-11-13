class WordChainSolver:
    def __init__(self):
        self.trie_root = self.TrieNode()
        self.longest_chain = []

    class TrieNode:
        def __init__(self):
            self.children = {}
            self.is_end_of_word = False

    def insert_word(self, word):
        node = self.trie_root
        for char in word:
            if char not in node.children:
                node.children[char] = self.TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def _dfs_get_words(self, node, prefix, words_list):
        if node.is_end_of_word:
            words_list.append(prefix)
        for char in sorted(node.children.keys()):
            self._dfs_get_words(node.children[char], prefix + char, words_list)

    def get_words_starting_with(self, letter):
        words = []
        if letter in self.trie_root.children:
            self._dfs_get_words(self.trie_root.children[letter], letter, words)
        return words

    def _backtrack(self, current_chain, used_words):
        if len(current_chain) > len(self.longest_chain):
            self.longest_chain = list(current_chain)
        elif len(current_chain) == len(self.longest_chain):
            if " ".join(current_chain) < " ".join(self.longest_chain):
                self.longest_chain = list(current_chain)

        last_word = current_chain[-1]
        last_char = last_word[-1]
        candidate_words = self.get_words_starting_with(last_char)

        for next_word in candidate_words:
            if next_word not in used_words:
                used_words.add(next_word)
                current_chain.append(next_word)
                self._backtrack(current_chain, used_words)
                current_chain.pop()
                used_words.remove(next_word)

    def find_longest_chain(self, start_word, all_words):
        for word in all_words:
            self.insert_word(word)

        if start_word not in all_words:
            return [start_word]

        self.longest_chain = [start_word]
        used_words = {start_word}

        self._backtrack([start_word], used_words)
        return self.longest_chain


if __name__ == "__main__":

    N = int(input())
    word_list = {input() for _ in range(N)}
    start = input()

    solver = WordChainSolver()
    result_chain = solver.find_longest_chain(start, word_list)

    print(" ".join(result_chain))
