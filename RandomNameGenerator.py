import json
import random
import mysql.connector
import time 
start = time.time()

with open("Names.json","r") as f: # Opens the name json
    data = f.read() # stores the json data in var

data = data.replace('"',"") # removes all "
data = data.replace(',',"") # removes all ,

nameList = data.split() # Turns into list
length = len(nameList) # gets length of list
FL = [] # empty list
for i in range(1000000):
    F = nameList[random.randint(0,length-1)] # gets random name from list
    L = nameList[random.randint(0,length-1)] # gets random name from list
    FL.append([F, L]) # Takes first and last name into a list 

print("Names Made")

cnx = mysql.connector.connect(user='python', password='python',database='wcgw',buffered = True) # connect to the SQL server 
cursor = cnx.cursor() # makes a short hand for ease of writting code
print("Connected to server")


for i in range (len(FL)):
    PN = ''
    for j in range(10):
        PN+= str(random.randint(0,10))
    cursor.execute("INSERT INTO customers (`FirstName`, `LastName`, `PhoneNumber`) " \
                   f"VALUES ('{FL[i][0]}', '{FL[i][1]}', '{PN}');") # runs a SQL querry to count the number of rows

cnx.commit()

elapsed = time.time() - start

print(elapsed, "Done!")