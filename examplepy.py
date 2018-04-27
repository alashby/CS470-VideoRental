import mysql.connector
import datetime
import unicodedata
cnx = mysql.connector.connect(user='admin', password='password',
                              host='localhost',
                              database='video_rental')
cursor = cnx.cursor(buffered=True)
cnx.autocommit = True
#Example Selection
'''
query = ("SELECT Title FROM movie "
         "WHERE Rating = %s")
cursor.execute(query, ('R',))
row = cursor.fetchone()
print(row[0].encode('ascii','ignore'))
'''

#verify customer id
'''
#customerNum will be the number the customer inputs
#should already be verified that it is an int
query = ("SELECT * FROM customer "
         "WHERE Customer_ID = %s")
cursor.execute(query, (customerNum,))
row = cursor.fetchall()
while not row:
    print("Customer not found. Please review your input and try again.")
    #code for user input goes here
    query = ("SELECT * FROM customer "
         "WHERE Customer_ID = %s")
    cursor.execute(query, (customerNum,))
    row = cursor.fetchall()
#from here go to browsing. maybe a choice between browsing and view current hold requests or rentals? idk will it even matter
'''


#browse title
'''
titles = []
query = ("SELECT Title FROM movie ORDER BY Title")
cursor.execute(query)
while True:
    row = cursor.fetchone()
    if not row: break
    titles.append(row[0].encode('ascii','ignore'))
for i in range(len(titles)):
    print(str(i++) + ". " + titles[i] + "\n")
'''
#after choosing title. "choice" would be the variable holding whatever number
#was inputted by the user
'''
selection = titles[choice--]
movies = []
query = ("SELECT * FROM movie "
         "WHERE Title = %s ORDER BY Title")
cursor.execute(query, (selection,))
while True:
    row = cursor.fetchone()
    if not row: break
    movies.append([row[0],row[1].encode('ascii','ignore'),row[2],row[3].encode('ascii','ignore'),
                   row[4].encode('ascii','ignore'),row[5].encode('ascii','ignore'),
                   row[6].encode('ascii','ignore'),row[7],row[8]])
for i in range(len(movies)):
    print(str(i++) + ". " + movies[i][1] + " (" + str(movies[i][2]) + ")\tGenre: " + movies[i][3] +
          "\tRating: " + movies[i][4] + "\tDirector: " + movies[i][5] + "\n" +
          movies[i][6] + "\nRuntime: " + str(movies[i][7]) + "\tIMDB Score: " + str(movies[i][8]) + "/10\n")
'''
#place hold request
'''
selection = movies[choice--]
#customerNum will be a variable holding the current user's customer number
reqdate = datetime.datetime.now()
query = ("INSERT INTO hold_request VALUES (" +
         str(selection[0]) + "," +
         str(customerNum) + ",'" +
         str(reqdate.year) + "-" +
         '%02d' % reqdate.month + "-" +
         '%02d' % reqdate.day +"')")
cursor.execute(query)
'''




#renting out copy
'''
selection = movies[choice--]
query = ("SELECT Copy_no FROM copy "
         "WHERE Renter_no IS NULL AND IMDB_no = %s ORDER BY Copy_no")
cursor.execute(query,(selection,))
row = cursor.fetchone()
#customerNum will be a variable holding the current user's customer number
duedate = datetime.datetime.now() + datetime.timedelta(days=7)
query = ("UPDATE copy "
         "SET Renter_no = " + customerNum +
         ", Due_date = '" + str(duedate.year) + "-" +
         '%02d' % duedate.month + "-" + '%02d' % duedate.day + "' "
         "WHERE IMDB_no = " + str(selection[0]) + " AND Copy_no = " + str(row[0]))
cursor.execute(query)
'''
