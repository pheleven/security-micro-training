"""Reproduce nine local assertions for reviewed release exercise repairs."""
import json
import sqlite3

db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE people (name TEXT)")
db.execute("INSERT INTO people VALUES ('Ada'), ('O''Brien')")

def lookup(name):
    return db.execute(
        "SELECT name FROM people WHERE name = ?", (name,)
    ).fetchall()

assert lookup("Ada") == [("Ada",)]
assert lookup("' OR '1'='1") == []
assert lookup("O'Brien") == [("O'Brien",)]
name = "D'Angelo"
db.execute("INSERT INTO people (name) VALUES (?)", (name,))
assert lookup(name) == [("D'Angelo",)]

db.execute("CREATE TABLE invoices (id INTEGER, note TEXT)")
db.executemany("INSERT INTO invoices VALUES (?, ?)", [(42, "old"), (43, "unchanged")])
saved_note = "Approved'; --"
db.execute("UPDATE invoices SET note = ? WHERE id = ?", (saved_note, 42))
assert db.execute("SELECT note FROM invoices WHERE id = 42").fetchone() == (saved_note,)
assert db.execute("SELECT note FROM invoices WHERE id = 43").fetchone() == ("unchanged",)

db.execute("CREATE TABLE customers (id INTEGER, name TEXT)")
db.executemany("INSERT INTO customers VALUES (?, ?)", [(1, "Ada"), (2, "O'Neil")])

def customer_lookup(conn, name):
    sql = "SELECT id FROM customers WHERE name = ?"
    return conn.execute(sql, (name,)).fetchall()

assert customer_lookup(db, "Ada") == [(1,)]
assert customer_lookup(db, "O'Neil") == [(2,)]
assert customer_lookup(db, "Nobody' OR '1'='1") == []
db.close()
print(json.dumps({"assertions_passed": 9, "scope": "Original in-memory fixtures; hands-on repair, insertion transfer, invoice review, and skipped exercise repair"}, indent=2))
