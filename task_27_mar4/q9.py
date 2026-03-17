

from csv import DictReader

fr = open("task_27_mar4\\move.csv","r")
fw = open("task_27_mar4\\sorted_movies.csv","w")

data = list(DictReader(fr))

print(data[0])

movie_names_list = [m.get("Name") for m in data]

print(movie_names_list)

movie_names_list.sort(reverse=True)

print(movie_names_list)

for i in movie_names_list:

    fw.write(i + "\n")


