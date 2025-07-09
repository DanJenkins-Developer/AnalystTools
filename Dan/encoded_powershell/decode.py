def loadPSCommandsFromFile():
    with open('normalized-command-lines.txt') as file:
        commands = file.read().splitlines()
        return commands
    
def getEncodedCommandArgumentPosition(command: str):

    position = 6 # change
    arguments = command.split(" ")
    for argument in arguments:
        print(argument)
    return position
    

def getEncodedCommand(command: str, position: int = 6):

    arguments = command.split(" ")
    encodedCommand = arguments[position]
    return encodedCommand


PSCommandsText = loadPSCommandsFromFile()
decodedCommands = []

for command in PSCommandsText:
    getEncodedCommand(command)
    decodedCommands.append(getEncodedCommand(command))




#test branch