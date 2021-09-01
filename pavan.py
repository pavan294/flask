import sqlite3
conn = sqlite3.connect('pavan.db')
c = conn.cursor()
# c.execute(""" CREATE TABLE employees (
#         first text,
#         last text,
#         pay integer
# )""")
#c.execute("INSERT INTO employees VALUES('Suresh','Kumar',3000)")
c.execute("SELECT * FROM employees where last='kaki'")
print(c.fetchone())
conn.commit()
conn.close()