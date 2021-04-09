import sqlite3
import re

conn = sqlite3.connect("mbox.sqlite")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Counts")

cur.execute("""CREATE TABLE Counts (org TEXT, count INTEGER)""")

def add_email(email, count):
	with conn:
		cur.execute("INSERT INTO Counts VALUES (:email, :count)", {'email':email, 'count':count})

fname = input("Enter file name: ")
if len(fname) < 1:
  fname = "mbox.txt"
fh = open(fname)
content = fh.read()

results = dict()

orgs = re.findall('From .*@([^ ]*)', content)
for line in orgs:
	results[line] = results.get(line, 0) + 1

for key, value in results.items():
	add_email(key, value)

cur.execute("SELECT * FROM Counts")
print(cur.fetchall())

conn.commit()
conn.close()