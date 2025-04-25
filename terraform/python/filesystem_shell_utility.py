import shutil
import os
from os import path
from zipfile import ZipFile

fname = "strtext.txt"

def fsops():
    if path.exists(fname):
    #get the path to the original file
        print ("ABSOLUTE PATH", path.abspath(fname))
        src =  path.realpath(fname)
        dest = src + ".bkp"
    #copy the file to destination
        shutil.copy(src, dest)
        
    #archive all the files to a folder
        (root_dir, fln) = path.split(src)
        shutil.make_archive("things", "zip", root_dir)
        
        #create a custom zip file with the contents we need
    with ZipFile("newzipfile.zip","w") as newzip:
        newzip.write("strtext.txt")
        newzip.write("strtext.txt.bkp")
        
        
fsops()