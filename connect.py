import MySQLdb


def connection():
    # Open database connection
    db = MySQLdb.connect("localhost", "root", "allstar", "testingone")
    # prepare a cursor object using cursor() method

    cursor = db.cursor()

    return cursor, db

