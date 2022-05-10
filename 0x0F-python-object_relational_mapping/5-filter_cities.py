#!/usr/bin/python3
'''list all cities from the database hbtn_0e_4_usa'''

import MySQLdb
import sys

if __name__ == "__main__":
    '''main function'''
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.name \
                FROM cities JOIN states ON cities.state_id=states.id \
                WHERE states.name = %s", (sys.argv[4],))
    query_rows = cur.fetchall()
    str = ""
    for row in query_rows:
        str = str + row[0]
        if row != query_rows[-1]:
            str = str + ", "
    print(str)
    cur.close()
    conn.close()