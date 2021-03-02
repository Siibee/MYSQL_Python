import mysql.connector as pymy
import mysql_passwd as mypasswd

connection = pymy.connect(user = 'root', host = '127.0.0.1', password ='')

connection = pymy.connect(**mypasswd.hideInfo)

first = connection.curson()
first.execute('SHOW DATABASES')
print(first.fetchall())

for i in first
    print(i)

connection.close()
