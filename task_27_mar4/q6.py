

from csv import DictReader

fr = open("task_27_mar4\\move.csv","r")

data = list(DictReader(fr))

print(data)

movie_genre = input("enter a genre=")

movie_names = [m.get("Name") for m in data if m.get("Movie Categories")==movie_genre]

print(movie_names)