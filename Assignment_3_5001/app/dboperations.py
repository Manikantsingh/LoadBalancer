import sqlalchemy as db
import pymysql
def savequery(inputQuery , finalResponse):
    db = pymysql.connect('db', 'newuser', 'password', 'test_db')
    cursor = db.cursor()

    print(inputQuery, finalResponse)
    # Prepare SQL query to INSERT a record into the database.
    sql = """INSERT INTO query(query, response) VALUES(%s , %s)"""
    print(sql)
    try:
        # Execute the SQL command
        cursor.execute(sql, (inputQuery, finalResponse))
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        print("some error occurred while connecting to database")
        db.rollback()
    db.close()
