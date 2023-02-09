import sqlite3

def blog_lst_conv_to_json(item):

    return {
        'id':item[0],
        'published':item[1],
        'title':item[2],
        'content':item[3],
        'public':bool(item[4])
    }


def fetch_blogs():

    #connect to the database

    con = sqlite3.connect("appliation.db")

    cur = con.cursor()


    #execute sql query

    cur.execute('SELECT * FROM blogs where public=1')

    #fetch the data and then turning into a dit for better representation in JSON

    result = list(map(blog_lst_conv_to_json,cur.fetchall()))

    #close the database
    cur.close()

    return result
