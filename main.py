on = True

def collectProcessInfo():
        
        processName = (input("Enter process name :: "))
        processPid = (input("Enter process PID :: "))

        process = {'process.name':processName, 'process.pid':processPid}

        return process

def formatProcessInfo(name, pid):
    
    query = f"(process.name: {name} and process.pid: {pid})"
    return query


def printProcessInfoPretty(processes):
    for process in processes:
        print(f"Process :: {process['process.name']}")
        print(f"Process PID :: {process['process.pid']}")


def buildProcessLineage(processQueries):

    lineage = ""

    for index, query in enumerate(processQueries):
        if (index <= len(processQueries) - 2):
            lineage = lineage + f"{query} or "
        else:
            lineage = lineage + f"{query}"

    return lineage

while (on):

    queryList = []

    while(True):

        process = collectProcessInfo()
        queryList.append(formatProcessInfo(process['process.name'], process['process.pid']))

        userChoise = input("Add another process? Y/N :: ")    
        if(userChoise == 'Y' or userChoise == 'y'):
            continue
        else:
             break
        
    print(queryList)

    processLineage = buildProcessLineage(queryList)
    print(processLineage)

        

    on = False
    


