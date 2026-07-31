import psutil  #Thirdparty dependencies
import sys
import os

def PlatformSurvillence(FolderName):

    Border = "-"*50

    Ret = False

    Ret = os.path.exists(FolderName)

    if(Ret == True):
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable to proceed as directory name is existing but its not a directory")
            return 
    else:
        os.mkdir(FolderName)
        print("Directory for the logfiles gets created succesfully")

def main():
    Border = "-"*50

    print(Border)
    print("----Marvellous Platform Survillence System----")
    print(Border)

    #--h & --u handling
    if (len(sys.argv)==2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):

            print("This Automation Script is used to perform")
            print("1: It fetch the information of running processes")
            print("2: It fetch information about the Primary storage as RAM")
            print("3: It fetch infromation about the Secondary storage as HDD")
            print("4: It fetch the information about the microprocessor")
            print("5: It gets auto schedule periodically")
            print("6: It maintains all records into log file")
            print("7: It sends the log files through mail periodically")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the Automation Script as :")
            print(f"python{sys.argv[0]} Time_Interval Folder_Name")
            print("Time_Interval : Time in minutes for periodic execution")
            print("Folder_Name : Name of folder for the log file creation")
        else:
             print("Unable to prceed as there is no matching ")
             print("please use --h or --u flag for getting more details")



    #Actual project code
    elif(len(sys.argv)==3):
        PlatformSurvillence(sys.argv[2])



    else:
        print("Invalid No of Arguments")
        print("Unable to proceed as arguments are not matching")
        print("please use --h or --u flag for getting more details")

    print(Border)
    print("---Thank you for using our Automation System---")
    print(Border)

if __name__ == "__main__":
    main()