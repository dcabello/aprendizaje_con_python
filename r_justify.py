def right_justify(word):
    word = " "*(70-len(word))+str(word)
    return word
palabra = "Toro"
print(right_justify(palabra))   