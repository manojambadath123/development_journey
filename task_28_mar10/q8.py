

class Book:

    def __init__(self,title,author):

        self.title=title
        self.author=author

    def display(self):

        print(self.title,self.author)


book_instance = Book("kerala varma pazhassi raja","M.T.vasudevan nair")

book_instance.display()