import sys
import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()
with conn:
    c.execute("""CREATE TABLE IF NOT EXISTS count (id INTEGER, c INTEGER);""")
conn.close()

for line in sys.stdin:
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    num = int(line)

    with conn:
        c.execute("SELECT c FROM count WHERE id = 1;")
        print('count outside:', c.fetchall()[0][0])

        c.execute("SELECT * FROM count")
        if c.fetchall():
            c.execute("""UPDATE count
                        SET c = ?
                        WHERE id = 1;""", (num,))
        else:
            c.execute("""INSERT INTO count
                        VALUES (?, ?);""",
                        (1, num))
    conn.close()
