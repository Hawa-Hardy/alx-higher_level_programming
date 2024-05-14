#!/usr/bin/python3
import MySQLdb
import sys

def list_states(username, password, dbname):
    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname
    )

    # Create a cursor object
    cur = db.cursor()

    # Execute the SQL query
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the results
    rows = cur.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the cursor and connection
    cur.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password dbname".format(sys.argv[0]))
        sys.exit(1)

    username, password, dbname = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states(username, password, dbname)
