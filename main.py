on = True

def collectProcessInfo():
        
        processName = (input("Enter process name :: "))
        processPid = (input("Enter process PID :: "))
        process = {'process.name':processName, 'process.pid':processPid}
        return process

def formatQueryFromProcess(process):
    
    query = f"(process.name: {process['process.name']} and process.pid: {process['process.pid']})"
    return query


def buildProcessLineage(processQueries):

    lineage = ""

    for index, query in enumerate(processQueries):
        if (index <= len(processQueries) - 2):
            lineage = lineage + f"{query} or "
        else:
            lineage = lineage + f"{query}"

    hostname = input("Enter a hostname to include in process lineage query or press enter to skip :: ")  

    if (hostname !=  ''):
         lineage = f"{hostname} and ({lineage})"

    return lineage

while (on):

    queryList = []

    while(True):

        process = collectProcessInfo()
        queryList.append(formatQueryFromProcess(process))

        userChoise = input("Add another process? Y/N :: ")    
        if(userChoise == 'Y' or userChoise == 'y'):
            continue
        else:
             break
        
    print(queryList)

    processLineage = buildProcessLineage(queryList)
    
    print(f"Final process lineage :: {processLineage}")

        

    on = False
    


