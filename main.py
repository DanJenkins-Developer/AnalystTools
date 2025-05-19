on = True

def collectHostInfo():
        
        hostname = (input("Enter host.name :: "))
        return hostname

def collectProcessInfo():
        
        processName = (input("Enter process name :: "))
        processPid = (input("Enter process PID :: "))
        process = {'process.name':processName, 'process.pid':processPid}
        return process

def formatQueryFromProcess(process):
    
    query = f"(process.name: {process['process.name']} and process.pid: {process['process.pid']})"
    return query


def buildProcessLineage(processQueries, hostname):

    lineage = ""

    for index, query in enumerate(processQueries):
        if (index != len(processQueries) - 1):
            lineage = lineage + f"{query} or "
        else:
            lineage = lineage + f"{query}"

    
    if (hostname !=  ''):
         lineage = f"{hostname} and ({lineage})"

    return lineage



queryList = []
host = collectHostInfo()


while True:
    process = collectProcessInfo()
    queryList.append(formatQueryFromProcess(process))
    processLineage = buildProcessLineage(queryList, host)

    print(f"Current process lineage :: {processLineage}")

    userChoise = input("Add another process? Y/N :: ")  
    if userChoise.lower() != 'y':
         break

    
print(f"Final process lineage :: {processLineage}")