word = input("type the word: ")
inverted_word = []
aux =0 
for x in range(len(word)):
    letter = word[(len(word)-1)-aux]
    aux +=1
    inverted_word.append(letter)
    
print(inverted_word)