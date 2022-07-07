from Controller.controlConfig import controlParameter
from Controller.cantrolDate import DT
from cryptography.fernet import Fernet
import mysql.connector
class connectDao:
	def lastRemove():
		try:
			MyDb = connection.connection2()
			myCursor = MyDb.cursor()
			myCursor.execute("SELECT id,email,date,product_id  FROM copytraderone.contasallwinn where typebot = 'SAL' and delition_date is not null")
			account = myCursor.fetchall()
			MyDb.close()
			if account == None:
				return None
			else: 
				return  account
		except Exception as a:
			MyDb.close()
			return  None

	
	def nextRemove():
		try:
			MyDb = connection.connection2()
			myCursor = MyDb.cursor()
			myCursor.execute("SELECT id,email,date,product_id  FROM copytraderone.contasallwinn where typebot = 'SAL' and delition_date is null")
			account = myCursor.fetchall()
			MyDb.close()
			if account == None:
				return None
			else: 
				return  account
		except Exception as a:
			MyDb.close()
			return  None	
	
	def todayRemove(dayWhere):
		try:
			MyDb = connection.connection2()
			myCursor = MyDb.cursor()
			myCursor.execute("SELECT id,email,date,product_id,delition_date  FROM copytraderone.contasallwinn where typebot = 'SAL' and (delition_date like '%"+dayWhere+"%' or delition_date is null)")
			account = myCursor.fetchall()
			MyDb.close()
			if account == None:
				return None
			else: 
				return  account
		except Exception as a:
			MyDb.close()
			return  None	
	
	
	
	def selUsers():
		try:
			MyDb = connection.connection2()
			myCursor = MyDb.cursor()
			myCursor.execute("SELECT chat_id FROM copytraderone.contasallwinn where activate = 'active' and typebot = 'SAL'")
			account = myCursor.fetchall()
			MyDb.close()
			if account == None:
				return False, None
			else: 
				return True, account
		except Exception as a:
			MyDb.close()
			return False, None
	def insertAcc(email, senha, valor,order_key, name, product_id, date,tokrn, chat_id, date_c, id_acc):
		try:
			MyDb = connection.connection2()
			myCursor = MyDb.cursor(buffered=True)
			myCursor.execute("SELECT countSubs,id FROM copytraderone.contasallwinn where email='"+email+"'")
			account = myCursor.fetchone()
			if product_id in ['531','27195','27194','27197','535','536']:
				if account == None:
					pass
				else:
					myCursor.execute("DELETE FROM copytraderone.contasallwinn WHERE email = '"+str(email)+"'")
					MyDb.commit()
			if product_id in ['531','27195','27194','27197','535','536']:		
				if None != account:
					countSubs = int(account[0]) + 1
				else:
					countSubs = '0'
				myCursor.execute("insert into copytraderone.contasallwinn (email, password, value, order_key, name, product_id, activate, token, chat_id, date,acc_id,typebot,countSubs) VALUES ('"+email+"', '"+senha+"', '"+valor+"', '"+order_key+"', '"+name+"', '"+product_id+"', 'active', 'SAL', '"+chat_id+"', '"+date_c+"', '"+id_acc+"','SAL','"+str(countSubs)+"')")
				MyDb.commit()
					
			if product_id in ['27195']:
				if None != account:
					countSubs = int(account[0]) + 1
				else:
					countSubs = '0'
				myCursor.execute("insert into copytraderone.contasallwinn (email, password, value, order_key, name, product_id, activate, token, chat_id, date,acc_id,typebot,countSubs) VALUES ('"+email+"', '"+senha+"', '"+valor+"', '"+order_key+"', '"+name+"', '"+product_id+"', 'active', 'LAB', '"+chat_id+"', '"+date_c+"', '"+id_acc+"','LAB','"+str(countSubs)+"')")
				MyDb.commit()
					
			if product_id in ['27197']:
				if None != account:
					countSubs = int(account[0]) + 1
				else:
					countSubs = '0'
				myCursor.execute("insert into copytraderone.contasallwinn (email, password, value, order_key, name, product_id, activate, token, chat_id, date,acc_id,typebot,countSubs) VALUES ('"+email+"', '"+senha+"', '"+valor+"', '"+order_key+"', '"+name+"', '"+product_id+"', 'active', 'LAB', '"+chat_id+"', '"+date_c+"', '"+id_acc+"','LAB','"+str(countSubs)+"')")
				MyDb.commit()
				myCursor.execute("insert into copytraderone.contasallwinn (email, password, value, order_key, name, product_id, activate, token, chat_id, date,acc_id,typebot,countSubs) VALUES ('"+email+"', '"+senha+"', '"+valor+"', '"+order_key+"', '"+name+"', '"+product_id+"', 'active', 'BOT', '"+chat_id+"', '"+date_c+"', '"+id_acc+"','BOT','"+str(countSubs)+"')")
				MyDb.commit()
					
			if product_id in ['27194']:
				if None != account:
					countSubs = int(account[0]) + 1
				else:
					countSubs = '0'
				myCursor.execute("insert into copytraderone.contasallwinn (email, password, value, order_key, name, product_id, activate, token, chat_id, date,acc_id,typebot,countSubs) VALUES ('"+email+"', '"+senha+"', '"+valor+"', '"+order_key+"', '"+name+"', '"+product_id+"', 'active', 'BOT', '"+chat_id+"', '"+date_c+"', '"+id_acc+"','BOT','"+str(countSubs)+"')")
				MyDb.commit()
			myCursor.close()
			MyDb.close()
			return True,''
		except Exception as a:
			MyDb.close()
			return False,"ERRO: "+str(a)

	def AuthId(userId):
		try:
			MyDb = connection.connection2()
			myCursor = MyDb.cursor()
			myCursor.execute("select * from copytraderone.contasallwinn where chat_id = '"+str(userId)+"' and activate = 'active' and typebot = 'LAB'")
			account = myCursor.fetchone()
			MyDb.close()
			if account == None:
				return False
			else: 
				return True
		except Exception as a:
			###print(a)
			MyDb.close()
			return False
	def updateStrategy(pair,time,filtro,syss,pct):
		try:
			MyDb2 = connection.connection()
			myCursor = MyDb2.cursor()
			myCursor.execute("SELECT * FROM allwinclub_winlab.strategy where par = '"+str(pair)+"' and time = '"+str(time)+"' and gale = '"+str(filtro)+"' and estrategia = '"+str(syss)+"' and pct >= '"+str(pct)+"' and data = '"+DT.dateNowForString()+"'")
			account = myCursor.fetchone()
			MyDb2.close()
			if account != None:
				return True, account[2]
			else: 
				return False,"Porcentagem abaixo de "+str(pct)+"%"
		except Exception as e:
			##print(e)
			return False,str(e)
	def conwoo():
		try:
			MyDb = connection.connection2()
			myCursor = MyDb.cursor()
			myCursor.execute("select * from copytraderone.secret_api")
			account = myCursor.fetchone()
			MyDb.close()
			if account == None:
				return False, None, None
			else: 
				return True, account[1], account[2]
				
		except Exception as a:
			MyDb.close()
			return False, None, None
	def getParesBd():
		try:
			MyDb = connection.connection2()
			myCursor = MyDb.cursor()
			myCursor.execute("select * from copytraderone.pares")
			account = myCursor.fetchone()
			MyDb.close()
			if account == None:
				return False, None
			else: 
				return True, account[1].split(',')
				
		except Exception as a:
			MyDb.close()
			return False, None
class connection:
	def connection2():
		MyDb = mysql.connector.connect(
		  host="den1.mysql5.gear.host",
		  user="copytraderone",
		  password="#hsE&tYEXkkdListGT",
		  database="copytraderone"
		)
		return MyDb
	def connection():
		MyDb2 = mysql.connector.connect(
		  host="45.13.59.114",
		  user="allwinclub_davi",
		  password="J3112davi!",
		  database="allwinclub_winlab"
		)
		return MyDb2
