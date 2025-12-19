
from collections import defaultdict
class PathFinder:

    def __init__(self, words):
        self.word_map = defaultdict(list)
        for word in words:
            self.word_map[word[0]].append(word)

        for key in self.word_map:
            self.word_map[key].sort()
            
        self.optimal_path = []

    def _search(self, path, visited):

        if len(path) > len(self.optimal_path):
            self.optimal_path = list(path)
        elif len(path) == len(self.optimal_path) and " ".join(path) < " ".join(self.optimal_path):
            self.optimal_path = list(path)


        last_char = path[-1][-1]
        for candidate in self.word_map.get(last_char, []):
            if candidate not in visited:
                visited.add(candidate)
                path.append(candidate)
                self._search(path, visited)
                path.pop()
                visited.remove(candidate)

    def find_path(self, start_word):

        if start_word not in self.word_map.get(start_word[0], []):
            return [start_word]
        
        self.optimal_path = [start_word]
        self._search([start_word], {start_word})
        return self.optimal_path


if __name__ == "__main__":
    num_words = int(input())
    word_list = {input() for _ in range(num_words)}
    start_node = input()


    finder = PathFinder(word_list)
    result = finder.find_path(start_node)
    
    print(" ".join(result))

