

# def cube(num):

#     result =27
#     # result = num**3

#     return result


# assert cube(3)==27 ,"test case1 failed" # assert condition ,"error message"
# assert cube(4)==64 ,"test case2 failed"

# print("code accepted")


def max_two(n1,n2):

    if n1>n2:

        result = n1

    else:

        result = n2

    return result

assert max_two(10,20)==20 , "test case1 failed"
assert max_two(-10,5)==5 , "test case2 failed"


print("code accepted")