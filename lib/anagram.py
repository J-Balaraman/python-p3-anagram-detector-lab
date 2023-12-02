class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, list):
        new_list = []
        for l in list:
            if sorted(self.word) == sorted(l):
                new_list.append(l)
        return new_list