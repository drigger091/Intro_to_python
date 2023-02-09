import sqlite3

con = sqlite3.connect("appliation.db")

cur = con.cursor()


#creating the table

cur.execute(''' CREATE TABLE blogs
                (id text not null primary key,date text,title text,context text,public integer)''')

#insert few rows of data
cur.execute("INSERT INTO blogs VALUES('first-blog','2023-02-09','My third blog','Some content',1)")
cur.execute("INSERT INTO blogs VALUES('second-blog','2023-02-09','My second blog','private',0)")
cur.execute("INSERT INTO blogs VALUES('third-blog','2021-02-09','My first blog','not for common eyes',2)")




#saving the chnages
con.commit()


#closing the connection
con.close()