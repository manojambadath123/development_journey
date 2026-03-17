
mark = int(input("enter your marks="))

if mark>=90:
    print(mark,"is distinction")
elif mark>=60 and mark<90:
    print(mark,"is first class")
elif mark>=40 and mark<60:
    print(mark,"is pass")
elif mark<40:
    print(mark,"is fail")
