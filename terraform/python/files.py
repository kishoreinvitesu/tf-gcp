
def filess():
    #open the file and create it if it doesn't exits
    myfile = open("stringtext.txt","w+")
    #write some thing to the file
    print ("writing to file") 
    for i in range(10):
        myfile.write("This is string \n")
    
    myfile.close()
    #read the file, after writing the file the file pointer moves to end and it would not display 
    #any output when we read it. so move the pointer to 0 again using seek function
    #myfile.seek(0)
    print ("reading the file")
    myfile = open("strtext.txt",'r+')
    print (myfile.read())
    #close the file at the end
    myfile.close()
    
    
#use readlines function to read contents of the file    
def readfile():
    print ("this is inside readfile function")
    filetoread = open("strtext.txt", 'r+')
    readlns = filetoread.readlines()
    for i in readlns:
        print (i)
    filetoread.close()
    
filess()
readfile()