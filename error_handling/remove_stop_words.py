

# def remove_stop_words(word):

#     fr = open("error_handling\\stop_words.txt","r")

#     result = ""

   

# stop_words = [line.rstrip("\n") for line in fr]

# for w in word.split(" "):

#     if w not in stop_words:

#          result+=w + " "


# return result


# print(remove_stop_words("machine learning is a subset of AI"))




def remove_stop_words(sentence):

    fr = open("error_handling\\stop_words.txt","r")

    result = ""

    

    stop_words = [line.rstrip("\n") for line in fr]

    for w in sentence.split(" "):

        if w not in stop_words:

             result+=w+" "


    return result

sentence = "machine learning is a subset of AI"

print(remove_stop_words(sentence))


assert remove_stop_words(sentence)=="machine learning subset AI" ,"testcase1 failed"

print("code accepted")




# def remove_stop_words(sentence):

#     fr = open("error_handling\\stop_words.txt","r")

#     result = ""


#     stop_words = [line.rstrip("\n") for line in fr]

#     cleaned_word = [w for w in sentence.split(" ") if w not in stop_words]

#     result = " ".join(cleaned_word)

#     return result

        

# sentence1 = "machine learning is a subset of AI"

# sentence2 = "django is a one of python framework"

# print(remove_stop_words(sentence1))
# print(remove_stop_words(sentence2))

# assert remove_stop_words(sentence1)=="machine learning subset AI","testcase1 failed"
# assert remove_stop_words(sentence2)=="django one python framework","testcase2 failed"

# print("code accepted")