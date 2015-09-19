class Library(object):
    """Create a new library object"""
    def __init__(self):
        self.shelves = []
        self.books = []

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

    def remove_from_shelf(self, shelf, book):
        """Removes book from shelf"""
        shelf.books.remove(book)

    def num_shelves(self):
        """Counts the number of shelves in the library"""
        return len(self.shelves)


class Shelf(object):
    """Create a shelf within the Library"""
    def __init__(self, name):
        self.name = name
        self.books = []

    def __str__(self):
        contents = ""
        for book in self.books:
            contents += str(book) + ", "
        return "The " + self.name + " shelf contains: \n" + contents


class Book(object):
    """Creates a new book including book title and author"""
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return self.title + " written by " + self.author


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
    # add scifi shelf to library
    issaquah_public.new_shelf(scifi)
    # create a new book
    wwz = Book("World War Z", "Max Brooks")
    # add world war z to science fiction shelf
    issaquah_public.return_to_shelf(scifi, wwz)
    # Print number of shelves in the library
    print("There are %s shelves in the library.\n"
          % issaquah_public.num_shelves())
    # print library
    print(issaquah_public)
    # remove Theory of Wing Selections from aerospace shelf
    issaquah_public.remove_from_shelf(aerospace, tows)
    print(aerospace)
