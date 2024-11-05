# Python Object Oriented Programming by Joe Marini course example
# Using composition to build complex objects


class Book:
    def __init__(self, title, price, author=None):
        self.title = title
        self.price = price

        self.author = author

        self.chapters = []

    def addchapter(self, chapter):
        self.chapters.append(chapter)

    def getbookpagecount(self):
        result = 0
        for ch in self.chapters:
            result += ch.getpagecount
        return result

class Author:
    def __init__(self, fname, lname, email):
        self.fname = fname
        self.lname = lname
        self.email = email

    def __str__(self):
        return f"{self.fname} {self.lname} ({self.email})"
    
class Chapter:
    def __init__(self,name, pagecount):
        self.name = name
        self.pagecount = pagecount


author  = Author("Leo", "Tolstoy", "Tolstoy@example.com")

b1 = Book("War and Peace", 39.0, author)

b1.addchapter(Chapter("Chapter 1", 125))
b1.addchapter(Chapter("Chapter 2", 97))
b1.addchapter(Chapter("Chapter 3", 143))

print(b1.title)
print(b1.author)
