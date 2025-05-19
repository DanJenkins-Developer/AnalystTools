from pathlib import Path

def collectInfo():

        input("Ensure you have copied the column and pasted it into file called \"input.txt\" that is in the same directory as this program and then press any key ")

        
        input_path = Path(__file__).parent / "input.txt"

        file = open(input_path)
        file_lines = file.read().splitlines()
        file.close()

        return file_lines

def processColumn(columnData):

        print(columnData[0] + "\n")

        for item in columnData[1:]:
                print(item)

        print("\n")

        for item in columnData[1:]:
                print(item.replace("\"", ""))

        print("\n" + "unique items:")

        query = ""
        res = list(dict.fromkeys(columnData[1:]))
        for item in res:
                
                print(item)

        for index, item in enumerate(res):
                if (index != len(res) - 1):
                        query = query + f"{item} or "
                else:
                        query = query + f"{item}"

        fieldName = columnData[0].replace("\"", "")
        query = f"{fieldName}: ({query})"

        print("\n" + query)
                
        return


data = collectInfo()

processColumn(data)
        