import os
import shutil

def removing():
 print('mam i am not able to write the if-else condition for checking wheteher it is  a file or folder')
 print('please help')

 path = input("Enter the file name to be removed")
 

 if os.path.exists(path):
      os.walk(path)
      os.path.join()

 if (path  == '') :
     print("The path is not found")

 ctime = os.stat(path).st_ctime
 return ctime

removing()