#!/usr/bin/python3

"""
#!/home/ad/venv/bin/python3
a script that lists all states with a name starting with
N (upper N) from the database hbtn_0e_0_usa:
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """
conn = MySQLdb.connect(host="localhost", port=3306,
                       user=argv[1], passwd=argv[2],
                       db=argv[3], charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states WHERE name like 'N%' ORDER BY id ASC")
# HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
