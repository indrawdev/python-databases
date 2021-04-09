import sqlite3

conn = sqlite3.connect(':memory:')
cur = conn.cursor()

cur.execute("""CREATE TABLE Ages(name VARCHAR(128), age INTEGER)""")

cur.execute("""DELETE FROM Ages""")

def add(name, age):
	with conn:
		cur.execute("INSERT INTO Ages VALUES (:name, :age)", {'name':name, 'age':age})

people = [('Savannah', 38), ('Truli', 39), ('Malia', 26), ('Dougal', 21)]

for i in people:
	name, age = i
	add(name, age)

cur.execute("SELECT hex(name || age) AS X FROM Ages ORDER BY X")
print(cur.fetchall())

conn.commit()
conn.close()

# Then, create a SQLITE database or use an existing database and create a table in the database called "Ages":

# CREATE TABLE Ages ( 
#   name VARCHAR(128), 
#   age INTEGER
# )

# Then make sure the table is empty by deleting any rows that you previously inserted, and insert these rows and only these rows with the following commands:

# DELETE FROM Ages;
# INSERT INTO Ages (name, age) VALUES ('Savannah', 38);
# INSERT INTO Ages (name, age) VALUES ('Truli', 39);
# INSERT INTO Ages (name, age) VALUES ('Malia', 26);
# INSERT INTO Ages (name, age) VALUES ('Dougal', 21);

# Once the inserts are done, run the following SQL command:

# SELECT hex(name || age) AS X FROM Ages ORDER BY X