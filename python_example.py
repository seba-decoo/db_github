print("mysql.connector:")

import mysql.connector
cnx= mysql.connector.connect(host="localhost",user="cedric",password="Howest2020",database="biodb2")
cursor=cnx.cursor()
query = ("SELECT * FROM modorg")
cursor.execute(query)
for result in cursor:
	print(result)
cursor.close()
cnx.close()
######################################################################################################
print("MySQLdb:")
import MySQLdb
db = MySQLdb.connect(host="localhost",user="cedric",passwd="Howest2020",db="biodb2")
cur=db.cursor()
cur.execute("SELECT * FROM modorg")
for result in cur:
	print(result)
db.close()
