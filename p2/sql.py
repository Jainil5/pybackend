import sqlite3

connect = sqlite3.connect("data.db")


connect.execute(""" CREATE TABLE CUSTOMER
             (ID INT PRIMARY KEY NOT NULL,
             AGE INT NOT NULL);""")

connect.execute("INSERT INTO CUSTOMER (ID,NAME,AGE) VALUES (1,'JAINIL',22)")

connect.close()            