
book_objs_list = []

class Library:
  no_of_books = 0
  def __init__(self, book, author):
    self.book = book
    self.author = author
    # self.books_list = []
    Library.no_of_books += 1
  
  def show_book(self):
    return self.book
    
  def show_author(self):
    return self.author

  def show_no_of_books(self):
    return self.no_of_books

  def length_book(self):
    return len(self.book)

  def length_author(self):
    return len(self.author)

#Adder for adding books
def adder(item):
  book_objs_list.append(item)

#------------------User Input Section-----------------------
decision = input("Enter 'y' to add information and anything else to exit: ").lower()

while decision == "y":
  book_name = input("\nEnter the name of the book: ").capitalize()
  author = input(f"\nEnter the name of the author of {book_name}: ").capitalize()

  book_obj = Library(book_name, author)
  adder(book_obj)

  decision = input("\nEnter 'y' to add information again\n"
                   "Anything else to exit: ").lower()

#-------------------------EXECUTION------------------------------
number = Library.no_of_books

if not book_objs_list:
  exit()
elif number == 1:
  print("\nYou have added 1 book in total.\n")
elif number != 1:
  print(f"\nYou have added {number} books in total.\n")


max_l_book = max(a.length_book() for a in book_objs_list)
max_l_author = max(a.length_author() for a in book_objs_list)

print(f"| {'Book':<{max_l_book}} | {'Author':<{max_l_author}} |")
print("-"*(max_l_book + max_l_author + 9))

#--------------------------Result---------------------------------
for book in book_objs_list:
  print(f"| {book.show_book():<{max_l_book}} | {book.show_author():<{max_l_author}} |")
