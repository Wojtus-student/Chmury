from neo4j import GraphDatabase, exceptions

# Neo4j configuration
uri = "neo4j+ssc://af4ae13c.databases.neo4j.io"
username = "neo4j"
password = "uxIzr3XjB7RXu8wsIeYO_E8OTKfZhxdnRZwlUicNdLU"

# Utworzenie sterownika połączenia
driver = GraphDatabase.driver(uri, auth=(username, password))

try:
    with driver.session() as session:
        # Testowe zapytanie
        result = session.run("RETURN 1 AS test")
        record = result.single()
        if record:
            print("Połączenie udane!")
            print("Wynik testu: ", record["test"])
        else:
            print("Brak wyniku!")
except exceptions.ServiceUnavailable as e:
    print(f"Błąd połączenia z bazą Neo4j: {e}")
except Exception as e:
    print(f"Inny błąd: {e}")
finally:
    driver.close()
