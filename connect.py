import MySQLdb


def connection():
    # Open database connection
    db = MySQLdb.connect("localhost", "root", "allstar", "testingone")
    # prepare a cursor object using cursor() method
    # print "connected"
    cursor = db.cursor()

    # sql = """INSERT INTO students(name, addr, city, pin) VALUES ('Mac', 'Mohan', 'naxal', 'fgjgh')"""
    # try:
    #     print "entered try"
    #     cursor.execute(sql)
    #     db.commit()
    # except:
    # # Rollback in case there is any error
    #     db.rollback()
    # print "inserted"
    # db.close()
    return cursor, db

# connection()
