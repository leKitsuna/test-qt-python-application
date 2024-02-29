import sqlite3

connection = sqlite3.connect("tournaments.db")
cursor = connection.cursor()

cursor.execute("""
               CREATE TABLE tournament(
                   id INT AUTO PRIMARY KEY,
                   name VARCHAR(30),
                   url VARCHAR(50),
                   discord VARCHAR(20),
                   tournament VARCHAR(30)
               ) 
               """)

connection.commit()