# Introduction to the Data

import sqlite3

conn = sqlite3.connect('jobs.db')

# Working with Sequences of Values as Tuples

import sqlite3
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

query = "select Major from recent_grads;"
cursor.execute(query)
majors = cursor.fetchall()
print(majors[0:2])

# Execute as a Shortcut for Running a Query

query = "select Major, Major_category from recent_grads;"
cursor.execute(query)
five_results = cursor.fetchmany(5)

# Closing the Database Connection

conn = sqlite3.connect("jobs.db")

conn.close()

# Workflow 

import sqlite3
conn = sqlite3.connect("jobs2.db")
cursor = conn.cursor()

query = "select Major from recent_grads order by Major desc;"
cursor.execute(query)
reverse_alphabetical = cursor.fetchall()
conn.close()
