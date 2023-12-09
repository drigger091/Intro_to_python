from threading import Thread

# create a function comtaining to be executed pararelly

def display():

    for i in range(4):

        print("Hello World")


# create a new thread

t1 = Thread(target=display)

# start the new thread

t1.start()
