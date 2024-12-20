from db_config import dbconnection


try:
    conn = dbconnection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM blogs;")
    tables = cursor.fetchall()
    for table in tables:
        print(table)

except Exception as e:
    print(str(e))

finally:
    cursor.close()
    conn.close()