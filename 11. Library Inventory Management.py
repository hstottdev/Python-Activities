import numpy as np

class Book:
    def __init__ (self, title,author,availability):
        self.title = title
        self.author = author
        self.availability = availability
        
#declare empty array of books
books = np.empty(0,Book)

def addBook(book):
    return np.append(books,book)
    

def findBookRecord(title):
    for book in books:
        if(book.title == title):
            print("found book")
            return book
    return None

def userCheckInBook():
    title = input("Hello, which book are you checking in?: ")
    #check if the library has record of the book
    checkedInBook = findBookRecord(title)

    #mark book as now available
    if(checkedInBook != None):
        checkedInBook = lambda book : setattr(book, True, availability)
    else:
        #there is no record of this book, we need more info from the user.
        author = input("Sorry, we don't know that book. \n Who is the author?: ")
        checkedInBook = Book(title,author,True)
        books = addBook(checkedInBook)
    
    print("Thank you. \n\n{0} by {1} is now checked into the library.".format(checkedInBook.title,checkedInBook.author))

def userCheckOutBook():
    title = input("Hello, which book would you like to take?: ")
    checkedOutBook = findBookRecord(title)

    #mark book as now unavailable
    if(checkedOutBook != None):
        checkedOutBook = lambda book : setattr(book, False, availability)
    else:
        author = input("Sorry, we don't have that book.")

def searchForBook():
    option = input("""Would you like to search by:
1. book title
2. book author

""")
    if(option == "1"):
        title = input("\nwhich book TITLE would you like to search for?: ")
        filterSetting = lambda book: book.title.lower() == title.lower()
    else:
        author = input("\nwhich book AUTHOR would you like to search for?: ")
        filterSetting = lambda book: book.author.lower() == author.lower()
    results = list(filter(filterSetting, books))
    print("\n{0} results:".format(len(results)))
    for book in results:
        print("\n{0} by {1}\n Available: {2}".format(book.title,book.author,book.availability))

def main():
    choice = input("""\nWelcome to the Library,

What would you like to do?:

    1. Take out a book
    2. Check in a book
    3. Search for a book
    4. Exit the library
    
    """)
    if(choice == "1"):
        userCheckOutBook()
    elif(choice == "2"):
        userCheckInBook()
    elif(choice == "3"):
        searchForBook()
    elif(choice == "4"):
        print("\nThank you for coming, Goodbye!")
        return
    main()

hello = np.empty(0,str)

books = addBook(Book("War Horse","Michael Morpurgo",True))
books = addBook(Book("Born to Run","Michael Morpurgo",True))
books = addBook(Book("A Critical Analysis of This Book","H.G Stott",False))
books = addBook(Book("Harry Potter and the Deathly Hallows","J.K Rowling",True))

main()
        
