#!/usr/bin/python3
"""
lists cities and state name
from database passed as argument
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT `cities`.`id`, `cities`.`name`, `states`.`name` \
                    FROM `cities` \
                    JOIN `states` \
                        ON `cities`.`id` \
                    ORDER BY `cities`.`id` ASC")
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close
