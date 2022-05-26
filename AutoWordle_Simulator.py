from random import randint

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def readWords(filename):
    with open(filename, "r") as file:
        words = []
        for line in file:
            if len(line) == 6:
                words.append(line[0:5])
        return words

def pickWord(words):
    answerWord = words[randint(0, len(words) - 1)]
    return answerWord

def guessCheck(words, answerWord, guess):
    checkedGuess = []
    for i in range(len(guess)):
        if guess[i] == answerWord[i]:
            checkedGuess.append(guess[i])
        elif guess[i] in answerWord:
            checkedGuess.append(guess[i].lower())
        else:
            checkedGuess.append("-")
    if "-" not in checkedGuess:
        return "correct"
    return "".join(checkedGuess)

def filterWords(checkedGuess, guess, words):
    words.remove(guess)
    correctLetters = list(checkedGuess)
    noDashes = []
    for letter in checkedGuess:
        if letter.upper() in ALPHABET:
            noDashes.append(letter)
    newWords1 = []
    newWords2 = []
    newWords3 = []
    newWords4 = []
    newWords5 = []
    newWords = []
    for word in words:
        for i in range(len(correctLetters)):
            if correctLetters[i] == "-":
                pass
            else:
                if correctLetters[i].isupper():
                    if correctLetters[i].upper() == word[i]:
                        if correctLetters[i] == noDashes[0]:
                            newWords1.append(word)
                        elif correctLetters[i] == noDashes[1]:
                            newWords2.append(word)
                        elif correctLetters[i] == noDashes[2]:
                            newWords3.append(word)
                        elif correctLetters[i] == noDashes[3]:
                            newWords4.append(word)
                        else:
                            newWords4.append(word)
                else:
                    if correctLetters[i].upper() in word and correctLetters[i].upper() != word[i]:
                        if correctLetters[i] == noDashes[0]:
                            newWords1.append(word)
                        elif correctLetters[i] == noDashes[1]:
                            newWords2.append(word)
                        elif correctLetters[i] == noDashes[2]:
                            newWords3.append(word)
                        elif correctLetters[i] == noDashes[3]:
                            newWords4.append(word)
                        else:
                            newWords4.append(word)
    if len(noDashes) == 2:
        newWords = list(set(newWords1) & set(newWords2))
    elif len(noDashes) == 3:
        newWords = list(set(newWords1) & set(newWords2) & set(newWords3))
    elif len(noDashes) == 4:
        newWords = list(set(newWords1) & set(newWords2) & set(newWords3) & set(newWords4))    
    elif len(noDashes) == 5:
        newWords = list(set(newWords1) & set(newWords2) & set(newWords3) & set(newWords4) & set(newWords5))
    else:
        newWords = newWords1
    if len(newWords) == 0:
        newWords = words
    return newWords
               
if __name__ == "__main__":
    words = readWords("Words.txt")
    answerWord = pickWord(words)
    done = False
    for i in range(6):
        guess = pickWord(words)
        print("GUESS " + str(i + 1) + ": " + guess)
        checkedGuess = guessCheck(words, answerWord, guess)
        if checkedGuess == "correct":
            print("Correct!")
            done = True
            break
        else:
            print("CHECK " + str(i + 1) + ": " + checkedGuess)
            words = filterWords(checkedGuess, guess, words)
    if not done:
        print("Incorrect!")
    print("ANSWER: " + answerWord)