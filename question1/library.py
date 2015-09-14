class Library(object):
    """Create a new library object"""
    def __init__(self):
        self.shelves = []
        self.books = []
        self.customers = []

    def __str__(self):
        contents = ""
        for books in self.shelves:
            contents += str(books)
        return contents

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

    def add_customer(self, customer):
        """adds a customer to the library"""
        self.customers.append(customer)

    def remove_customer(self, customer):
        """removes a customer from the library"""
        try:
            self.customers.remove(customer)
        except ValueError:
            print("That customer was not found in our system.")


class Shelf(object):
    """Create a shelf within the Library"""
    def __init__(self, name):
        self.name = name
        self.books = []

    def __str__(self):
        contents = ""
        for book in self.books:
            contents += str(book)
        return "The " + self.name + " shelf contains the following books: \n"
        + contents


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


if __name__ == '__main__':
    # create a new library
    issaquah_public = Library()
    # create a new shelf in the issaquah_public library
    aerospace = Shelf("Aerospace")
    # create a new book
    tows = Book("Theory of Wing Sections", "Ira Abbott")
    # create a new book
    blt = Book("Boundry Layer Theory", "Hermann Schlichting")
    # add aerospace shelf to library
    issaquah_public.new_shelf(aerospace)
    # add theory of wing sections to aerospace shelf
    issaquah_public.return_to_shelf(aerospace, tows)
    # add boundry layer theory to aerospace shelf
    issaquah_public.return_to_shelf(aerospace, blt)
    # create a new shelf in the issaquah_public library
    scifi = Shelf("Science Fiction")
    # create a new book
    wwz = Book("World War Z", "Max Brooks")
    # add world war z to science fiction shelf
    issaquah_public.return_to_shelf(scifi, wwz)
    # print library
    print(issaquah_public)
    # create a new customer
    andrew = Customer("Andrew Prince")
    # add customer to library
    issaquah_public.add_customer(andrew)
