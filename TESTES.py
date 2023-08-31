import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()
con.close()