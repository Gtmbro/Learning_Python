
class Library:
  def __init__(self, books=None):
    self.books = books if books else []

  @property
  def number(self):
    return (len(self.books))

  def add_books(self, book):
    self.books.append(book)

  def show_books(self):
    print("List of books are: ")
    for book in self.books:
      print(f"- {book}")

library = Library()

decision = input("Enter Y to add book: ").strip().lower()
while decision == "y":
  book = input("\nEnter the name of the book: ").strip().capitalize()
  library.add_books(book)
  decision = input("\nEnter Y to add book again: ").strip().lower()

print("\nHere are the books:\n")
library.show_books()
print(f"\nYou added {library.number} books in total.")
