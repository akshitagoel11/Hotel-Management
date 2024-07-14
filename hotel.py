#Project Name     :Hotel Management System  
#Made by          :Akshita and Bulbul  
#session          :2022-23  
  
import mysql.connector def 
settings():  
    conn = 
mysql.connector.connect(host='localhost',database='hotel_management_sbps',user='ro 
ot',password='admin')     cursor=conn.cursor()     sql = "select * from setting;"     
cursor.execute(sql)     records=cursor.fetchall()     for i in records:  
        print(i)  
  
def clear():     for _ in 
range (65):  
        print()  
   
def showcustomer():  
    conn = mysql.connector.connect(host='localhost', 
database='hotel_management_sbps', user='root', password='admin')     
cursor=conn.cursor()     sql = "select * from customer;"     
cursor.execute(sql)     record=cursor.fetchall()     for i in record:  
        print(i)  
  
def add_customer():  
    conn = mysql.connector.connect(host='localhost', 
database='hotel_management_sbps', user='root', password='admin') 
cursor = conn.cursor() name = input ('Enter Customer Name :')  
address = input ('Enter Customer Address: ')  
    phone=input (' Enter Customer Phone NO :')     email = input (' Enter 
Customer Email ID :')     id_proof=input (' Enter Customer ID 
(Aadhar/Passport/DL/VoterID) :')     id_proof_no = input(' Enter 
Customer ID proof NO :')     males = input ('Enter Total Males :')     
females= input ('Enter Total Females :')     children= input ('Enter Total 
Children :')     sql='insert into  
customer(name,address,phone,email,id_proof,id_proof_no,males,females,children)valu 
es \  
         
("'+name+'","'+address.upper()+'","'+phone+'","'+email.upper()+'","'+id_proof.upper()+' 
","'+id_proof_no.upper()+'",'+males+','+females+','+children+');'  
      
    cursor.execute(sql)     conn.commit()     
print('\n\n\nCustomer Added successfully......... ')     
conn.close()     wait = input('\n\n\n Press any key to 
continue......')  
  
def show_roomtype():  
    conn = mysql.connector.connect(host='localhost', 
database='hotel_management_sbps', user='root', password='admin')     
print('ALL records of Types of Rooms available')     
cursor=conn.cursor()     sql="select * from roomtype;"     
cursor.execute(sql)     record=cursor.fetchall()     for i in record:  
        print(i)  
          
def roomrent():  
    conn = mysql.connector.connect(host='localhost', 
database='hotel_management_sbps', user='root', password='admin')     
print("WE HAVE THE FOLLOWING ROOMS FOR YOU:-") print("1. 
Single Room RS 2000 Per Night") print("2. Double Room RS 3000 Per 
Night")  
print("3. Triple Room RS 4000 Per Night")  
    print("4. King   Room RS 6000 Per Night")     
x=int(input("ENTER YOUR CHOICE PLEASE->"))     
n=int(input("FOR HOW MANY NIGHTS DID YOU STAY: "))     
if(x==1):  
        print("YOU HAVE Chosen Single Room")         
s=2000*n     elif(x==2):  
        print("YOU HAVE Chosen Double Room")         
s=3000*n     elif(x==3):  
        print("YOU HAVE Chosen Triple Room")         
s=4000*n     elif(x==4):  
        print("YOU HAVE Chosen King Room")         
s=6000*n     else:  
        print("PLEASE CHOOSE A ROOM")     
print("your room rent is =",s,"\n")  
  
def laundrymenu():  
    conn = mysql.connector.connect(host='localhost', 
database='hotel_management_sbps', user='root', password='admin')  
      
    print('All records of Laundry')     
cursor=conn.cursor()     
sql="select * from Laundry;"     
cursor.execute(sql)     
record=cursor.fetchall()     for i 
in record:  
        print(i)  
        
def add_laundry():  
    conn = mysql.connector.connect(host='localhost', 
database='hotel_management_sbps', user='root', password='admin')     
cursor=conn.cursor() sql="select * from Laundry;" 
cursor.execute(sql)  
record=cursor.fetchall()  
    for i in record:  
        print(i)  
      
    L=[]  
    sno=input("ENTER Dress Item Serial No.:")     
L.append(sno)  
    itemname=input("ENTER ITEM TO BE WASHED NAME:")     
L.append(itemname)  
    rate=input("ENTER RATE Per Piece:")     L.append(rate)     
laundry=(L)     sql="insert into 
Laundry(sno,itemname,rate)values(%s,%s,%s)"     
cursor.execute(sql,laundry)     conn.commit()     print('Record 
inserted')  
  
def lbill():  
    conn = mysql.connector.connect(host='localhost', 
database='hotel_management_sbps', user='root', password='admin')     
print('All records of Laundry')     cursor=conn.cursor()     sql="select * 
from Laundry;"     cursor.execute(sql)     record=cursor.fetchall()     for 
i in record:  
        print(i)     
s=0  
  
    while True:  
        c_wash=int(input("enter your choice of clothes to be washed"))         
n=int(input("enter no. of clothes to be washed"))  
        L=[]         for i 
in record:             
a=list(i)  
            L.append(a)         
for j in L:             if 
j[0]==c_wash:                 
rate=n*j[2]                 
s=s+rate                 
print("your bill for this 
cloth",s)         
ch=input("do you 
want to wash more 
clothes?(y/n):")  
          
        if ch in 'yY':             
continue         
else:             
break  
          
def show_game():  
    conn = mysql.connector.connect(host='localhost', 
database='hotel_management_sbps', user='root', password='admin')     
print('ALL Games available')     cursor=conn.cursor()     sql="select * 
from game;"     cursor.execute(sql)     record=cursor.fetchall()     for i 
in record:  
        print(i)  
      
  
def add_game():  
    conn = mysql.connector.connect(host='localhost', 
database='hotel_management_sbps', user='root', password='admin')     
c1=conn.cursor()     sql="select * from game;"     c1.execute(sql)     
record=c1.fetchall()     for i in record:  
        print(i)  
      
    L=[]  
    sno=input("ENTER Game No.:")     
L.append(sno)  
    gamename=input("ENTER GAME NAME:")     
L.append(gamename)     charges=input("ENTER 
CHARGES:")  
    L.append(charges)     game=(L)     sql="insert into 
game(sno,gamename,charges)values(%s,%s,%s)"     
c1.execute(sql,game)     conn.commit()     print('Game inserted')  
  
def gamebill():  
    conn = mysql.connector.connect(host='localhost', 
database='hotel_management_sbps', user='root', password='admin')     
print('All records of games')     cursor=conn.cursor()     sql="select * 
from game;"     cursor.execute(sql)     record=cursor.fetchall()     for i 
in record:  
        print(i)     
s=0  
  
    while True:  
        c_game=int(input("enter your choice of game"))         
n=int(input("enter no. of hours to play"))  
        L=[]         for i 
in record:             
a=list(i)  
            L.append(a)         for j in L:             if j[0]==c_game:                 
rate=n*j[2]                 s=s+rate                 print("your bill for 
this game",s)         ch=input("do you want to play any other 
game?(y/n):")  
          
        if ch in 'yY':             
continue         
else:             
break  
          
def show_restaurant():  
    conn = mysql.connector.connect(host='localhost', 
database='hotel_management_sbps', user='root', password='admin')     
print(' MENU')     cursor=conn.cursor()     sql="select * from 
restaurant;"     cursor.execute(sql)     record=cursor.fetchall()     for i 
in record:  
        print(i)  
  
     
def add_restaurant():  
    conn = mysql.connector.connect(host='localhost', 
database='hotel_management_sbps', user='root', password='admin')     
cursor=conn.cursor()     print('         MENU')     sql="select * from 
restaurant;"     cursor.execute(sql)     record=cursor.fetchall()     for i 
in record:  
        print(i)     
L=[]  
    sno=input("ENTER FOOD ITEM No.:")     
L.append(sno)  
    f=input("ENTER ITEM NAME:")     
L.append(f)  
    charges=input("ENTER CHARGES:")     
L.append(charges)  
    f=(L)  
    sql="insert into restaurant(sno,item,rate)values(%s,%s,%s)"     
cursor.execute(sql,f)     conn.commit()  
    print('Food Item inserted')  
  
  
  
  
def restaurantbill(): 
    conn = mysql.connector.connect(host='localhost', 
database='hotel_management_sbps', user='root', password='admin')     
print('All records of dishes')     cursor=conn.cursor()     sql="select * 
from restaurant;"     cursor.execute(sql)     record=cursor.fetchall()     
for i in record:  
        print(i)     
s=0  
  
    while True:  
        c_dish=int(input("enter your choice of dish"))         
n=int(input("enter no. of servings you want"))  
        L=[]         for i 
in record:             
a=list(i)  
            L.append(a)         for j in L:             if j[0]==c_dish:                 
rate=n*j[2]                 s=s+rate                 print("your bill for 
this dish",s)         ch=input("do you want to eat any other 
dish?(y/n):")  
          
        if ch in 'yY':             
continue         else:  
            break  
          
def menu():  
      print()  
      
print("*********************************************************")       
print(              "         HOTEL  MANAGEMENT  SYSTEM  Project")       print("1.show 
settings of the hotel")       print("2.  Show all customers' Detail")       print("3.  Add 
new customer Detail")  
      print("4.  Show Types of Rooms available")       print("5.  Ask Customer choice of 
rooms and calculate charges according to stay")       print("6.  Show Laundry menu")       
print("7.  Add details of Items and Charges in Laundry")       print("8. Laundry Bill")       
print("9. Show all Games List")       print("10. Add details of Items and Charges")       
print("11. Game Bill")       print("12. Show Menu of Restaurant")       print("13. Add 
details of food items available in restaurant")       print("14. Restaurant Bill")  
print("***********************************************************") 
menu() opt="" opt=int(input("enter your choice: ")) if opt==1:     settings() elif 
opt==2:  
showcustomer() elif 
opt==3:  
add_customer() elif 
opt==4:  
show_roomtype() 
elif opt==5:     
roomrent() elif 
opt==6:  
laundrymenu() elif 
opt==7:  
add_laundry() elif 
opt==8:  
lbill() elif 
opt==9:  
show_game() 
elif opt==10:     
add_game() elif 
opt==11:     
gamebill() elif 
opt==12:     
show_restaura
 nt() elif 
opt==13:     
add_restaurant
 () elif opt==14:     
restaurantbill() 
else:     
print('invalid 
option') 
