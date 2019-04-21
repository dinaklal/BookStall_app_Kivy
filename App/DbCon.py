import mysql.connector
class DbCon:

    def __init__(self):
        self.db = mysql.connector.connect(
                          host="localhost",
                          user="lal",
                          password="949510",
                          database= 'bookstall'
                        )
        self.c = self.db.cursor()

    def get_user(self):
        self.c.execute("SELECT * FROM user")
        return self.c.fetchall()
    def get_user_ac(self,username,password):
        self.c.execute("SELECT * FROM user where user ='"+username+ "' and password ='"+ password+"'")
        return self.c.fetchall()
