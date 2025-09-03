class Flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word + '(' + self.meaning + ')'
f = []
print ("Welcome to flashcard application")
while True:
    word = input("Enter a word: ")
    meaning = input("Enter its meaning: ")
    f.append(Flashcard(word, meaning))
    i = int(input("Enter 0 to continue, Enter 1 to stop"))
    if i:
        break
print("Your flashcards are:")
for j in f:
    print(j)