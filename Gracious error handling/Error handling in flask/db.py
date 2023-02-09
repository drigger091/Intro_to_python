import sqlite3

con = sqlite3.connect("application.db")

cur = con.cursor()


#creating the table

cur.execute(''' CREATE TABLE blogs
                (id text not null primary key,date text,title text,context text,public integer)''')

#insert few rows of data
cur.execute("INSERT INTO blogs VALUES('4th-blog','2023-02-09','My fourth blog','Some content',1)")
cur.execute("INSERT INTO blogs VALUES('3rd-blog','2023-02-09','My third blog','private',0)")
cur.execute("INSERT INTO blogs VALUES('2nd-blog','2021-02-09','My second blog','not for common eyes',1)")
cur.execute("INSERT INTO blogs VALUES('1st-blog','2020-02-09','My first blog','not for common eyes',1)")





#saving the chnages
con.commit()


#closing the connection
con.close()