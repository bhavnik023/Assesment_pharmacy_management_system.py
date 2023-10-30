import mysql.connector
import datetime

def create_conn():  #create connection with mysql
    return mysql.connector.connect(
        host="localhost",
        username="root",
        password="",
        database="pharmacy_system"
    )

#Class For Admin Role
class Admin:
    def __init__(self,username,password,name,mobile):
        self.username=username
        self.password=password
        self.name=name
        self.mobile=mobile
    #Function For Register Admin
    def admin_register(self):
        conn=create_conn()
        cursore=conn.cursor()
        query="insert into adminregister(usernamer,password,name,mobile) values(%s,%s,%s,%s)"
        args=(self.username,self.password,self.name,self.mobile)
        cursore.execute(query,args)
        conn.commit()
        conn.close()
        print("Admin Register For successfuly")
    #Function For Login Admin
    def Login_Admin(self):
        conn=create_conn()
        cursore=conn.cursore()
        query="select * from adminregister  where username=%s"
        args=(self.username)
        cursore.execute(query,args)
        row=cursore.fetchone()
        return row
    #View All Manager
    def view_all_manager(self):
        conn=create_conn()
        cursore=conn.cursore()
        query="select * from manager"
        cursore.execute(query)
        rows=cursore.fetchall()

        for row in rows:
            print(f"Sr.No: {row[0]}, Username:{row[1]}, Name: {row[3]}, PharmacyName: {row[4]}")

        conn.close()

    #View All Medicine
    def view_all_medicine(self):
        conn=create_conn()
        cursore=conn.cursore
        query="select * from medicine"
        cursore.execute(query)
        rows=cursore.fetchall()

        for row in rows:
            if not row:
                print("No Medicine Available")
            else:
                print(f"(Sr.No :{row[0]}, Medicine Name: {row[1]}, Added ate: {row[2]}, Added By: {row[3]}, Price :{row[5]})\n")
#Class For Manager
class manager():

    def __init__(self) -> None:
        pass

    #Manager Register Function
    def manager_register(self,username,password,name,pharmacy):
        conn=create_conn()
        cursore=conn.cursore
        query="insert into manager(username,pass,manager_name,pharmacy_name) values(%s,%s,%s,%s)"
        args=(username,password,name,pharmacy)
        cursore.execute(query,args)
        conn.commit()
        conn.close()
        print("Manager Register For Successfuly")
    
    #Login manager
    def login_manager(self,username):
        conn=create_conn()
        cursore=conn.cursore()
        query="select * from manager whare username=%s"
        args=(username,)
        cursore.execute(query,args)
        row=cursore.fetchone()
        return row