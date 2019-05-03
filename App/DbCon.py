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
        self.c.execute("SELECT userid FROM user where user ='"+username+ "' and password ='"+ password+"'")
        return self.c.fetchall()
    def get_gst(self):
        self.c.execute("SELECT gstclass FROM gst")
        return self.c.fetchall()
    def get_cat(self):
        self.c.execute("SELECT category FROM category")
        return self.c.fetchall()

    def add_item(self,item,price,qtty,gst,cat,user):

        self.c.execute("select categoryid from category where category ='"+cat+"' ")
        r= self.c.fetchall()
        for row in r:
            catid =  row[0]
        self.c.execute("select gstclass_id from gst where gstclass ='" + gst + "' ")
        r = self.c.fetchall()
        for row in r:
            gstid = row[0]
        self.c.execute("select userid from user where user ='" + user + "' ")
        r = self.c.fetchall()
        for row in r:
            userid = row[0]
        self.c.execute("INSERT INTO item (item,description, categoryid,gstclass_id,addedby,price,quantity) VALUES ( '"+item+"','desc','"+str(catid)+"','"+str(gstid)+"','"+str(userid)+"',"+str(price)+","+str(qtty)+")")
        return (self.db.commit())

