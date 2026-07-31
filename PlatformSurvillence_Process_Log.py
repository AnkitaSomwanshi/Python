import psutil  #Thirdparty dependencies
import sys
import os
import time
import schedule

def ProcessScan():
    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=["pid","name","username","status"])
        info["cpu_percent"] = proc.cpu_percent(None)
        info["memory_percent"] = proc.memory_percent()

        print("----------------------------------------------")
        print(info)
        print("----------------------------------------------")

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
        print("Directory for the log files gets created succesfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = os.path.join(FolderName,"Marvellous_%s.log" %timestamp)

    fobj = open(FileName,"w")

    print(f"Log file gets succesfully created with name {FileName}")

    fobj.write(Border+"\n")
    fobj.write("----Marvellous Platform Survillence System----\n")
    fobj.write("Log file gets created at : "+timestamp+"\n")
    fobj.write(Border+"\n\n")

    fobj.write("-----------------------System Report-------------------------\n")


    #CPU Information
    fobj.write("No of active CPU Cores : %s \n" %psutil.cpu_count())
    fobj.write("CPU Usage : %s %%\n" %psutil.cpu_percent())

    fobj.write(Border+"\n")

    #RAM Information
    memory = psutil.virtual_memory()
    fobj.write("RAM Usage : %s %%\n" %memory.percent)
    fobj.write("Total RAM available : %s \n" %memory.total)

    fobj.write(Border+"\n")

    #Network Usage
    netobj = psutil.net_io_counters()

    fobj.write("Newtwork Usage Report\n")
    fobj.write("Sent : %.2f MB\n" %(netobj.bytes_sent / (1024*1024)))
    fobj.write("Receive : %.2f MB\n" %(netobj.bytes_sent / (1024*1024)))

    fobj.write(Border+"\n")

    fobj.write("\n\n\n\n\n\n\n\n\n\n\n\n\n")

    fobj.write(Border+"\n")
    fobj.write("-----------------------End of Log File-----------------------\n")
    fobj.write(Border+"\n")

    fobj.close()

def main():
    ProcessScan()

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

        #PlatformSurvillence(sys.argv[2])
        #print("CPU Usage : ",psutil.cpu_percent())  #what is cpu-percent()

        print("Schedular Started Succesfully")
        print("Press Ctrl + C to abort the automation script")

        schedule.every(int(sys.argv[1])).minute.do(PlatformSurvillence,sys.argv[2])

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid No of Arguments")
        print("Unable to proceed as arguments are not matching")
        print("please use --h or --u flag for getting more details")

    print(Border)
    print("---Thank you for using our Automation System---")
    print(Border)

if __name__ == "__main__":
    main()