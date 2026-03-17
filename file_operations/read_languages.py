
fr = open("file_operations\\languages.txt","r")

for line in fr:

    print(line.rstrip("\n"))