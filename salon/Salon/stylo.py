print("*****************************  Stylo Salon & Spa  *****************************  ")
a='b'
while(a=='b'):
 print('1.employee')
 print('2.client profile')
 print('3.packages')
 print('4.appointments')
 print('5.product for sale')
 print('6.exit')
 print("\n")
 sel=int(input('enter the number:'))
 if sel==1:
     def emp():
      print('1.add')
      print('2.update')
      print('3.display')
      print('4.search')
      print('5.delete')
      print('6.main menu')
      c=int(input("enter any number"))
      if c==1:
          addemp()
      if c==2:
          upemp()
      if c==3:
          disemp()
      if c==4:
          searchemp()
      if c==5:
          delemp()
      else :
          print('returning to main menu')
            
     def addemp():
        import mysql.connector
        try:
          mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
          mycursor=mydb.cursor()
          id=input('enter employee_id')
          name=input('enter employee name')
          no=input('enter phone no.')
          salary=input('enter salary')
          address=input('enter address')
          mycursor.execute("""insert into employee(employee_id,name,phone_no,salary,address)values(%s,%s,%s,%s,%s)""",(id,name,no,salary,address))
          mydb.commit()
          print("record inserted")
        except Exception as e:
           print(e)
           print("unable to add record,plz try again")
     def upemp():
        import mysql.connector
        try:
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo") 
         mycursor=mydb.cursor()
         i=input('enter employee_id')
         print("new data")
         v=input('enter employee id')
         w=input('enter employee name')
         x=input('enter phone no')
         y=input('enter salary')
         z=input('enter address')
         up=("update employee set employee_id=%s,name=%s,phone_no=%s,salary=%s,address=%s where employee_id=%s")
         data=(v,w,x,y,z,i)
         mycursor.execute(up,data)
         print("record updated")
         mydb.commit()
        except: 
         print("unable to update record,plz try again")
     def disemp():
        import mysql.connector
        from tabulate import tabulate
        try:
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
         mycursor=mydb.cursor()
         mycursor.execute("select*from employee")
         results=mycursor.fetchall()
         print(tabulate(results,headers=["employee_id","name","phone_no","salary","address"],tablefmt="grid"))
         print("record displayed")
        except:
         print("unable to display, plz try again")
     def searchemp():
        import mysql.connector
        from tabulate import tabulate
        try:
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
         mycursor=mydb.cursor()
         s=input('enter employee id')
         st=("select * from employee where employee_id='%s'"%(s))
         mycursor.execute(st)
         results=mycursor.fetchall()
         print(tabulate(results,headers=["employee_id","name","phone_no","salary","address"],tablefmt="grid"))
         print('record displayed')
        except:
         print("unable to display,plz try again")
     def delemp():
        import mysql.connector
        try:
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
         mycursor=mydb.cursor()
         i=input('employee id')
         e="delete from employee where employee_id='%s'"%i
         mycursor.execute(e)
         mydb.commit()
         print("record deleted")
        except:
            print("unable to delete,plz try again")
     emp()
 if sel==2:
     def cp():
      print('1.add')
      print('2.update')
      print('3.display')
      print('4.search')
      print('5.delete')
      print('6.main menu')
      f=int(input("enter any number"))
      if f==1:
           addcp()
      if f==2:
           upcp()
      if f==3:
           discp()
      if f==4:
           searchcp()
      if f==5:
           delcp()
      else:
           print('returning to the main menu')
           
     def addcp():
        import mysql.connector
        try:
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
         mycursor=mydb.cursor()
         name=input("enter name of client")
         no=input("enter phone number of client")
         treatment=input("enter treatment of client")
         amount=input("enter amount of treatment")
         mycursor.execute("""insert into client_profile(name,phone_no.,treatment,amount)values(%s,%s,%s,%s)""",(name,no,treatment,amount))
         mydb.commit()
         print("record inserted")
        except:
            print("unable to add record,plz try again")
     def upcp():
        import mysql.connector
        try:
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo") 
         mycursor=mydb.cursor()
         i=input('enter phone_no')
         print("new data")
         v=input('enter name of client')
         w=input('enter phone_no')
         x=input('enter treatment')
         y=input('enter amount')
         up=("update client profile set name of client=%s,phone_no=%s,treatment=%s,amount=%s where phone_no=%s")
         data=(v,w,x,y,i)
         mycursor.execute(up,data)
         print("record updated")
         mydb.commit()
        except: 
         print("unable to update record,plz try again")
     def discp():
        import mysql.connector
        try:
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
         mycursor=mydb.cursor()
         mycursor.execute("select * from client profile")
         results=mycursor.fetchall()
         for x in results:
             print(x)
         print("record displayed")
         mydb.commit()
        except:
         print("unable to display, plz try again")
     def  searchcp():
         import mysql.connector
         try:
          mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
          mycursor=mydb.cursor()
          s=input('enter phone_no')
          st="select * from client profile where phone_no='%s'"%(s)
          mycursor.execute(st)
          results=mycursor.fetchall()
          for x in results:
              print(x)
          print('record displayed')
          mydb.commit()
         except:
          print("unable to display,plz try again")
     def delcp():
        import mysql.connector
        try:
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
         mycursor=mydb.cursor()
         i=input('phone_no')
         e="delete from client profile where phone_no='%s'"%i
         mycursor.execute(e)
         mydb.commit()
         print("record deleted")
        except:
            print("unable to delete,plz try again")
     cp()
 if sel==3:
     def pak():
      print('1.add')
      print('2.update')
      print('3.display')
      print('4.modify')
      print('5.delete')
      print('6.main menu')
      g=int(input("enter number"))
      if g==1:
          addpak()  
      if g==2:
          uppak()
      if g==3:
          dispak()
      if g==4:
          searchpak()
      if g==5:
          delpak()
      else:
          print('returning to main menu')
           
     def addpak():
        import mysql.connector
        try:
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
         mycursor=mydb.cursor()
         no=input('enter s.no')
         name=input('enter package name')
         amount=input('enter amount')
         mycursor.execute("""insert into packages(s.no,package_name,amount)values(%s,%s,%s)""",(no,name,amount))
         mydb.commit()
         print('record inserted')
        except:
            print('unable to insert record,plz try again')
     def uppak():
        import mysql.connector
        try:
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo") 
         mycursor=mydb.cursor()
         i=input('enter s.no')
         print("new data")
         v=input('enter s.no')
         w=input('enter package name')
         x=input('enter amount')
         up=("update packages set s.no=%s,package name=%s,amount=%s where s.no=%s")
         data=(v,w,x,i)
         mycursor.execute(up,data)
         print("record updated")
         mydb.commit()
        except: 
         print("unable to update record,plz try again")
     def dispak():
        import mysql.connector
        try:
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
         mycursor=mydb.cursor()
         mycursor.execute("select * from packages")
         results=mycursor.fetchall()
         for x in results:
             print(x)
         print("record displayed")
         mydb.commit()
        except:
         print("unable to display, plz try again")
     def searchpak():
        import mysql.connector
        try:
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
         mycursor=mydb.cursor()
         s=input('enter s.no')
         st="select * from packages where s.no='%s'"%(s)
         mycursor.execute(st)
         results=mycursor.fetchall()
         for x in results:
             print(x)
         print('record displayed')
         mydb.commit()
        except:
         print("unable to display,plz try again")
     def delpak():
       import mysql.connector
       try:
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
         mycursor=mydb.cursor()
         i=input('s.no')
         e="delete from packages where s.no='%s'"%i
         mycursor.execute(e)
         mydb.commit()
         print("record deleted")
       except:
           print("unable to delete,plz try again")
     pak()
 if sel==4:
     def app():
      print('1.add')
      print('2.update')
      print('3.display')
      print('4.search')
      print('5.delete')
      print('6.main menu')
      h=int(input('enter number'))
      if h==1:
          addapp()
      if h==2:
          upapp()
      if h==3:
          disapp()
      if h==4:
          searchapp()
      if h==5:
          delapp()
      else:
          print('returning to the main menu')
          
     def addapp():
        import mysql.connector
        try:
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
         mycursor=mydb.cursor()
         name=input('enter name of client')
         no=input('enter phone no.')
         date=input('enter scheduled date')
         time=input('enter time')
         mycursor.execute("""insert into appointments(name,phone_no.,scheduled_date,time)values(%s,%s,%s,%s)""",(name,no,date,time))
         print('record inserted')
         mydb.commit()
        except:
            print('unable to insert record,plz try again')
     def upapp():
        import mysql.connector
        try:
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo") 
         mycursor=mydb.cursor()
         i=input('enter phone_no')
         print("new data")
         v=input('enter name of client')
         w=input('enter phone_no')
         x=input('enter scheduled_date')
         y=input('enter time')
         up=("update appointments set name of client=%s,phone_no=%s,scheduled_date=%s,time=%s where phone_no=%s")
         data=(v,w,x,y,i)
         mycursor.execute(up,data)
         print("record updated")
         mydb.commit()
        except: 
         print("unable to update record,plz try again")
     def disapp():
        import mysql.connector
        try:
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
         mycursor=mydb.cursor()
         mycursor.execute("select * from appointments")
         results=mycursor.fetchall()
         for x in results:
             print(x)
         print("record displayed")
         mydb.commit()
        except:
         print("unable to display, plz try again")
     def searchapp():
        import mysql.connector
        try:
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
         mycursor=mydb.cursor()
         s=input('enter s.no')
         st="select * from appointments where s.no='%s'"%(s)
         mycursor.execute(st)
         results=mycursor.fetchall()
         for x in results:
             print(x)
         print('record displayed')
         mydb.commit()
        except:
         print("unable to display,plz try again")
     def delapp():
        import mysql.connector
        try:
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
         mycursor=mydb.cursor()
         i=input('s.no')
         e="delete from appointments where s.no='%s'"%i
         mycursor.execute(e)
         mydb.commit()
         print("record deleted")
        except:
            print("unable to delete,plz try again")
     app()
 if sel==5:
     def prod():
      print('1.add')
      print('2.update')
      print('3.display')
      print('4.search')
      print('5.delete')
      print('6.main menu')
      i=int(input('enter number'))
      if i==1:
          addprod()
      if i==2:
          upprod()
      if i==3:
          disprod()
      if i==4: 
          searchprod()
      if i==5:
          delprod()
      else:
          print('returning to the main menu')
          
     def addprod():     
        import mysql.connector
        try:
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
         mycursor=mydb.cursor()
         name=input('enter product name')
         quantity=input('enter quantity')
         amount=input('enter amount')
         date=input('enter expiry date')
         mycursor.execute("""insert into product_for_sale(product_name,quantity,amount,expiry_date)values(%s,%s,%s,%s)""",(name,quantity,amount,date))
         mydb.commit()
         print('record inserted')
        except:
            print('unable to record,plz try again')
     def upprod():
        import mysql.connector
        try:
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo") 
         mycursor=mydb.cursor()
         i=input('enter product name')
         print("new data")
         v=input('enter product name')
         w=input('enter quantity')
         x=input('enter amount')
         y=input('enter expiry_date')
         up=("update product_for_sale set product name=%s,quantity=%s,amount=%s,expiry_date=%s where product name=%s")
         data=(v,w,x,y,i)
         mycursor.execute(up,data)
         print("record updated")
         mydb.commit()
        except: 
         print("unable to update record,plz try again")
     def disprod():
        import mysql.connector
        try:
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
         mycursor=mydb.cursor()
         mycursor.execute("select * from product_for_sale")
         results=mycursor.fetchall()
         for x in results:
             print(x)
         print("record displayed")
         mydb.commit()
        except:
         print("unable to display, plz try again")
     def searchprod():
        import mysql.connector
        try:
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
         mycursor=mydb.cursor()
         s=input('enter product name')
         st="select * from product_for_sale where product name='%s'"%(s)
         mycursor.execute(st)
         results=mycursor.fetchall()
         for x in results:
             print(x)
         print('record displayed')
         mydb.commit()
        except:
         print("unable to display,plz try again")
     def delprod():
        import mysql.connector
        try:
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
         mycursor=mydb.cursor()
         i=input('product name')
         e="delete from product_for_sale where product name='%s'"%i
         mycursor.execute(e)
         mydb.commit()
         print("record deleted")
        except:
            print("unable to delete,plz try again")
       
     prod()
 if sel==6:
     exit()
