from collections import deque
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer

    BFS,loop per lelvel
    """
    def ladderLength(self, start, end, dict):
        
        dict.add(end)
        visited = set([start])
        queue = deque([start])
        distance={start:1}

        while queue:

            word = queue.popleft()
            if word == end:
                return distance[word]

            for new_word in self.get_next_word(word):
                if new_word not in dict or new_word in visited:
                    continue

                queue.append(new_word)
                visited.add(new_word)
                distance[new_word] = distance[word]+1


    def get_next_word(self,word):

        words=[]
        for i in range(len(word)):
            part1,part2= word[:i],word[i+1:]

            for char in 'abcdefghijklmnopqrstuvwxyz':

                if char == word[i]:
                    continue
                new_word = part1 + char +part2

                words.append(new_word)

        return words
