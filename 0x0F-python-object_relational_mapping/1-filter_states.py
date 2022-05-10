#!/usr/bin/python3
""" lists all states with a name starting with N (upper N)
    from the database hbtn_0e_0_usa
"""
if __name__ == "__main__":

    import sys
    import MySQLdb
    
    mydb = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           password=sys.argv[2], database=sys.argv[3])
    mycursor = mydb.cursor()
    q = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    mycursor.execute(q)
    myresult = mycursor.fetchall()
    for row in myresult:
        print(row)
    mycursor.close()
    mydb.close()