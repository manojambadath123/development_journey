


sentence = "python is a programming programming is language"

word = sentence.split(" ")

print(word)

word_count = {w:word.count(w) for w in word}

print(word_count)