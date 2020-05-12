class Library:

    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks

    def displayAvailbleBooks(self):
        print()
        print("Available Books: ")
        for book in self.availableBooks:
            print(book)

    def lendBook(self, requestedBook):
        if requestedBook in self.availableBooks:
            print("You have now borrowed the book")
            self.availableBooks.remove(requestedBook)
        else:
            print("SOrry the book is not availble")

    def addBook(self, returnedBook):
        self.availableBooks.append(returnedBook)
        print("Thank you for returning the book")

class Customer:
    def requestBook(self):
        print("Enter the book that you would like to borrow")
        self.book = input()
        return self.book

    def returnBook(self):
        print("Enter the book you want to return")
        self.book = input()
        return self.book

library = Library(['think and Grow', 'Who will cry', 'For one More Day'])
customer = Customer()

while True:
    print("Enter 1 to display the availble books")
    print("Enter 2 to request for a book")
    print("Enter 3 to return a book")
    print("Enter 4 to exit")
    userChoice = int(input())
    if userChoice == 1:
        library.displayAvailbleBooks()
    elif userChoice == 2:
        requestedBook = customer.requestBook()
        library.lendBook(requestedBook)
    elif userChoice == 3:
        returnBook = customer.returnBook()
        library.addBook(returnBook)
    elif userChoice == 4:
        quit()