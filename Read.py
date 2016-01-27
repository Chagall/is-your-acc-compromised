import os
import sqlite3

connection = sqlite3.connect('Accounts.db')
conCursor = connection.cursor()
conCursor.execute('CREATE TABLE IF NOT EXISTS TenMiAcc(username TEXT, password TEXT)')

counter = 0

with open('10-million-combos.txt','r',encoding='ISO-8859-1') as accFile:

	for line in accFile:
		try:
			accLineList = line.split()
			accUsername = accLineList[0]
			accPassword = accLineList[1]
			#print(accUsername,accPassword)
			conCursor.execute('INSERT INTO TenMiAcc(username,password) VALUES(?,?)', (accUsername,accPassword))
		except Exception as e:
			accPassword = ' '
			conCursor.execute('INSERT INTO TenMiAcc(username,password) VALUES(?,?)', (accUsername,accPassword))			

print('Commiting changes...')
connection.commit()
print('Process Complete!')
connection.close()