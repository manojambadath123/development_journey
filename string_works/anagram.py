

word1 = "silent" #eilnts sort it first and check whether they are same then it is an anagram

word2 = "listen" #eilnts

is_anagram = True

for ch in word1:

    if word2.find(ch)==-1:

        is_anagram=False
        break

    else:

        is_anagram=True

print(is_anagram)