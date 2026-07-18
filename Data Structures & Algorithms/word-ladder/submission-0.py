class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)

        if endWord not in words:
            return 0

        queue = deque([(beginWord, 1)])

        while queue:
            word, sequence_length = queue.popleft()

            if word == endWord:
                return sequence_length

            word_chars = list(word)

            for index in range(len(word_chars)):
                original_char = word_chars[index]

                for char_code in range(ord("a"), ord("z") + 1):
                    new_char = chr(char_code)

                    if new_char == original_char:
                        continue

                    word_chars[index] = new_char
                    next_word = "".join(word_chars)

                    if next_word in words:
                        words.remove(next_word)
                        queue.append((next_word, sequence_length + 1))

                word_chars[index] = original_char

        return 0