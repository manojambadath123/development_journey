


num = int(input("enter a number="))

previous = 0
current=1
next=previous+current

while(num<=next):

    previous=current
    current=next
    next = previous + current

    print(next)

