#!/usr/bin/python3
#lists state name passed as argument safely
import sys
import MySQLdb

if __name__ == "main":
    """establish connection to database"""
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor();
    state_input = sys.argv[4]
    cursor.execute("SELECT * FROM states WHERE BINARY `name` = '{state_input}' ORDER BY states.id ASC")
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    connection.close
