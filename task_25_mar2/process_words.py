

fr = open("task_25_mar2\\words.txt","r")

words_list = [line.rstrip("\n") for line in fr]

print(words_list)

words_count = {w:words_list.count(w) for w in words_list}

print(words_count)


