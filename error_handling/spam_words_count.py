

def spam_words_count(message):

    count=0

    fr = open("error_handling\\spam_words.txt","r")

    spam_words = [line.rstrip("\n") for line in fr]

    for w in message.split(" "):

        if w in spam_words:

            count+=1

    return count



print(spam_words_count("bonus cash manoj debt"))