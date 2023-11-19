#!/usr/bin/python3
#lists cities and state name
import sys
import MySQLdb

if __name__ == "main":
    """establish connection to database"""
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor();
    cursor.execute("SELECT `cities`.`id`, `cities`.`name`, `states`.`name` \
                    FROM `cities` \
                    INNER JOIN `states` \
                        ON `cities`.`state`.`id` \
                    ORDER BY `cities`.`id` ASC")
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    connection.close
