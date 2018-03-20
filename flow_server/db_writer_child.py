import sys
import time
import sqlite3

for line in sys.stdin:
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    num = float(line)

    with conn:
        SQL = """INSERT INTO display_flow_flow (val, timestamp)
                    VALUES (:val, :timestamp);"""
        vals = {'val':num, 'timestamp':int(time.time())}
        c.execute(SQL, vals)             

    conn.close()
