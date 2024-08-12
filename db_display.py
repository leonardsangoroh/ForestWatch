import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('instance/events.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Execute a query to retrieve all data from the Event table
cursor.execute("SELECT * FROM event")

# Fetch all rows from the query result
rows = cursor.fetchall()

# Print each row
for row in rows:
    print(row)

# Close the connection
conn.close()
