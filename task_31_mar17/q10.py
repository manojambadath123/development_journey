
#shallow copy
from copy import deepcopy,copy

numbers1 = [10,20,30,40]


numbers2 = copy(numbers1)


print(numbers1)
print(numbers2)

print(id(numbers1))
print(id(numbers2))

#deep copy

from copy import deepcopy,copy

numbers1 = [10,20,30,40]


numbers2 = deepcopy(numbers1)


print(numbers1)
print(numbers2)

print(id(numbers1))
print(id(numbers2))