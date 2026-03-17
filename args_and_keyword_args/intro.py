"""
*args recieves any number of parameter as tuple
"""

def add(*args): # args =(10,20,30)

    # args => will be of type tuple

    return sum(args)

# print(add(10,20))
# print(add(10,20,30))


def largest_number(*args):

    return max(args)

# print(largest_number(10,20))
# print(largest_number(10,20,30))


def count_evens(*args):

    count=0

    for num in args:

        if num%2==0:

          count+=1

    return count


# print(count_evens(10,11,12,13))



def count_of_evens(*args):

    evens = [num for num in args if num%2==0]

    print(evens)

    return len(evens)

# print(count_of_evens(10,11,12,13))



def count_odds(*args):

    count=0

    for num in args:

        if num%2!=0:

          count+=1

    return count


# print(count_odds(10,11,12,13))


def count_of_odds(*args):

    odds = [num for num in args if num%2!=0]

    print(odds)


    return len(odds)


# print(count_of_odds(10,11,12,13))

def product_of_nums(*args:tuple):

    product=1

    for num in args:

        product*=num

    return product

# print(product_of_nums(1,2,3))


