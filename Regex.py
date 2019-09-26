import sqlite3
con = sqlite3.connect('mydb.sqlite3')
# import pymysql
# con = pymysql.connect(host='' , user='' , password='' , db ='')
cur = con.cursor()
query = """CREATE TABLE IF NOT EXISTS LOGDATA(
            IP VARCHAR(100),
            username VARCHAR(100),
            timestamp VARCHAR(100),
            accessrequest VARCHAR(100),
            result VARCHAR(100),
            byte VARCHAR(100),
            url VARCHAR(100),
            agent VARCHAR(100))"""
cur.execute(query)

myurl = 'https://www.jafsoft.com/searchengines/log_sample.html'
import urllib.request as u
F =u.urlopen(myurl)

import re as reg

for line in F:
    #print(line)
    line = line.decode()
    m = reg.match('(\d{3}\.\d{3}[.]\d{1,3}\.[0-9]{3}).*(\D{2})(\d{1,2}/[A-Za-z]{3}/\d{4}).*GET\s+/(pics/(\w+\.\w+))?.*(http[s]?.//\S+)</A>.*' , line)
    # \d = digit
    # \D = non digit
    # . = Any char
    # * = 0 or more
    # + = 1 or more
    # ? = 0 or one
    if m != None:
        ip = m.group(1)
        #print(ip)
        username = m.group(2)
        #print(username)
        date = m.group(3)
        #print(date)
        im = m.group(5)
        if im == None:
            im = 'No Image'
        wb = m.group(6)
        print(wb)
        #print(ip, date, im , wb)


import pandas as pd
L1 = [[10,20,30],[40,50,60]]
L2 = list([[10,20,30],[40,50,60]])
df1 = pd.DataFrame([[10,20,30],[40,50,60]])
print(L1, L2, df1, sep='\n')