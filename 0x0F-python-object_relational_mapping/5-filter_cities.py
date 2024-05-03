#!/usr/bin/python3
"""
Lists cities in states passed as argument
from database passed as argument
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    city_input = sys.argv[4]
    cursor.execute("SELECT `cities`.`name`\
                    FROM `cities`\
                    JOIN `states` ON `cities`.`state_id` = `states`.`id`\
                    WHERE states.name LIKE %s\
                    ORDER BY `cities`.`id` ASC", (city_input,))
    cities = cursor.fetchall()
    cities_arr = []
    for row in cities:
        for col in row:
            cities_arr.append(col)
    print((", ").join(cities_arr))

    cursor.close()
    db.close
