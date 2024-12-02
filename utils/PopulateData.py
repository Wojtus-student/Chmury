from neo4j import GraphDatabase

class Database:
    def __init__(self, uri, username, password):
        self.driver = GraphDatabase.driver(uri, auth=(username, password))

    def close(self):
        self.driver.close()

    def add_author(self, name):
        with self.driver.session() as session:
            session.run("CREATE (a:Author {name: $name})", name=name)

    def add_book(self, title, year):
        with self.driver.session() as session:
            session.run("CREATE (b:Book {title: $title, year: $year})", title=title, year=year)

    def link_author_book(self, author, book):
        with self.driver.session() as session:
            session.run("""
                MATCH (a:Author {name: $author}), (b:Book {title: $book})
                CREATE (b)-[:WRITTEN_BY]->(a)
            """, author=author, book=book)

# Neo4j configuration
uri = "neo4j+ssc://af4ae13c.databases.neo4j.io"
username = "neo4j"
password = "uxIzr3XjB7RXu8wsIeYO_E8OTKfZhxdnRZwlUicNdLU"
db = Database(uri, username, password)

# Sample data
authors = [
    "J.K. Rowling", "George R.R. Martin", "J.R.R. Tolkien", "Agatha Christie", "Stephen King",
    "Isaac Asimov", "Arthur C. Clarke", "Philip K. Dick", "Ray Bradbury", "H.G. Wells",
    "Ernest Hemingway", "F. Scott Fitzgerald", "Mark Twain", "Charles Dickens", "Jane Austen",
    "Leo Tolstoy", "Fyodor Dostoevsky", "Gabriel Garcia Marquez", "Haruki Murakami", "J.D. Salinger",
    "Kurt Vonnegut", "Aldous Huxley", "George Orwell", "Virginia Woolf", "James Joyce"
]

books = [
    {"title": "Harry Potter and the Philosopher's Stone", "year": 1997},
    {"title": "A Game of Thrones", "year": 1996},
    {"title": "The Hobbit", "year": 1937},
    {"title": "Murder on the Orient Express", "year": 1934},
    {"title": "The Shining", "year": 1977},
    {"title": "Foundation", "year": 1951},
    {"title": "2001: A Space Odyssey", "year": 1968},
    {"title": "Do Androids Dream of Electric Sheep?", "year": 1968},
    {"title": "Fahrenheit 451", "year": 1953},
    {"title": "The War of the Worlds", "year": 1898},
    {"title": "The Old Man and the Sea", "year": 1952},
    {"title": "The Great Gatsby", "year": 1925},
    {"title": "Adventures of Huckleberry Finn", "year": 1884},
    {"title": "A Tale of Two Cities", "year": 1859},
    {"title": "Pride and Prejudice", "year": 1813}
]

# Add authors
for author in authors:
    db.add_author(author)

# Add books
for book in books:
    db.add_book(book["title"], book["year"])

# Link authors to books
links = [
    ("J.K. Rowling", "Harry Potter and the Philosopher's Stone"),
    ("George R.R. Martin", "A Game of Thrones"),
    ("J.R.R. Tolkien", "The Hobbit"),
    ("Agatha Christie", "Murder on the Orient Express"),
    ("Stephen King", "The Shining"),
    ("Isaac Asimov", "Foundation"),
    ("Arthur C. Clarke", "2001: A Space Odyssey"),
    ("Philip K. Dick", "Do Androids Dream of Electric Sheep?"),
    ("Ray Bradbury", "Fahrenheit 451"),
    ("H.G. Wells", "The War of the Worlds"),
    ("Ernest Hemingway", "The Old Man and the Sea"),
    ("F. Scott Fitzgerald", "The Great Gatsby"),
    ("Mark Twain", "Adventures of Huckleberry Finn"),
    ("Charles Dickens", "A Tale of Two Cities"),
    ("Jane Austen", "Pride and Prejudice")
]

for author, book in links:
    db.link_author_book(author, book)

# New sample data
new_authors = [
    "Neil Gaiman", "Terry Pratchett", "Douglas Adams", "Jules Verne"
]

new_books = [
    {"title": "Good Omens", "year": 1990},
    {"title": "American Gods", "year": 2001},
    {"title": "The Hitchhiker's Guide to the Galaxy", "year": 1979},
    {"title": "Twenty Thousand Leagues Under the Sea", "year": 1870}
]

# Add new authors
for author in new_authors:
    db.add_author(author)

# Add new books
for book in new_books:
    db.add_book(book["title"], book["year"])

# Link new authors to books
new_links = [
    ("Neil Gaiman", "Good Omens"),
    ("Terry Pratchett", "Good Omens"),
    ("Neil Gaiman", "American Gods"),
    ("Douglas Adams", "The Hitchhiker's Guide to the Galaxy"),
    ("Jules Verne", "Twenty Thousand Leagues Under the Sea")
]

for author, book in new_links:
    db.link_author_book(author, book)

# Additional links between old and new authors and books
additional_links = [
    ("Neil Gaiman", "Harry Potter and the Philosopher's Stone"),
    ("Terry Pratchett", "A Game of Thrones"),
    ("Douglas Adams", "The Hobbit"),
    ("Jules Verne", "The War of the Worlds"),
    ("Isaac Asimov", "Good Omens"),
    ("Arthur C. Clarke", "American Gods"),
    ("Philip K. Dick", "The Hitchhiker's Guide to the Galaxy"),
    ("Ray Bradbury", "Twenty Thousand Leagues Under the Sea"),
    ("H.G. Wells", "Foundation"),
    ("Ernest Hemingway", "2001: A Space Odyssey"),
    ("George Orwell", "The Shining"),
    ("Virginia Woolf", "Murder on the Orient Express"),
    ("James Joyce", "The Great Gatsby"),
    ("Gabriel Garcia Marquez", "Adventures of Huckleberry Finn"),
    ("Haruki Murakami", "A Tale of Two Cities"),
    ("J.K. Rowling", "Good Omens"),
    ("George R.R. Martin", "American Gods"),
    ("J.R.R. Tolkien", "The Hitchhiker's Guide to the Galaxy"),
    ("Agatha Christie", "Twenty Thousand Leagues Under the Sea"),
    ("Stephen King", "The Great Gatsby"),
    ("Isaac Asimov", "Harry Potter and the Philosopher's Stone"),
    ("Arthur C. Clarke", "A Game of Thrones"),
    ("Philip K. Dick", "The Hobbit"),
    ("Ray Bradbury", "Murder on the Orient Express"),
    ("H.G. Wells", "The Shining"),
    ("Ernest Hemingway", "Foundation"),
    ("F. Scott Fitzgerald", "2001: A Space Odyssey"),
    ("Mark Twain", "Do Androids Dream of Electric Sheep?"),
    ("Charles Dickens", "Fahrenheit 451"),
    ("Jane Austen", "The War of the Worlds"),
    ("Leo Tolstoy", "Good Omens"),
    ("Fyodor Dostoevsky", "American Gods"),
    ("Gabriel Garcia Marquez", "The Hitchhiker's Guide to the Galaxy"),
    ("Haruki Murakami", "Twenty Thousand Leagues Under the Sea"),
    ("J.D. Salinger", "The Great Gatsby"),
    ("Kurt Vonnegut", "The Hobbit"),
    ("Aldous Huxley", "Harry Potter and the Philosopher's Stone"),
    ("George Orwell", "A Game of Thrones"),
    ("Virginia Woolf", "The Shining"),
    ("James Joyce", "Murder on the Orient Express"),
    ("Neil Gaiman", "Foundation"),
    ("Terry Pratchett", "2001: A Space Odyssey"),
    ("Douglas Adams", "Do Androids Dream of Electric Sheep?"),
    ("Jules Verne", "Fahrenheit 451"),
    ("Isaac Asimov", "The War of the Worlds"),
    ("Arthur C. Clarke", "Good Omens"),
    ("Philip K. Dick", "American Gods"),
    ("Ray Bradbury", "The Hitchhiker's Guide to the Galaxy"),
    ("H.G. Wells", "Twenty Thousand Leagues Under the Sea"),
    ("Ernest Hemingway", "The Great Gatsby"),
    ("F. Scott Fitzgerald", "The Hobbit"),
    ("Mark Twain", "Harry Potter and the Philosopher's Stone"),
    ("Charles Dickens", "A Game of Thrones"),
    ("Jane Austen", "The Shining"),
    ("Leo Tolstoy", "Murder on the Orient Express"),
    ("Fyodor Dostoevsky", "Foundation"),
    ("Gabriel Garcia Marquez", "2001: A Space Odyssey"),
    ("Haruki Murakami", "Do Androids Dream of Electric Sheep?"),
    ("J.D. Salinger", "Fahrenheit 451"),
    ("Kurt Vonnegut", "The War of the Worlds"),
    ("Aldous Huxley", "Good Omens"),
    ("George Orwell", "American Gods"),
    ("Virginia Woolf", "The Hitchhiker's Guide to the Galaxy"),
    ("James Joyce", "Twenty Thousand Leagues Under the Sea"),
    ("Neil Gaiman", "The Great Gatsby"),
    ("Terry Pratchett", "The Hobbit"),
    ("Douglas Adams", "Harry Potter and the Philosopher's Stone"),
    ("Jules Verne", "A Game of Thrones"),
    ("Isaac Asimov", "The Shining"),
    ("Arthur C. Clarke", "Murder on the Orient Express"),
    ("Philip K. Dick", "Foundation"),
    ("Ray Bradbury", "2001: A Space Odyssey"),
    ("H.G. Wells", "Do Androids Dream of Electric Sheep?"),
    ("Ernest Hemingway", "Fahrenheit 451"),
    ("F. Scott Fitzgerald", "The War of the Worlds"),
    ("Mark Twain", "Good Omens"),
    ("Charles Dickens", "American Gods"),
    ("Jane Austen", "The Hitchhiker's Guide to the Galaxy"),
    ("Leo Tolstoy", "Twenty Thousand Leagues Under the Sea"),
    ("Fyodor Dostoevsky", "The Great Gatsby"),
    ("Gabriel Garcia Marquez", "The Hobbit"),
    ("Haruki Murakami", "Harry Potter and the Philosopher's Stone"),
    ("J.D. Salinger", "A Game of Thrones"),
    ("Kurt Vonnegut", "The Shining"),
    ("Aldous Huxley", "Murder on the Orient Express"),
    ("George Orwell", "Foundation"),
    ("Virginia Woolf", "2001: A Space Odyssey"),
    ("James Joyce", "Do Androids Dream of Electric Sheep?"),
    ("Neil Gaiman", "Fahrenheit 451"),
    ("Terry Pratchett", "The War of the Worlds"),
    ("Douglas Adams", "Good Omens"),
    ("Jules Verne", "American Gods"),
    ("Isaac Asimov", "The Hitchhiker's Guide to the Galaxy"),
    ("Arthur C. Clarke", "Twenty Thousand Leagues Under the Sea"),
    ("Philip K. Dick", "The Great Gatsby"),
    ("Ray Bradbury", "The Hobbit"),
    ("H.G. Wells", "Harry Potter and the Philosopher's Stone"),
    ("Ernest Hemingway", "A Game of Thrones"),
    ("F. Scott Fitzgerald", "The Shining"),
    ("Mark Twain", "Murder on the Orient Express"),
    ("Charles Dickens", "Foundation"),
    ("Jane Austen", "2001: A Space Odyssey"),
    ("Leo Tolstoy", "Do Androids Dream of Electric Sheep?"),
    ("Fyodor Dostoevsky", "Fahrenheit 451"),
    ("Gabriel Garcia Marquez", "The War of the Worlds"),
    ("Haruki Murakami", "Good Omens"),
    ("J.D. Salinger", "American Gods"),
    ("Kurt Vonnegut", "The Hitchhiker's Guide to the Galaxy"),
    ("Aldous Huxley", "Twenty Thousand Leagues Under the Sea"),
    ("George Orwell", "The Great Gatsby"),
    ("Virginia Woolf", "The Hobbit"),
    ("James Joyce", "Harry Potter and the Philosopher's Stone"),
    ("Neil Gaiman", "A Game of Thrones"),
    ("Terry Pratchett", "The Shining"),
    ("Douglas Adams", "Murder on the Orient Express"),
    ("Jules Verne", "Foundation"),
    ("Isaac Asimov", "2001: A Space Odyssey"),
    ("Arthur C. Clarke", "Do Androids Dream of Electric Sheep?"),
    ("Philip K. Dick", "Fahrenheit 451"),
    ("Ray Bradbury", "The War of the Worlds"),
    ("H.G. Wells", "Good Omens"),
    ("Ernest Hemingway", "American Gods"),
    ("F. Scott Fitzgerald", "The Hitchhiker's Guide to the Galaxy"),
    ("Mark Twain", "Twenty Thousand Leagues Under the Sea"),
    ("Charles Dickens", "The Great Gatsby"),
    ("Jane Austen", "The Hobbit"),
    ("Leo Tolstoy", "Harry Potter and the Philosopher's Stone"),
    ("Fyodor Dostoevsky", "A Game of Thrones"),
    ("Gabriel Garcia Marquez", "The Shining"),
    ("Haruki Murakami", "Murder on the Orient Express"),
    ("J.D. Salinger", "Foundation"),
    ("Kurt Vonnegut", "2001: A Space Odyssey"),
    ("Aldous Huxley", "Do Androids Dream of Electric Sheep?"),
    ("George Orwell", "Fahrenheit 451"),
    ("Virginia Woolf", "The War of the Worlds"),
    ("James Joyce", "Good Omens"),
    ("Neil Gaiman", "American Gods"),
    ("Terry Pratchett", "The Hitchhiker's Guide to the Galaxy"),
    ("Douglas Adams", "Twenty Thousand Leagues Under the Sea"),
    ("Jules Verne", "The Great Gatsby"),
    ("Isaac Asimov", "The Hobbit"),
    ("Arthur C. Clarke", "Harry Potter and the Philosopher's Stone"),
    ("Philip K. Dick", "A Game of Thrones"),
    ("Ray Bradbury", "The Shining"),
    ("H.G. Wells", "Murder on the Orient Express"),
    ("Ernest Hemingway", "Foundation"),
    ("F. Scott Fitzgerald", "2001: A Space Odyssey"),
    ("Mark Twain", "Do Androids Dream of Electric Sheep?"),
    ("Charles Dickens", "Fahrenheit 451"),
    ("Jane Austen", "The War of the Worlds"),
    ("Leo Tolstoy", "Good Omens"),
    ("Fyodor Dostoevsky", "American Gods"),
    ("Gabriel Garcia Marquez", "The Hitchhiker's Guide to the Galaxy"),
    ("Haruki Murakami", "Twenty Thousand Leagues Under the Sea"),
    ("J.D. Salinger", "The Great Gatsby"),
    ("Kurt Vonnegut", "The Hobbit"),
    ("Aldous Huxley", "Harry Potter and the Philosopher's Stone"),
    ("George Orwell", "A Game of Thrones"),
    ("Virginia Woolf", "The Shining"),
    ("James Joyce", "Murder on the Orient Express")
]

for author, book in additional_links:
    db.link_author_book(author, book)

db.close()