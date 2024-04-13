#!/usr/bin/python3

"""This script lists all cities from the database `hbtn_0e_4_usa`"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    username, password, db_name = sys.argv[1:]

    conn = MySQLdb.connect(
        host="localhost",
        user=username,
        password=password,
        database=db_name,
        port=3306,
    )

    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT cities.id, cities.name, states.name
        FROM cities
            JOIN states ON cities.state_id = states.id
        ORDER BY cities.id;
        """
    )

    list_result = cursor.fetchall()

    for row in list_result:
        print(row)

    cursor.close()
    conn.close()
