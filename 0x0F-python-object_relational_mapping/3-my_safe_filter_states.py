#!/usr/bin/python3
"""
Lists state name passed as argument safely\
from database passed as argument
"""
import sys
import MySQLdb

if __name__ == "__main__":
    """establish connection to database"""
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    state_input = sys.argv[4]
    cursor.execute("SELECT * FROM states\
                    WHERE `name` LIKE %s\
                    ORDER BY id ASC", (state_input,))
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
