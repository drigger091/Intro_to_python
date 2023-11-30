#types of exceptions we may find is that we cannot find the blog 
# we may come across a blog that is not public
#this one we are adding context manager and doing the application
#here the enter method will return a cursor method and we intiate the connection open and  close with sqlite class
                                              



#adding a context manager , which signifies what happens when an object is created and  destryoed and the file 

import sqlite3
class Sqlite:

    def __init__(self,file = "application.db"):
        self.file = file       
    def __enter__(self):
        self.conn = sqlite3.connect(self.file)
        return self.conn.cursor()   #returning a cursor object as it will be executable for query
    def __exit__(self,type,value,traceback):  # all these parameters are needed for it to work correctly
        self.conn.close()



class Notfounderror(Exception):
    pass


class Notauthorizederror(Exception):
    pass

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
    try:
        with Sqlite("application.db") as cur:
            
       


    #execute sql query

            cur.execute('SELECT * FROM blogs where public=1')

    #fetch the data and then turning into a dit for better representation in JSON

            result = list(map(blog_lst_conv_to_json,cur.fetchall()))
            return result

    except Exception as e:
        print(e)
        return []

   # we dont need the close statemnt anymore as the context manager closes the database connection
    # context manager helps creation and destruction of resources in a single place
    
    




def fetch_blog(id:str):

    #connect the database
    try:
        con = sqlite3.connect('application.db')
        cur = con.cursor()

    #query to fetch the data

        cur.execute(f"SELECT * FROM blogs where id = '{id}'")
        result = cur.fetchone()

        #if the result from the request retuns none , we are handling that exception as well
        if result is None:
            raise Notfounderror(f"Unable to find blog with id {id}.")

        data = blog_lst_conv_to_json(result)
        #now we have to check wther the return bloc is allowed to be viewed in public or not
        if not data['public']:
            raise Notauthorizederror(f"You are not authorized to access the blog with id {id}.")

        return data

    except sqlite3.OperationalError as ex1:
        print(ex1)

        raise Notfounderror(f"Unable to fin blog with id {id}.")
    finally:
        #close the database
        con.close()
