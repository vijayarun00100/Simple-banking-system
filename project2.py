#modules
from os import name
import tkinter
import mysql.connector 
import pickle
import csv
import qrcode 
#database connection
db=mysql.connector.connect(user="root",host="localhost",passwd="root123",auth_plugin="mysql_native_password",database="complaint") 
mycursor=db.cursor()
main_sql="SET SQL_SAFE_UPDATES=0" 
mycursor.execute(main_sql) 
db.commit() 

#decorator for the function
def dec(func):
    def wrapee():
        print("-------------------------------") 
        func() 
        print("---------------------")
        print("*********************")
    return wrapee

@dec
def add_user():
    cursor=db.cursor()
    a=input("enter ur name:") 
    b=input("enter phone_number:")
    c=input("enter ur complaint in 100-150 words:") 
    d=input("enter date (in the format dd/mm/yy):")  
    #using r strip to remove the space when given 
    name=a.rstrip()
    phone_number=b.rstrip()
    complaint=c.rstrip() 
    date=d.rstrip()
    sql="INSERT INTO complaint(name_,phone_number,complaint,date_) VALUES(%s,%s,%s,%s)"
    data=(name,phone_number,complaint,date)
    cursor.execute(sql,data)
    db.commit()
    print(cursor.rowcount ,"added successfully! :)")  

def database_():
    sql_select_Query = "select * from complaint"
    cursor = db.cursor()
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    
    
    for row in records:
        print("Total number of rows in table: ", cursor.rowcount,"\n")
        print("name = ", row[0], )
        print("phone number = ", row[1])
        print("complaint  = ", row[2])
        print("date  = ", row[3], "\n")

#qrcode creation 

img=qrcode.make('''
                  welcome to the project of banking ! 
                  in this project we have used sql and python to store the data 
                  of the users in a interactive way. The aim of the project is to 
                  collect the user's data from python and store it in the database. 

                  Here the database is mysql file. for using mysql we have used the 
                  mysql.connector. Then for making qrcode , qrcode module is imported 
                  . 

                  thank you !

''')

img.save(r"D:\vijay_project.png")

while True:
    try:
        print('''
                  menu 
                  1) add your complaint.
                  2) show the list of complaints.
                  3) exit.
        ''')
        ch=int(input("enter your choice:"))
        #1st code 
        if ch==1:    
          req=input("enter yes to add input:") 
          add_input = req.rstrip() 
          if add_input == "yes":
              add_user() 
              continue
          if add_input =="no":
              print("thank you") 
              break
          else:
              print("enter a valid input!") 
              continue 
        #2nd code 
        if ch==2:
            print("the records are:","\n")
            database_()
        if ch==3:
            break  
    except EOFError:
        print("our server is quiet busy , pleease try again later :( ") 
