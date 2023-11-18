#!/usr/bin/python3
"""
#!/home/ad/venv/bin/python3
a script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
and one that is safe from MySQL injections!
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
    with conn.cursor() as cur:
        cur.execute("""SELECT * FROM states WHERE name like BINARY
                    %(name)s ORDER BY id ASC """, {'name': argv[4]})
    # HERE I have to know SQL to grab serched states in my database
        query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
