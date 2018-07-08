# User class
class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("The email for user " + self.name + " has been updated to: " + self.email)

    def __repr__(self):
        return self.name + " Email: " + self.email + " Books read: " + str(len(self.books))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        return False

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        average = 0
        books_rated = 0
        for value in self.books.values():
            if value:
                average += value
                books_rated += 1
        average = average/books_rated
        return average

# Book class
class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []
        
    def get_title(self):
        return self.title
        
    def get_isbn(self):
        return self.isbn
        
    def set_isbn(self, isbn):
        self.isbn = isbn
        print("The ISBN for book: " + self.title + " has been set to " + str(self.isbn))

    def add_rating(self, rating):
        if rating and rating > 0 and rating < 5:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def get_average_rating(self):
        avg = 0
        for rating in self.ratings:
            avg += rating
        avg = avg/len(self.ratings)
        return avg

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        else:
            return False

    def __hash__(self):
        return hash((self.title, self.isbn))

# Fiction: Subclass of Book
class Fiction(Book):
    def __init__(self, title, author, isbn):
        Book.__init__(self, title, isbn)
        self.author = author
    
    def get_author(self):
        return self.author

    def __repr__(self):
        return self.title + " by " + self.author

# Non-fiction: Subclass of Book
class Non_fiction(Book):
    def __init__(self, title, subject, level, isbn):
        Book.__init__(self, title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level
    
    def __repr__(self):
        return self.title + ", a " + self.level + " manual on " + self.subject

# TomeRater class
class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        another_book = Book(title, isbn)
        return another_book

    def create_novel(self, title, author, isbn):
        another_book = Fiction(title, author, isbn)
        return another_book

    def create_non_fiction(self, title, subject, level, isbn):
        another_book = Non_fiction(title, subject, level, isbn)
        return another_book

    def add_book_to_user(self, book, email, rating = None):
        user = self.users.get(email, None)
        if user:
            user.read_book(book, rating)
            if book not in self.books:
                self.books[book] = 0
            self.books[book] += 1
            book.add_rating(rating)
        else:
            print("No user exists with email " + email)

    def add_user(self, name, email, user_books = None):
        another_user = User(name, email)
        self.users[email] = another_user
        if user_books:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for book in self.books:
            print(book)

    def print_users(self):
        for user in self.users:
            print(user)

    def highest_rated_book(self):
        highest_rated = float("-inf")
        highest_rated_book = None
        for book in self.books:
            average = book.get_average_rating()
            if average > highest_rated:
                highest_rated = average
                highest_rated_book = book
        return highest_rated_book

    def most_positive_user(self):
        highest_rated = float("-inf")
        highest_rater = None
        for user in self.users.values():
            average = user.get_average_rating()
            if average > highest_rated:
                highest_rated = average
                highest_rater = user
        return highest_rater
