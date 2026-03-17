

from csv import DictReader
fr=open("task_27_mar4\\move.csv","r")
fw = open("task_27_mar4\\top_rated.csv","w")

data = list(DictReader(fr))

print(data)

movie_names = [m.get("Name") for m in data if float(m.get("Rating"))>8.0]

print(movie_names)

for i in movie_names:

    fw.write(i + "\n")

    
# fw.write(movie_names +"\n")



