import mysql.connector
def create():
     #table product is for admin side
    myc=mysql.connector.connect(host="localhost",user='root',password='Aarya0308',database="mall")
    mycursor=myc.cursor()
    if myc.is_connected():
             print("connected")
    else:
        print("server not connected")
          
    mycursor.execute("create database if not exists mall")
    
   
    mycursor.execute("create table if not exists product (pid integer primary key,name varchar(20),category varchar(30),quantity integer,price decimal)")
    mycursor.close()
    myc.close()
create()

def addproduct():
     #adding product in table product for admin
        myc=mysql.connector.connect(host="localhost",user='root',password='Aarya0308',database="mall")
        mycursor=myc.cursor()
        no=int(input('enter no of products:'))
        for i in range(no):
             pid=int(input('enter product id:'))
             name=input('enter name of the product:')
             category=input('enter category:')
             quantity=int(input('enter quantity'))
             price=int(input('enter price:'))
             sql="insert into product values(%s,%s,%s,%s,%s)"
             value=(pid,name,category,quantity,price)
             mycursor.execute(sql,value)
        mycursor.close()
        myc.commit()
        myc.close()

def deleteproduct():
    
    #deleting product from table product for admin
    myc=mysql.connector.connect(host="localhost",user='root',password='Aarya0308',database="mall")
    mycursor=myc.cursor()
    no=int(input('enter no of products to be deleted:'))
    for i in range(no):
        pid=int(input("enter productid to be deleted"))
        sql="delete from product where pid=%s"
        val=(pid,)
        mycursor.execute(sql,val)
    mycursor.close()
    myc.commit()
    myc.close()

def modifyproduct():
            #modify name,category,quantity,price in table product for admin
            myc=mysql.connector.connect(host="localhost",user='root',password='Aarya0308',database="mall")
            mycursor=myc.cursor()
            no=int(input('enter no of products to be modified:'))
            for i in range(no):
                pid=int(input("enter product no to be modified"))
                name=input('enter new name of the product:')
                quantity=int(input("enter new quantity"))
                category=input('enter new category:')
                price=float(input("enter new price"))
                sql="update product set name=%s,category=%s,quantity=%s,price=%s where pid=%s"
                val=(name,category,quantity,price,pid)
                mycursor.execute(sql,val)
            mycursor.close()
            myc.commit()
            myc.close()

def displayaproduct():
    #displaying product details of the product whose pid is entered by the user(table-product for admin)
    myc=mysql.connector.connect(host="localhost",user='root',password='Aarya0308',database="mall")
    mycursor=myc.cursor()
    pid=int(input("enter pid of the product to be displayed"))
    sql="select*from product where pid=%s"
    val=(pid,)
    mycursor.execute(sql,val)
    result=mycursor.fetchall()
    for i in result:
        print(i)
    mycursor.close()
    myc.close()
    
def displayallproducts():
     #displaying all th products in the product table(admin side)
     myc=mysql.connector.connect(host="localhost",user='root',password='Aarya0308',database="mall")
     mycursor=myc.cursor()
     sql="Select * from product" 
     mycursor.execute(sql) 
     result=mycursor.fetchall() 
     for x in result: 
        print(x)
     mycursor.close()
     myc.close()
     
#table custad is for admin side
def createtb():
    myc=mysql.connector.connect(host="localhost",user='root',password='Aarya0308',database="mall")
    mycursor=myc.cursor()
    mycursor.execute('create table if not exists custad(custid int primary key,name varchar(25),lastbillamt decimal,points int)')
    mycursor.close()
    myc.close()
createtb()
def addacustomer():
     #adding a customer in table custad(admin side)
     myc=mysql.connector.connect(host="localhost",user='root',password='Aarya0308',database="mall")
     mycursor=myc.cursor()
     no=int(input('enter no of customers:'))
     for i in range(no):
         custid=int(input("enter customer id"))
         name=input("enter name")
         lastbillamt=int(input("enter last bill amt"))
         points=int(input("enter points"))
         sql="insert into custad values (%s,%s,%s,%s)"
         val=(custid,name,lastbillamt,points)
         mycursor.execute(sql,val)
     mycursor.close()
     myc.commit()
     myc.close()
    
    
def deletecustomer():
    #deleting customer from table custad(admin side)
    myc=mysql.connector.connect(host="localhost",user='root',password='Aarya0308',database="mall")
    mycursor=myc.cursor()
    no=int(input('enter no of customers to be deleted:'))
    for i in range(no):
        custid=int(input("enter cust id to be deleted"))
        sql="delete from custad where custid=%s"
        val=(custid,)
        mycursor.execute(sql,val)
    mycursor.close()
    myc.commit()
    myc.close()

def addpoints():
    #adding points in table custad(admin side)
    myc=mysql.connector.connect(host="localhost",user='root',password='Aarya0308',database="mall")
    mycursor=myc.cursor()
    custid=int(input("enter cust id where points are to be added"))
    poi=int(input("enter points to be added"))
    sql="update custad set points=points+%s where custid=%s"
    val=(poi,custid)
    mycursor.execute(sql,val)
    mycursor.close()
    myc.commit()
    myc.close()
    
def displaypoints():
    #displaying points of the customer from table custad(admin side)
    myc=mysql.connector.connect(host="localhost",user='root',password='Aarya0308',database="mall")
    mycursor=myc.cursor()
    custid=int(input("enter cust id where points are to be displayed"))
    sql="select points from custad where custid=%s"
    val=(custid,)
    mycursor.execute(sql,val) 
    result=mycursor.fetchall() 
    for x in result: 
        print("total points=",x)
    mycursor.close()
    myc.close()
    
def displaybill():
    #displaying last bill of the customer from table custad(admin side)
    myc=mysql.connector.connect(host="localhost",user='root',password='Aarya0308',database="mall")
    mycursor=myc.cursor()
    custid=int(input("enter cust id "))
    sql="select lastbillamt from custad where custid=%s"
    val=(custid,)
    mycursor.execute(sql,val) 
    result=mycursor.fetchone() 
    for x in result: 
        print("last bill amount is",x)  
    mycursor.close()
    myc.close()
    
    
def createtbl():
    #table employee for admin
    myc=mysql.connector.connect(host="localhost",user='root',password='Aarya0308',database="mall")
    mycursor=myc.cursor()    

    mycursor.execute('create table if not exists employee (empid integer primary key,name varchar(20),salary integer)')
    mycursor.close()
    myc.close()
def addemp():
    #adding employee in table employee(admin side)
    myc=mysql.connector.connect(host="localhost",user='root',password='Aarya0308',database="mall")
    mycursor=myc.cursor()
    empid=int(input("enter employee id"))
    name=input("enter name")
    salary=int(input("enter salary"))
    sql="insert into employee values (%s,%s,%s)"
    val=(empid,name,salary)
    mycursor.execute(sql,val)
    mycursor.close()
    myc.commit()
    myc.close()

def incsal():
    #increasing salary of employee in table employee(admin side)
    myc=mysql.connector.connect(host="localhost",user='root',password='Aarya0308',database="mall")
    mycursor=myc.cursor()
    empid=int(input("enter empid"))
    sal=int(input("enter amount to be increased"))
    sql="update employee set salary=salary+%s where empid=%s"
    val=(sal,empid)
    mycursor.execute(sql,val)
    mycursor.close()
    myc.commit()
    myc.close()

def deleteemp():
    #deleting emp from table employee(admin side)
    myc=mysql.connector.connect(host="localhost",user='root',password='Aarya0308',database="mall")
    mycursor=myc.cursor()
    empid=int(input("enter empid to be deleted"))
    sql="delete from employee where empid=%s"
    val=(empid,)
    mycursor.execute(sql,val)
    mycursor.close()
    myc.commit()
    myc.close()
    
def modifyemp():
    #modifying name,salary in table employee(admin side)
    myc=mysql.connector.connect(host="localhost",user='root',password='Aarya0308',database="mall")
    mycursor=myc.cursor()
    empid=int(input("enter empid to be modified"))
    name=input("enter new name")
    salary=int(input("enter new salary"))
    sql="update employee set name=%s,salary=%s where empid=%s"
    val=(name,salary,empid) 
    mycursor.execute(sql,val)
    mycursor.close()
    myc.commit()
    myc.close()

def searchemp():
     #displaying details of an emp from table employee(admin side)
    myc=mysql.connector.connect(host="localhost",user='root',password='Aarya0308',database="mall")
    mycursor=myc.cursor()
    empid=int(input("enter empid"))
    sql="select*from employee where empid=%s"
    val=(empid,)
    mycursor.execute(sql,val)
    result=mycursor.fetchall() 
    for x in result: 
        print(x)  
    mycursor.close()
    myc.close()
     
def displayallemp():
    #displaying details of all employees
    myc=mysql.connector.connect(host="localhost",user='root',password='Aarya0308',database="mall")
    mycursor=myc.cursor()
    sql="select*from employee"
    mycursor.execute(sql)
    result=mycursor.fetchall() 
    for x in result: 
        print(x)  
    mycursor.close()
    myc.close()


 
#for customer side    
def allpro():
    #for viewing all products from table product(customer side)
    myc=mysql.connector.connect(host="localhost",user='root',password='dpss',database="mall")
    mycursor=myc.cursor()
    sql="select*from product"
    mycursor.execute(sql)
    result=mycursor.fetchall() 
    for x in result: 
        print(x)  
    mycursor.close()
    myc.close()
    
def menpro():
    #for viewing products from men's section from table product(customer side)
    myc=mysql.connector.connect(host="localhost",user='root',password='dpss',database="mall")
    mycursor=myc.cursor()
    sql="select*from product where category='mens'"
    mycursor.execute(sql)
    result=mycursor.fetchall() 
    for x in result: 
        print(x)  
    myc.close()
    
def womenpro():
    #for viewing products from women's section from table product(customer side)
    myc=mysql.connector.connect(host="localhost",user='root',password='dpss',database="mall")
    mycursor=myc.cursor()
    sql="select*from product where category='women'"
    mycursor.execute(sql)
    result=mycursor.fetchall() 
    for x in result: 
        print(x)  
    mycursor.close()
    myc.close()

def kidspro():
    #for viewing products from kids section from table product(customer side)
    myc=mysql.connector.connect(host="localhost",user='root',password='dpss',database="mall")
    mycursor=myc.cursor()
    sql="select*from product where category='kids'"
    mycursor.execute(sql)
    result=mycursor.fetchall() 
    for x in result: 
        print(x)  
    mycursor.close()
    myc.close()
    
def pro1000():
    #for viewing products under 1000 from table product(customer side)
    myc=mysql.connector.connect(host="localhost",user='root',password='dpss',database="mall")
    mycursor=myc.cursor()
    sql="select*from product where price<1000"
    mycursor.execute(sql)
    result=mycursor.fetchall() 
    for x in result: 
        print(x)  
    mycursor.close()
    myc.close()
    

def  generatebill():
    #for generating bill from table product(customer side)
    myc=mysql.connector.connect(host="localhost",user='root',password='dpss',database="mall")
    mycursor=myc.cursor()
    pid=int(input("enter product id "))
    quantity=int(input("enter quantity"))
    sql="select price from product where pid=%s"
    val=(pid,)
    mycursor.execute(sql,val)
    result=mycursor.fetchone() 
    for x in result: 
        print(x*quantity)  
    mycursor.close()
    myc.close()
    
def viewpts():
    #for viewing points from table custad(customer side)
    myc=mysql.connector.connect(host="localhost",user='root',password='dpss',database="mall")
    mycursor=myc.cursor()
    custid=int(input("enter customer id"))
    sql="select points from custad where custid=%s"
    val=(custid,)
    mycursor.execute(sql,val)
    result=mycursor.fetchall() 
    for x in result: 
        print(x)  
    mycursor.close()
    myc.close()
    
def lastamt():
     #for viewing last bill amt from table custad(customer side)
     myc=mysql.connector.connect(host="localhost",user='root',password='dpss',database="mall")
     mycursor=myc.cursor()
     custid=int(input("enter customer id"))
     sql='select lastbillamt from custad where custid=%s'
     val=(custid,)
     mycursor.execute(sql,val)
     result=mycursor.fetchall() 
     for x in result: 
        print(x)  
     mycursor.close()
     myc.close()
 
    
 
print('1.admin')
print('2.customer')
ch=int(input("enter choice"))
if ch==1:
     print("1.details relating to product")
     print('2.details relating to customer')
     print('3.details relating to employee')
     c=int(input("enter choice"))
     if c==1:
         print("1.add product")
         print("2.delete product")
         print("3.modify product")
         print("4.display a product")
         print("5.display all products")
         choice=int(input("enter choice"))
         if choice==1:
             addproduct()
                     
         elif choice==2:
             deleteproduct()
         elif choice==3:
             modifyproduct()
         elif choice==4:
             displayaproduct()
         elif choice==5:
             displayallproducts()
     elif c==2:
        print("1.add a customer")
        print("2.delete a customer")
        print("3.add points")
        print("4.display points")
        print("5.display bill amount")
        choice=int(input("enter choice"))
        if choice==1:
            addacustomer()
        elif choice==2:
            deletecustomer()
        elif choice==3:
            addpoints()
        elif choice==4:
            displaypoints()
        elif choice==5:
            displaybill()
     elif c==3:
        print("1.add employee")
        print("2.increase salary")
        print("3.delete employee")
        print("4.modify employee")
        print("5.seardh employee")
        print("6.display all employees")
        choice=int(input("enter choice"))
        if choice==1:
            addemp()
        elif choice==2:
            incsal()
        elif choice==3:
            deleteemp()
        elif choice==4:
            modifyemp()
        elif choice==5:
            searchemp()
        elif choice==6:
            displayallemp()
elif ch==2:
    print("1.view products")
    print("2.view your information or generate bill")
    c=int(input("enter choice"))
    if c==1:
        print("1.view all products")
        print("2.view men's section")
        print("3.view women's section")
        print("4.view kid's section")
        print("5.view products under 1000")
        choice=int(input("enter choice"))
        if choice==1:
            allpro()
        elif choice==2:
            menpro()
        elif choice==3:
            womenpro()
        elif choice==4:
            kidspro()
        elif choice==5:
            pro1000()
    elif c==2:
        print("1.generate bill")
        print("2.view no. of points")
        print("3.view last bill amt")
        choice=int(input("enter choice"))
        if choice==1:
            generatebill()
        elif choice==2:
            viewpts()
        elif choice==3:
            lastamt()

