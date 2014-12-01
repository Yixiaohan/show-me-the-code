#-*- coding: utf-8-*-
import  mysql.connector

config = {
  'user': 'root',
  'password': 'root',
  'host': '127.0.0.1',
  'database': 'test',
  'raise_on_warnings': True,
}

class save_keys_to_mysql:
	def __init__(self,path):
		self.path=path
		print(self.path)
	def __conn(self,**conf):
		try:
			conn=mysql.connector.connect(**conf)
			print(conn)
		except mysql.connector.Error as err:
			if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
				print("something is wrong with your user name or password")
			elif err.errno == errorcode.ER_BAD_DB_ERROR:
				prnt("database does not exists")
			else:
				print(err)
		return conn
		#print(self.conn)

	def save_to_mysql(self,**conf):
		conn=self.__conn(**conf)
		path=self.path
		cursor=conn.cursor()
		cursor.execute('drop table if exists act_keys')
		cursor.execute('create table act_keys (id int(8) primary key, act_keys varchar(50))')
		row=0
		with open('keys_text.txt','r') as f:
			for line in f.readlines():
				#row_no='0000'+str(row)
				act_keys=line.rstrip()
				cursor.execute('insert into act_keys (id, act_keys) values (%s, %s)',[row,act_keys])
				row+=1
		conn.commit()
		cursor.close()
		conn.close()


	def see_all(self,**conf):
		conn=self.__conn(**conf)
		cursor=conn.cursor()
		cursor.execute('select * from act_keys')
		values=cursor.fetchall()
		print(values)
		cursor.close()
		conn.close()



test=save_keys_to_mysql('keys_text.txt')
test.save_to_mysql(**config)
test.see_all(**config)

