#!/usr/bin/python3
#lists state with name Arizona passed as argument
import sys
import MySQLdb

if __name__ == "main":
    """establish connection to database"""
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor();
    cursor.execute("SELECT * FROM states WHERE BINARY `name` = '{}' ORDER BY states.id ASC".format(sys.argv[4])
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    connection.close
