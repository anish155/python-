import sqlite3
db=sqlite3.connect("mydb.db")
cursor=db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    salary FLOAT
)
""")

cursor.execute("INSERT INTO employees (id, name, salary) VALUES (?, ?, ?)", (1, "Alice", 50000))
db.commit()

cursor.execute("SELECT * FROM employees")
for row in cursor.fetchall():
    print(row)