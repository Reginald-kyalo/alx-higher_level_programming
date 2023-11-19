#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "main":
    """establish connection to database"""
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor();
    city_input = sys.argv[4]
    cursor.execute("SELECT * FROM cities WHERE BINARY `name` = '{city_input}' ORDER BY cities.id ASC")
    cursor.execute("SELECT `cities`.`id`, `cities`.`name`, `states`.`name` \
                    FROM `cities` \
                    WHERE BINARY `name` = '{city_input}' \
                    INNER JOIN `states` \
                        ON `cities`.`state`.`id` \
                    ORDER BY `cities`.`id` ASC")
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    connection.close
