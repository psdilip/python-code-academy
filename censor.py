def censor(text, word):
    #want to replace only the letters of the word with asterick
    #dont touch anything else

    #How do you not touch anything else?
    #How do you select the word, and replace all its characters
    # if word in text:
    #     print(word)
    new = text.split()
    # if word in new:
    #     print(word)
    for t in new:
        if t == word:
            text = text.replace(t,"*"*len(word))
    print(text)

        # print(word)
    #     for i in word:
    #         text = text.replace(word, "*")
    # print(text)

# def censor2(text,word):
#     for t in word:
#     print(text)



text = "this hack is wack hack"
word = "hack"
censor(text, word)
# censor2(text,word)

# string.split()
# and 
# " ".join(list)