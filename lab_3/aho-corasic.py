from collections import deque, defaultdict


class AhoCorasick:
    def __init__(self):
        self.trie = [{}]
        self.output = defaultdict(list)
        self.fail = []

    def add_pattern(self, pattern):
        node = 0
        for char in pattern:
            if char not in self.trie[node]:
                self.trie[node][char] = len(self.trie)
                self.trie.append({})
            node = self.trie[node][char]
        self.output[node].append(pattern)

    def build(self):
        self.fail = [-1] * len(self.trie)
        queue = deque()

        for char, child in self.trie[0].items():
            self.fail[child] = 0
            queue.append(child)

        while queue:
            current = queue.popleft()

            for char, child in self.trie[current].items():
                fail = self.fail[current]
                while fail != -1 and char not in self.trie[fail]:
                    fail = self.fail[fail]
                self.fail[child] = self.trie[fail][char] if fail != -1 else 0
                self.output[child].extend(self.output[self.fail[child]])

                queue.append(child)

    def search(self, text):
        node = 0
        occurrences = []

        for i, char in enumerate(text):
            while node != -1 and char not in self.trie[node]:
                node = self.fail[node]
            if node == -1:
                node = 0
                continue
            node = self.trie[node][char]

            for pattern in self.output[node]:
                occurrences.append((i - len(pattern) + 1, pattern))

        return occurrences


# Example
ac = AhoCorasick()
wzorce = ["he", "she", "his", "hers"]
for wzorzec in wzorce:
    ac.add_pattern(wzorzec)
ac.build()

tekst = "ushers"
wyniki = ac.search(tekst)
print("Wyniki:", wyniki)
