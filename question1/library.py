class Library(object):
    """Create a new library object"""
    def __init__(self):
        self.shelves = []
        self.books = []

    def add_shelf(self, shelf):
        """Add shelf to library"""
        self.shelves.append(shelf)

    def return_to_shelf(self, shelf, book):
        """returns a book to a shelf"""
        shelf.books.append(book)


class Shelf(object):
    """Create a shelf within the Library"""
    def __init__(self, name):
        self.name = name


class Book(object):
    """Creates a new book including book title and author"""
    def __init__(self, title, author):
        self.title = title
        self.author = author
