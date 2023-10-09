# your code goes here!

word =["enlists", "google", "facebook", "inlets", "things"]


class Anagram:
    
    def __init__(self, sent):
        self.word = sent
        
    def match(self, word_list):
        sorted_word = sorted(self.word)
        return [word for word in word_list if sorted(word) == sorted_word]
        
        
        
        


listen = Anagram("facebook")
print(listen.match(word))
