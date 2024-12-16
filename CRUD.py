import sqlite3

conn = sqlite3.connect('example.db') 
c = conn.cursor()

# Deleting a record
c.execute("DELETE FROM employees WHERE EmployeeID = 1")
conn.commit()
conn.close()
