import uuid
import MySQLdb as mdb

class Application(object):

    def ID_Generate(self):
        self.id_box = []
        for i in range(0, 200):
            self.id_box.append(uuid.uuid4())

    def ID_Store(self):
        con = mdb.connect('localhost', 'ex02','ex02', 'ex02db')

        with con:
            cur = con.cursor()
            cur.execute("DROP TABLE IF EXISTS ID_Generate")
            cur.execute("CREATE TABLE ID_Generate(NO. INT PRIMARY KEY AUTO_INCREMENT,\
                        ID VARCHAR(20))")
            cur.execute("INSERT INTO ID_Generate(ID) VALUES(self.id_box)")
        con.close()