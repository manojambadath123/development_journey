

from csv import DictReader

fr = open("task_27_mar4\\move.csv","r")

data = list(DictReader(fr))

print(data[0])

movie_category = [m.get("Movie Categories") for m in data]

print(movie_category)

movie_category_count = {c:movie_category.count(c) for c in movie_category }

print(movie_category_count)