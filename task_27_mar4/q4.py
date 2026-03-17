

from csv import DictReader

fr = open("task_27_mar4\\move.csv","r")

data = list(DictReader(fr))

print(data[0])

year = int(input("enter a year="))

all_movie_titles = [m.get("Name") for m in data if int(m.get("Year of Release"))==year]

print(all_movie_titles)