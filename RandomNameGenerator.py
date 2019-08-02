import json
import random
import mysql.connector
import time 
start = time.time()

with open("Names.json","r") as f:
    data = f.read()    

# names = json.load(data)
data = data.replace('"',"")
data = data.replace(',',"")

nameList = data.split()
length = len(nameList)
FL = []
for i in range(1000000):
    F = nameList[random.randint(0,length-1)]
    L = nameList[random.randint(0,length-1)]
    FL.append([F, L])

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