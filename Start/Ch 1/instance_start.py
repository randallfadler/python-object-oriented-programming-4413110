# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes

class Publication:
    def  __init__(self, title, price):
        self.title = title
        self.price = price

class Periodical(Publication): 
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher

class Book(Publication):
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        super().__init__(title,price)
        self.author =  author
        self.price = price
        self.__secret = "This is a hidden  attribute in Book"

class Magazine(Periodical):
    def __init__(self, title, publisher, price, period, photographer):
        super().__init__(title, price, period, publisher)
        self.photographer = photographer
        self.__secret = "This is a hidden attribute in Magazine"
    
    def get_photographer(self):
        return self.photographer 
    
    def  set_photographer(self, photographer):
        self.photographer = photographer

class Newspaper(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, period, publisher)
        self.__secret = "This is a hidden attribute in Newspaper"

# TODO: create some book instances
b1 = Book("War and Peace",  "Leo Tolstoy", 1225, 15.99)
n1 = Newspaper("NY Times",  "New York Times Company", 6.0, "Daily")
m1 = Magazine("Scientific American", "Springer Nature", 5.9,  "Monthly", "Stacy Jones")

# print (b1.title)
# print  (n1.publisher)
# print (b1.price, m1.price, n1.price)
# print (b1._Book__secret)
p = (m1.get_photographer)
print (p)
m1.set_photographer("Jason Perry")
p = (m1.get_photographer)
print (p)
