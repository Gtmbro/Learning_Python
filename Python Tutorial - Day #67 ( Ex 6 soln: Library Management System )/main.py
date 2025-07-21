class Library:
  def __init__(self, books=None):
    self.books = books if books else []

  @property
  def Books_Count(self):
    return len(self.books)

  def adder(self, book, author):
    self.books.append({"book":book,"author":author})
    
  
  def ShowInfo(self):
    for count, item in enumerate (self.books, start=1):
      print(f"\nFor book no.{count} {item['book']}, author is: {item['author']}")

library = Library()

decision = input("Enter y to add info: ").lower()

while decision == "y":
  book = input("\nEnter book: ").capitalize()
  author = input("\nEnter author: ").capitalize()

  if not book and not author:
    break
    
  library.adder(book, author)
  decision = input("\nEnter y again to add info: ").lower()

if not library.books:
  exit()
  
print(f"\nYou added {library.Books_Count} books in total")
library.ShowInfo()
