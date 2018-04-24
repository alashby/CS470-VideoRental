import mysql.connector
cnx = mysql.connector.connect(user='admin', password='password',
                              host='localhost',
                              database='video_rental')
cursor = cnx.cursor(buffered=True)
#Example
query = ("SELECT Title FROM movie "
         "WHERE Rating = %s")
cursor.execute(query, ('R',))
row = cursor.fetchone()
print(row)
