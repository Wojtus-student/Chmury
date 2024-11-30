from flask import Flask, request, jsonify, render_template
from neo4j import GraphDatabase

app = Flask(__name__)

# Neo4j configuration
uri = "neo4j+ssc://af4ae13c.databases.neo4j.io"
username = "neo4j"
password = "uxIzr3XjB7RXu8wsIeYO_E8OTKfZhxdnRZwlUicNdLU"
driver = GraphDatabase.driver(uri, auth=(username, password))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_author', methods=['POST'])
def add_author():
    data = request.json
    name = data['name']
    with driver.session() as session:
        session.run("CREATE (a:Author {name: $name})", name=name)
    return jsonify({"message": "Author added!"})

@app.route('/add_book', methods=['POST'])
def add_book():
    data = request.json
    title = data['title']
    year = data.get('year', 'Unknown')
    with driver.session() as session:
        session.run("CREATE (b:Book {title: $title, year: $year})", title=title, year=year)
    return jsonify({"message": "Book added!"})

@app.route('/link_author_book', methods=['POST'])
def link_author_book():
    data = request.json
    author = data['author']
    book = data['book']
    with driver.session() as session:
        session.run("""
            MATCH (a:Author {name: $author}), (b:Book {title: $book})
            CREATE (b)-[:WRITTEN_BY]->(a)
        """, author=author, book=book)
    return jsonify({"message": "Author linked to book!"})

@app.route('/get_books_by_author/<author>', methods=['GET'])
def get_books_by_author(author):
    with driver.session() as session:
        result = session.run("""
            MATCH (a:Author {name: $author})<-[:WRITTEN_BY]-(b:Book)
            RETURN b.title AS title, b.year AS year
        """, author=author)
        books = [{"title": record["title"], "year": record["year"]} for record in result]
    return jsonify(books)

if __name__ == '__main__':
    app.run(debug=True)
