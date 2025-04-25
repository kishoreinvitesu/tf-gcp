import os
from os import path
import time
import datetime
from datetime import date, timedelta

#operating system functions
print (os.name)

#use path module to check the file path operations
#check for the item exists or not
print ("Item in the path exists", path.exists("strtext.txt"))

#check if the item is of file or dir
def filecheck ():
    if path.isfile("strtext.txt"):
        print ("The item is a file")
    else:
        print ("The item is not a file")

def dircheck():
    if path.isdir("..\python"):
        print ("the item is dir")
    else:
        print ("the item is not dir")

#get the real path of the file
print (path.realpath("strtext.txt"))
print (path.split(path.realpath("strtext.txt")))

def timemodules():
    #get the readable time of the file using getmtime of path module
    mod_time = time.ctime(path.getmtime("strtext.txt"))
    print ("modifiled time of the file is", mod_time)       
    
    #get timestamp of the file modified
    print ("modidifed time stamp", datetime.datetime.fromtimestamp(path.getmtime("strtext.txt")))

def deltatimecalculation():
     tdy_time = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("strtext.txt"))
     print(tdy_time)
     
     
filecheck()
dircheck()
timemodules()
deltatimecalculation()

