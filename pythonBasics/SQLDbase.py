import mysql.connector


conn = mysql.connector.connect(host='localhost', user='root', password='A_ta25!wbY66@',
                            database='pythonapisqltest')
#verify python/sql connection = true
print(conn.is_connected())

#query the tables created on mysql with python code, create a cursor obj
cursor = conn.cursor()
#use query SELECT * FROM customerInfo;
cursor.execute('SELECT * FROM customerInfo')
#row = cursor.fetchone()
#print(row)
#it will print in tuple or list(find the index), dictionary (then find key value)
#for tuple or list
#print(row[3])

#rowAll = cursor.fetchall()
#print(rowAll) #this will fetch a list of tuples. iterate through list
rows = cursor.fetchall()
print(type(rows))
print(rows)

total_amount = 0

for row in rows: # example ('Protractor', datetime.date(2026, 2, 18), 45, 'Africa')
    print(row[2]) #lists all the amounts in every row
    total_amount = total_amount + row[2] #to sum up all amounts in a loop
    print("Total Amount:", total_amount)

#query update customerinfo on mysql from pycharm using python code
#update customerInfo set Location = 'Japan' where CourseName = 'selenium'"
#rewrite without hard coding
query = "update customerInfo set Location = %s where CourseName = %s"
data = ("Dubai", "selenium")
cursor.execute(query, data)
#commit

query = "DELETE FROM CustomerInfo WHERE CourseName = %s"
data = ("Protractor",)

cursor.execute(query, data)

#commit
conn.commit()

#verify data on Mysql is updated/DELETED as expected


conn.close()