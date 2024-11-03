# library management system

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def displayinfo(self):
        return f"Title: {self.title}, Author: {self.author}"
 # child class/derived- inheriting traits
class LibraryBook(Book):
     def __init__(self, title, author, isbn, copies_available):
         # inheriting
         super().__init__(title, author)
         self.isbn = isbn
         self.copies_available = copies_available
     def borrow_book(self):
         # use if statement to check copies available
         if self.copies_available > 0:
             self.copies_available-=1
             return f"{self.title} borrowed. Copies left: {self.copies_available}"
         else:
             return f"No of Title {self.title} available"
     def return_book(self):
         self.copies_available+=1
         return f"{self.title} returned. Copies left: {self.copies_available}"

# usage example
# instance of the class
book1=LibraryBook("Blossoms", "Maina Kimani", 548892749, 18)
print(book1.displayinfo())
# borrowing a book
print(book1.borrow_book())

print(book1.borrow_book())
# return book
print(book1.return_book())