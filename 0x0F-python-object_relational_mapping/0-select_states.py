#!/usr/bin/python3
"""script that lists alll states from database hbtn_0e_usa"""


import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host = "localhost", user = sys.argv[1], port = 3306,
                         passwd = sys.argv[2], db = sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()

    for row in rows:
        print(row)

