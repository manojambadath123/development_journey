

def skill_set_extract(message):

    result=""

    fr = open("error_handling\\skill_set.txt","r")

    skill_words = [line.rstrip("\n") for line in fr]

    for w in message.split(" "):

        if w in skill_words:

            result+=w+" "

    # cleaned_word = [w for w in message.split(" ") if w in skill_words]

    # result = " ".join(cleaned_word)

    return result


print(skill_set_extract("Python Java is programming language"))