import mysql.connector as my
import json

# to check connection is possible
def newConnect():
    db = my.connect(host='localhost', user='root', password='')
    if not db:
        print("Connection to the database failed !")
    return db


# to creat data base if not exist
def createDatabase():
    db = newConnect()
    cur = db.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS chatbot")


# to check connection to chat bot databse is possible
def connect():
    db = my.connect(host='localhost', user='root', password='', database="chatbot")
    if not db:
        print("Failed to connect to chatbot's database !")
    return db


def createTable():
    db = connect()
    cur = db.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS data( username VARCHAR(30),email VARCHAR(30), pass VARCHAR(10), passManage JSON , bdayManage JSON , timeManage JSON  ) ")
    db.commit()


def insert(name, email, passw, p , b, t ):
    db = connect()
    cur = db.cursor()
    query = "INSERT INTO data (username , email , pass, passManage, bdayManage, timeManage) VALUES (%s , %s, %s, %s, %s,%s)"
    values = (name, email, passw,p,b,t)
    cur.execute(query, values)
    db.commit()


def isMailPresent(m):
    db = connect()
    cur = db.cursor()
    query = "SELECT email FROM data"
    cur.execute(query)
    list=cur.fetchall()
    for i in list:
        if m == i[0]:
            print("Email found !!")
            return True
    return False

def checkPass(emaill,passw):
    db = connect()
    cur = db.cursor()
    query = "SELECT pass FROM data WHERE email = %s"
    values = (emaill,)
    cur.execute(query, values)
    smail = cur.fetchone()
    print(smail)
    if smail[0] == passw:
        return True
    return False

def bringData(s):
    db = connect()
    cur = db.cursor()
    pquery="SELECT passManage, bdayManage, timeManage FROM data WHERE email= %s "
    valuep=(s,)
    cur.execute(pquery,valuep)
    # print(cur.fetchone())
    return tuple(map(lambda dicts: json.loads(dicts), cur.fetchone()))

def sendData(dicts,mail):
    # pwd, bday, meet
    # s.sendData((pwd,bday,meet),str_mail)
    db = connect()
    cur = db.cursor()
    pwd = json.dumps(dicts[0])
    bday = json.dumps(dicts[1])
    meet = json.dumps(dicts[2])
    # pwd, bday, meet = dicts
    print(type(pwd))
    print(pwd)
    print(bday)
    print(meet)
    # d = {"hi":1}
    # query="UPDATE data SET passManage = JSON_REPLACE(passManage, %s, %s) WHERE email = 'jeet2@gmail.com'"
    query="UPDATE data SET passManage = %s , bdayManage = %s , timeManage = %s WHERE email = 'jeet2@gmail.com'"
    # query = "UPDATE `data` SET `passManage`='%s' WHERE email='jeet2@gmail.com'"
    values=('{"hi":9}','{"hi":2}','{"hi":4, "PL":3}',)
    # query="UPDATE data SET passManage=%s WHERE email=%s"
    # values=("b"+f"\'{pwd}\'",mail)
    cur.execute(query, values)
    

createDatabase()
createTable()
p2={"hi":9}
b2={"hi":2}
m2={"hi":4, "PL":3}
sendData((p2,b2,m2),"jeet2@gmail.com")

# bringData("jeet2@gmail.com")
