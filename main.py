on = True

def collectProcessInfo():
        processName = (input("Enter process name :: "))
        processPid = (input("Enter process PID :: "))
        process = {'process.name':processName, 'process.pid':processPid}
        return process

def formatProcessInfo(processes):
    
    processList = []
    
    for process in processes:
        processList.append(f"(process.name: {process['process.name']} and process.pid: {process['process.pid']})")

    return processList


def printProcessInfoPretty(processes):
    for process in processes:
        print(f"Process :: {process['process.name']}")
        print(f"Process PID :: {process['process.pid']}")


def buildProcessLineage(formatedProcesses):
    query = ""

    for index, process in enumerate(formatedProcesses):
        if (index <= len(formatedProcesses) - 2):
            query = query + f"{process} or "
        else:
            query = query + f"{process}"

    return query

while (on):
    
    processList = []

    while(True):

        process = collectProcessInfo()
        processList.append(process)

        userChoise = input("Add another process? Y/N :: ")    
        if(userChoise == 'Y' or userChoise == 'y'):
            continue
        else:
             break
        
    formattedProcessList = formatProcessInfo(processList)
    print(formattedProcessList)

    finalQuery = buildProcessLineage(formattedProcessList)
    print(finalQuery)


    on = False
    


