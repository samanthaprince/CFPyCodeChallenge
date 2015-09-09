class Library(object):
    """Create a new library object"""
    def __init__(self):
        self.shelves = []
        self.books = []
        self.customers = []

    def new_shelf(self, shelf):
        """Add shelf to library"""
        self.shelves.append(shelf)

    def return_to_shelf(self, shelf, book):
        """Puts a book on a shelf already in library"""
        shelf.books.append(book)

    def check_out_book(self, book, customer):
        """Checks a book out of the library to a specific customer and
        makes book unavilable for others to check out"""
        try:
            if book.available:
                customer.checked_out_books.append(book)
                book.avaiable = False
            else:
                print(book.title + " is not available at this time. "
                      + "Try selecting another book instead. ")
        except:
            print("We do not have that book in our collection.")


class Shelf(object):
    """Create a shelf within the Library"""
    def __init__(self, name):
        self.name = name


class Book(object):
    """Creates a new book including book title and author"""
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True


class Customer(object):
    def __init__(self, name):
        self.name = name
        self.checked_out_books = []

    def __str__(self):
        checkedout = ""
        for checked_out_books in self.checked_out_books:
            checkedout += str(checked_out_books) + ", "
        return self.name + " has the following books checked out: \n"
        + checkedout
