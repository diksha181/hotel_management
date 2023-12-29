conn=mysql.connector.connect(host="localhost",username="root",password="diksha",database="hotel_management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
        rows=my_cursor.fetchall()