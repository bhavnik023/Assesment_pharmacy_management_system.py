import mysql.connector
import datetime

def create_conn():  #create connection with mysql
    return mysql.connector.connect(
        host="localhost",
        username="root",
        password="",
        database="pharmacy_system1"
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
        cursore=conn.cursore()
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
        cursore=conn.cursore()
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
    
    #Add Medicine
    def add_medicine(self, SR_number, medicine_name,Qty, Added_Date, Added_By, price):
        conn=create_conn()
        cursore=conn.cursore()
        query="insert into medicine(SR_No,Medicine_Name, Qty, Added_Dates, Added_By, price) Value(%s,%s,%s,%s,%s,%s)"
        args=(self, SR_number, medicine_name,Qty, Added_Date, Added_By, price)
        cursore.execute(query,args)
        conn.commit()
        conn.close()
        print("Add Medicine Successfuly")
    
    #View medicine
    def view_medicine(self,medicine_srno):
        conn=create_conn()
        cursore=conn.cursor()
        query="select * from medicine where SR_No=%s"
        args=(medicine_srno)
        cursore.execute(query,args)
        rows=cursore.fetchall()

        for row in rows:
            if not row:
                print("No Medicine Available")
            else:
                print(f,"(SR.No :{row[0]},Medicine Name: {row[1]},Qty :{[2]},Added Date :{row[3]},Added By :{roe[4]},Price :{row[5]})\n")

        conn.close()

    #Delete Medicine
    def dalete_medicine(self,medicine_srno):
        conn=create_conn()
        cursore=conn.cursore()
        query="DELETE FROM `medicine` WHERE SR_No=%s"
        args=(medicine_srno)
        cursore.execute(query,args)
        conn.commit()
        conn.close()
    
while True:
    print(" "*23,"WELCOME PHARMACY MANAGEMENT SYTEM")
    print("")
    print(" "*30,"1) Admin")
    print(" "*30,"2) Pharmacy Manager") 
    print(" "*30,"3) Exit")

    Role = input("Enter Your Role : ")#Select Role
    try:
        Role = int(Role)
    except ValueError:
        print("Error Caught : Enter  Role As A Numberical Value ")
    
#Admin Role
    if Role==1:
        while True:
            print("")
            print(" "*30,"Welcome Admin Page")
            print("")
            print(" "*30,"1) Register")
            print(" "*30,"2) Login")
            print(" "*30,"3) Exit Admin Page")

            choice= input("Enter Your Choice : ")
            try:
                choice=int(choice)
            except ValueError:
                print("Error Caught : Enter choice As A  Numberical Value ")
            
            #Admin Register
            if choice==1:
                print(" "*30,"Admin Register Page")
                user_name=input("Enter User Name : ")
                conn=create_conn()
                cursore=conn.cursore()
                query="select * from adminregister where username=%s"
                args=(user_name,)
                cursore.execute(query,args)
                row=cursore.fetchall()

                if row is None or user_name!=row[1]:
                    user_pass=input("Enter Your paasword : ")
                    Name=input("Enter Your Name : ")
                    mobile=input("Enter Your Mobile : ")
                    register=(user_name,user_pass,Name,mobile)
                    register.admin_register()

                else:
                    print("User name is already exist")
                    continue

            #Admin Login
            elif choice==2:
                while True:
                    print(" "*30,"Admin Login Page")
                    user_name=("Enter User Name")
                    user_pass=("Enter Password")

                    loginadmin=Admin(user_name,user_pass,None,None)
                    row=loginadmin.Login_Admin()

                    if row is None or (user_name!=row[1] or (user_pass!=row[2])):
                        print("Enter Correct Username And Password")
                        continue

                    else:
                        print("")
                        print("Admin Login Successfuly")
                        print("")
                        while True:
                            print(" "*30,"1) View All Manager")
                            print(" "*30,"2) View All Medicine")
                            print(" "*30,"3) Back Admin Main Page")

                            choice=input("Enter YOur Choice :")

                            try:
                                choice=int(choice)
                            except ValueError:
                                print("Error Caught : Enter choice As A  Numberical Value ")

                            #View All Manager
                            if choice==1:
                                viewmanager=Admin(None,None,None,None)
                                viewmanager.view_all_manager()

                            #View All Medicines
                            if choice==2:
                                viewmedicines=Admin(None,None,None,None)
                                viewmedicines.view_all_medicine()

                            if choice==3:
                                break

                            else:
                                print("Enter Correct Choice")

                            perform=input('Do you want to perform more operations Press "y" for yes or "n" for no: ')
                            if perform.lower()!= 'y':
                                break
                        break
            
            elif choice==3:
                break
            else:
                print("Enter Correct Choice")
                continue

            perform=input('Do you want to perform more operations Press "y" for yes or "n" for no: ')
            if perform.lower()!= 'y':
                 break

#Manager Role
    elif Role==2:

        while True:
            print("")
            print(" "*30,"Welcome manager page")
            print("")
            print(" "*20,"1) Register")
            print(" "*20,"2) Login")
            print(" "*20,"3) Exit Manager Page")

            choice=input("Enter Your Choice : ")
            try:
                choice=int(choice)
            except ValueError:
                    print("Error Caught : Enter choice As A  Numberical Value ")
               
            #Manager Register
            if choice==1:
                print=(" "*30,"Manager Register Page")
                user_name=input("Enter User Name : ")
                Conn=create_conn()
                cursore=Conn.cursore
                query="select * from manager where username=%s"
                args=(user_name,)
                cursore.execute(query,args)
                row=cursore.fetchone()

                if row is None or user_name!=row[1]:
                    user_pass=input("Enter Your Password : ")
                    manager_name=input("Enter Manager Name : ")
                    pharmacy=input("Enter Pharmacy Name : ")
                    register=manager()
                    register.manager_register(user_name,user_pass,manager_name,pharmacy)

                else:
                    print("User Name Alreday Exist") #when Name Already Exist in database the show error
                    continue
            
            #Manager Login
            elif choice==2:
                print(" "*30,"Manager Login Page")
                user_name=input("Enter User Name : ")
                user_pass=input("Enter User Password : ")

                login=manager()
                row=login.manager_login(user_name)


                if row is None or (user_name!=row[1] and user_pass!=[2]):
                    print("Enter Correct Username and Password")
                    continue
                else:
                    print("Manager Login Successfuly")

                    while True:

                        print("")
                        print(" "*30,"1) Add Medicine")
                        print(" "*30,"2) View Medicine")
                        print(" "*30,"3) Delete Medicine")
                        print(" "*30,"4) Back Manage Main Page")

                        #select choice for perform by manager
                        choice=input("Enter Your Choice : ")
                        try:
                            choice=int(choice)
                        except ValueError:
                            print("Error Caught : Enter Choice As An Numberical Value ")
                        
                        #Add Medicine
                        if choice==1:

                            SR_number=input("Enter Medicine SR Number : ")
                            Conn=create_conn()
                            cursore=Conn.cursore
                            query="select * from medicine where SR_No=%s"
                            args==(SR_number,)
                            cursore.execute(query,args)
                            row=cursore.fetchone()

                            if row is None or SR_number!=row[0]:
                                medicine_name=input("Enter Medicine Name : ")
                                qty=input("Enter medicine QTY : ")
                                try:
                                    qty=int(qty)
                                except ValueError:
                                    print("Error Caught : Enter qty As A  Numerical Value ")
                                    continue
                                Added_date=datetime.datetime,now().strftime("%Y-%m-%d %H:%M:%S")
                                Added_by=input("Enter Added By : ")
                                price=input("Enter Medicine Price : ")
                                try:
                                    price=int(price)
                                except:
                                    print("Error Caught : Enter qty As A  Numerical Value ")
                                    continue
                                medicine=manager()
                                medicine.add_medicine(SR_number,medicine_name,qty,Added_date,Added_by,price)

                            else:
                                print("SR Number Already Exist") #when Sr No Already Exist in database then show error
                                continue
                        
                        #View Medicine
                        elif choice==2:

                            medicine_srno=input("Enter Medicine SR Number : ")


                            if medicine_srno==" ":
                                print("Please Enter Sr No")
                            else:
                                Conn=create_conn()
                                cursore=Conn.cursor()
                                query="select * from medicine where SR_No=%s"
                                args-(medicine_srno)
                                cursore.execute(query,args)
                                row=cursore.fetchone()

                                if row is None or medicine_srno!=row[0]:
                                    print("Enter Correct Sr Number ")
                                    continue
                                else:
                                    viewmedicines = manager()
                                    viewmedicines.view_medicine(medicine_srno)
                        #Delete Medicine
                        elif choice==3:
                            medicine_srno=input("Enter Medicine SR Number")

                            if medicine_srno==" ":
                                print("Please Enter Sr No")
                            else:
                                deletemedicine=manager()
                                deletemedicine.dalete_medicine(medicine_srno)
                                print("Delete Medicine Successfuly")
                        
                        else:
                            print("Enter Correct Choice ")
                            continue

                        perform = input('Do you want to perform more operations Press "y" for yes or "n" for no: ')
                        if perform.lower()!= 'y':
                            break  
                            
            elif choice==3:
                break    
            else:
                print("Enter Correct Choice")
                continue
            
            perform = input('Go Back Manager Page press "y" for yes or "n" for no: ')
            if perform.lower()!= 'y':
                break          
    
    elif Role==3:
        break
    else:
        print("Enter Correct Role")
        continue





















                        










            



                