

from csv import DictReader

fr = open("task_27_mar4\\move.csv","r")

data = list(DictReader(fr))

movie_count = len([m.get("Name") for m in data])

print(movie_count)