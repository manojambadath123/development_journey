

from csv import DictReader

fr = open("task_27_mar4\\move.csv","r")

data = list(DictReader(fr))

print(data)

high_rating = max([float(m.get("Rating")) for m in data ])

print(high_rating)

high_rating_movie_name = [m.get("Name") for m in data if float(m.get("Rating"))==high_rating]

print(high_rating_movie_name)