from pathlib import Path

def collectInfo():

        input("Ensure you have copied the column and pasted it into file called \"input.txt\" that is in the same directory as this program and then press any key ")

        
        input_path = Path(__file__).parent / "input.txt"

        file = open(input_path)
        file_lines = file.read().splitlines()
        file.close()

        print(file_lines)

        print(f"The values belong to the {file_lines[0]} fild correct Y/N?")
        
        

        return 

def processColumn(columnData):
        return


collectInfo()
        