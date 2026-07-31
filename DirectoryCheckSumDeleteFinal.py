###############################################################
# 
# Importing Required Libraries
# 
###############################################################

import sys
import os
import hashlib
import schedule
import time

############################################################### 
# function name : CalculateCheckSum
# Input : Name of File
# Description : Calculate Checksum of each file
# Date : 25/07/2026
# Author : Ankita Anant Somwanshi
############################################################## 

def CalculateCheckSum(FileName):
    fobj = open(FileName,"rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while(len(Buffer)>0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()
    
    return hobj.hexdigest()

############################################################### 
# function name : FindDuplicate
# Input : Name of Directory
# Description : Finds Duplicate files present in the directory
# Date : 25/07/2026
# Author : Ankita Anant Somwanshi
##############################################################

def FindDuplicate(DirectoryName):
    Ret = False

    Ret = os.path.exists(DirectoryName)

    if Ret == False:
        print("Path is Invalid")
        return
    
    Ret = os.path.isdir(DirectoryName)

    if Ret == False:
        print("It is not a Directory")
        return

    Duplicate = {}

    for FolderName, SubFolder,FileName in os.walk(DirectoryName):
        for fname in FileName:
            fname = os.path.join(FolderName,fname)
            CheckSum = CalculateCheckSum(fname)

            if CheckSum in Duplicate:
               
                Duplicate[CheckSum].append(fname)
            else:
               
                Duplicate[CheckSum] =[fname]

    return Duplicate

############################################################### 
# function name : DeleteDuplicate
# Input : Name of Directory
# Description : Delete Duplicate Files found in the directory
# Date : 25/07/2026
# Author : Ankita Anant Somwanshi
##############################################################

def DeleteDuplicate(DirectoryName):

    Border = "-"*40
    
    timestamp = time.ctime()
    
    LogFileName = "Test%s.log"%(timestamp)
    
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")
    
    Ret = False
    
    Ret = os.path.exists(DirectoryName)
    
    if (Ret == False):
            print("Marvellous Automation Error : There is no such directory with name ",DirectoryName)
            return
        
    Ret = os.path.isdir(DirectoryName)
    
    if(Ret == False):
            print("Marvellous Automation Error : It is not a directory with name ",DirectoryName)
            return 
    
    print("Log file gets created with name : ",LogFileName)
    
    fobj = open(LogFileName,"w")
    
    fobj.write(Border+"\n")
    
    fobj.write("Marvellous Automation Script \n")
    
    fobj.write(Border+"\n\n")

    fobj.write("Files from the directory are : \n\n")

    start_time = time.ctime()
    
    MyDict = FindDuplicate(DirectoryName)

    Result = list(filter(lambda x : len(x)>1, MyDict.values()))

    count = 0
    TotalDeletedFiles = 0

    TotalFiles = sum(len(files) for files in MyDict.values())

    for value in Result:   
        for subvalue in value:

            count = count + 1
            if(count>1):
                os.remove(subvalue)
                TotalDeletedFiles = TotalDeletedFiles+1
        count = 0

    DuplicateFiles = sum(len(files)-1 for files in Result)

    AbsolutePath = os.path.abspath(DirectoryName)

    end_time = time.ctime()

    fobj.write(Border+"\n")
    
    fobj.write(f"Total files scanned : {TotalFiles}\n")
    fobj.write(f"Total Duplicate files found : {DuplicateFiles}\n")
    fobj.write(f"Total Duplicate files deleted : {TotalDeletedFiles}\n")
    fobj.write(f"Directory Scanned : {AbsolutePath}\n")
    fobj.write(f"Starting time of Scanning : {start_time}\n")
    fobj.write(f"Completion time of Scanning :{end_time}\n")
       
    fobj.write(Border+"\n")
    
    fobj.write("Log file gets created at : "+timestamp)
    
    fobj.write("\n"+Border+"\n")
    
    fobj.close()

###############################################################
# function name : Main
# Input : Command line arguments
# Description : It controls the script
# Date : 25/07/2026
# Author : Ankita Anant Somwanshi
###############################################################

def main():

        #DeleteDuplicate("Test")

        Border = "-"*40
        
        print(Border)
        print(" Marvellous Automation Script ")
        print(Border)
       
        if(len(sys.argv) == 2):
        
                if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
                    print("This automation script is used to travel the directory")
                    print("For better usage please check --u flag")
                elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
                    print("Please execute the script as ")
                    print("Python FileName.py DirectoryName")
                    print("DirectoryName should be absolute path")
                else:
        
                    schedule.every(1).minute.do(DeleteDuplicate,sys.argv[1])
        
                    #DeleteDuplicate(sys.argv[1])
        
                    while True:
                        schedule.run_pending()
                        time.sleep(1)
        
        else:
                print("Invalid number of arguments")
                print("Please use --h or --u  for more information")
     
        print(Border)
        print(" Thank you for using Marvellous Automation Script ")
        print(Border)

############################################################### 
# 
# Starter of  the Automation Script
# 
###############################################################  
        
if __name__ == "__main__":
    main()