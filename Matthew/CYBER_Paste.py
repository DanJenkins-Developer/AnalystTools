import pyperclip
from pynput import keyboard
import re

def format_data(text):
    if text == "agent.status	Offline":
        # print("agent status removed")
        pass
    elif text == "agent.status	Healthy":
        # print("agent status removed")
        pass
    elif text == "agent.status	Unhealthy":
        # print("agent status removed")
        pass
    elif text == "agent.status	Updating":
        pass
    elif text == "Endpoint.policy.applied.artifacts.global.channel	stable":
        pass
    elif text == "Endpoint.policy.applied.artifacts.global.channel	candidate":
        pass
    elif text == "Endpoint.policy.applied.artifacts.global.channel	default":
        pass
    elif text == "Field\tValue":
        pass
    else: 
        words = text.split("\t")
        impoWrds1 = words[0].split(".")
        # print(impoWrds1)
        impoWrds = []
        for i in range(len(impoWrds1)):
            impoWrds += impoWrds1[i].split("_")
        # print(impoWrds)
        if impoWrds[0] == "rule":
            # print("Rule Removed")
            return
        frmtStr = ""
        if len(impoWrds) > 1:
            # print(impoWrds)
            if (impoWrds[1] == "parent" or impoWrds[1] == "command") and impoWrds[0] == "process":
                impoWrds.pop(0)
        for i in range(len(impoWrds)):
            if impoWrds[i] == "name":
                continue
            elif impoWrds[i] == "pe":
                continue
            elif impoWrds[i] == "text":
                continue
            elif impoWrds[i] == "Events" or impoWrds[i] == "events":
                continue
            frmtStr += impoWrds[i].capitalize() + " "
        # print(frmtStr)
        frmtStr += "`"
        for i in range(1,len(words)):
            frmtStr += words[i]
        frmtStr += "`"
        # print(frmtStr)
        if impoWrds[0] == "user":
            frmtStr += "\nGroup ``\n"
        return frmtStr

def formated_text():
    global shift
    global cmd
    if shift or cmd:
        return False

    # Get the text from the clipboard
    clipboard_text = pyperclip.paste()

    # Split the text into lines
    lines = clipboard_text.splitlines()

    # Format each line
    formatted_lines = [format_data(line) for line in lines]

    # Join the formatted lines back into a single string
    formatted_lines = list(filter(None, formatted_lines))
    formatted_text = "\n".join(formatted_lines)

    # Copy the formatted text to the clipboard
    pyperclip.copy(formatted_text)
    # print("Formatted text copied to clipboard!") 

def obs_statement():
    global cmd
    global shift
    if cmd:
        return False

    # Get the text from the clipboard
    clipboard_text = pyperclip.paste()

    # Split the text into lines
    lines = clipboard_text.splitlines()

    shift = False

    try:
        group = lines[2].split(" ")
        lines[2] = group[1]
        formatted_text = lines[len(lines)-1] + " flagged for on " + lines[0] + " under " + lines[1] + " at " + lines[2] + "."
        # Copy the formatted text to the clipboard
        pyperclip.copy(formatted_text)
        # print("Observation Statement Formatted text copied to clipboard!")
    except:
        print("Error Formatting Observation Statement")

def dupe_statement():
    global firstText
    
    # Get the text from the clipboard
    clipboard_text = pyperclip.paste()

    formatted_text = "Duplicate of [Hive Case #" + firstText + "](" + clipboard_text + ")"
    # Copy the formatted text to the clipboard
    firstText = ""
    pyperclip.copy(formatted_text)
    # print("Duplicate Statement Formatted text copied to clipboard!")

def format_data2(line):
    return '`' + line[1:-1] + '`'

def format_data3(line):
    return '`' + line[:] + '`'

firstText = ""

def column(version=1):
    global firstText
    # Get the text from the clipboard
    clipboard_text = pyperclip.paste()

    # Split the text into lines
    lines = clipboard_text.splitlines()
    lines.pop(0)

    # Format each line
    if version == 1:
        formatted_lines = [format_data2(line) for line in lines]
    elif version == 2:
        formatted_lines = [format_data3(line) for line in lines]

    # Join the formatted lines back into a single string
    formatted_lines.insert(0,firstText)
    formatted_lines = list(filter(None, formatted_lines))
    formatted_text = "\n".join(formatted_lines)
    
    firstText = ""
    # Copy the formatted text to the clipboard

    pyperclip.copy(formatted_text)
    # print("Formatted coulumn copied to clipboard!") 

def extra_text():
    global firstText
    firstText = pyperclip.paste().strip()

def discover_link():
    # Get the text from the clipboard
    clipboard_text = pyperclip.paste()

    formatted_text = "This [Discover tab](" + clipboard_text + ") shows"
   
    pyperclip.copy(formatted_text)
    # print("Formatted discover link copied to clipboard!") 

def quote():
    # Get the text from the clipboard
    clipboard_text = pyperclip.paste()

    formatted_text = "`" + clipboard_text.lstrip() + "`"
   
    pyperclip.copy(formatted_text)
    # print("Formatted Quote copied to clipboard!") 
    
extraText1 = ""
extraText2 = ""

def extra_text1():
    global extraText1
    extraText1 = pyperclip.paste().strip()

def extra_text2():
    global extraText2
    extraText2 = pyperclip.paste().strip()

def person_info():
    if shift:
        return False
    
    global firstText
    global extraText1
    global extraText2
    # Get the text from the clipboard
    clipboard_text = pyperclip.paste()

    formatted_text = "[" + firstText + "](" + clipboard_text + ") is a `" + extraText1 +  "` in the `" + extraText2 + "` department."
   
    pyperclip.copy(formatted_text)
    firstText = ""
    extraText1 = ""
    extraText2 = ""
    # print("Formatted Person Info copied to clipboard!") 
    
def hive_search():
    # Get the text from the clipboard
    clipboard_text = pyperclip.paste()

    words = re.split(r"[- \s \\ _]", clipboard_text)

    formatted_text = ""

    for i in range(len(words)):
        if words[i] == "":
            continue
        formatted_text = formatted_text + "*" + words[i] + "*" 
   
    pyperclip.copy(formatted_text)
    # print("Formatted Hive Search copied to clipboard!") 

def add_parent():
    # Get the text from the clipboard
    clipboard_text = pyperclip.paste()

    words = re.split("process.", clipboard_text)

    formatted_text = ""

    for i in range(len(words)-1):
        formatted_text += words[i] + "process.parent." 
    
    formatted_text += words[len(words)-1]
   
    pyperclip.copy(formatted_text)
    # print("Formatted Add Parent copied to clipboard!") 

def rem_empty_column():
    # Get the text from the clipboard
    column()

    clipboard_text = pyperclip.paste()

    lines = clipboard_text.splitlines()

    formatted_text = ""

    for i in range(len(lines)):
        if lines[i] == "` - `" or lines[i] == "`'-`" or lines[i] == '`" - "`':
            continue
        formatted_text += lines[i] + "\n"
   
    pyperclip.copy(formatted_text)
    # print("Removed '-' from list copied to clipboard!") 

def source_dest_IP():
    # Get the text from the clipboard
    clipboard_text = pyperclip.paste()

    lines = clipboard_text.strip().splitlines()

    for i in range(len(lines)):
        lines[i] = lines[i].strip().capitalize()
    
    formatted_text = lines[0]
    
    try:
        sIP = lines[1].rsplit('.',1)
        sIP = ' `' + sIP[0] + "[.]" + sIP[1] + '` '
        dIP = lines[6].rsplit('.',1)
        dIP = ' `' + dIP[0] + "[.]" + dIP[1] + '` '

        formatted_text += sIP + lines[2] + ' `' + lines[3] + '`\n' + lines[5] + dIP + lines[7] + ' `' + lines[8] + '`'
    
        pyperclip.copy(formatted_text)
        # print("Source-Destination Format copied to clipboard!") 
    except:
        print("Error Formatting Source-Destination")

def two_column():
    global extraText1
    column()
    clipboard_text = pyperclip.paste()
    lines = clipboard_text.splitlines()
    left = extraText1.splitlines()

    if len(lines) != len(left):
        print("Unequal Lengths")
        return

    output = ""
    for i in range(0,len(lines)):
        output += left[i] + " | " + lines[i] + "\n"

    extraText1 = "" 
    pyperclip.copy(output)
    # print("Two Column Format copied to clipboard!")

def unique():
    clipboard_text = pyperclip.paste()
    lines = clipboard_text.splitlines()

    column()

    unique_text = set(lines) 
    output = "\n".join(unique_text)
    
    pyperclip.copy(output)
    # print("Unique Values Copied to Clipboard!")

def discover_row_backticking():
    clipboard_text = pyperclip.paste()
    fields = clipboard_text.split("\t")
    formated_text = ""
    for i in range(0,len(fields)):
        formated_text += "`" + fields[i] + "` "

    pyperclip.copy(formated_text)
    # print("Discover Row with Backticks Copied to Clipboard!")

def timeline_proc_cmd():
    clipboard_text = pyperclip.paste()
    lines = clipboard_text.splitlines()

    formated_text = "`" + lines[0] + "`\nCommand `"

    for i in range(2, len(lines) - 1):
        formated_text += lines[i] + " "
    formated_text += lines[len(lines)-1] + "`"

    pyperclip.copy(formated_text)
    # print("Timeline Process and Command Format Copied to Clipboard!")

def phish_obs_statement():
    clipboard_text = pyperclip.paste()
    lines = clipboard_text.splitlines()

    formated_text = lines[2][:5].strip() + " with " + lines[2][5:].strip() + " from " + lines[1][18:].strip() + " sent to " + lines[0][16:].strip() + " was flagged as a Phishing Email by " + lines[-1][14:].strip() + "."

    pyperclip.copy(formated_text)

print("Ready to Format")
print("ctrl+alt+v: Format")
print("ctrl+alt+shift+v: Observation Statement Format")
print("ctrl+win+shift+v: Duplicate Format (MacOS Cmd Key)")
print("ctrl+alt+shift+a: Extra Text Format")
print("ctrl+alt+1: Extra Text 1 Format")
print("ctrl+alt+2: Extra Text 2 Format")
print("ctrl+alt+c: Column Format")
print("ctrl+win+c: Column Format - Non Destructive (MacOS Cmd Key)")
print("ctrl+alt+d: Discover Link Format")
print("ctrl+`: Quote Format")
print("ctrl+alt+p: Person Info Format")
print("ctrl+alt+h: Hive Search Format")
print("ctrl+alt+q: Add Parent Format") 
print("ctrl+alt+r: Remove ' - ' From Column Format")
print("ctrl+alt+shift+w: Source-Destination IP Format")
print("ctrl+alt+z: Two Column Format")
print("ctrl+alt+u: Unique Columns Format")
print("ctrl+alt+b: Discover Row with Backticks Format")
print("ctrl+alt+shift+t: Timeline Process and Command Format")
print("ctrl+alt+shift+p: Phishing Observation Statement Format")

def exit():
    listener.stop()

print("ctrl+alt+shift+esc: Exit CYBER Paste")

def on_press(key):  # The function that's called when a key is pressed
    global shift
    global cmd
    # print("Pressed " + format(key))
    if format(key) == "Key.shift":
        shift = True
    # if format(key) == "Key.cmd":
    #     cmd = True

def on_release(key):  # The function that's called when a key is pressed
    global shift
    global cmd
    # print("Pressed " + format(key))
    if format(key) == "Key.shift":
        shift = False
    # if format(key) == "Key.cmd":
    #     cmd = False

shift = False
cmd = False
listener2 = keyboard.Listener(
        on_press=lambda event:on_press(event),
        on_release=lambda event:on_release(event))
listener2.start()
    

with keyboard.GlobalHotKeys({
        '<ctrl>+<alt>+v': formated_text,
        '<ctrl>+<alt>+<shift>+v': obs_statement,
        '<ctrl>+<cmd>+<shift>+v': dupe_statement,
        '<ctrl>+<alt>+c': column,
        '<ctrl>+<cmd>+c': lambda: column(2),
        '<ctrl>+<alt>+<shift>+a': extra_text,
        '<ctrl>+<alt>+1': extra_text1,
        '<ctrl>+<alt>+2': extra_text2,
        '<ctrl>+<alt>+d': discover_link,
        '<ctrl>+`': quote,
        '<ctrl>+<alt>+p': person_info,
        '<ctrl>+<alt>+h': hive_search,
        '<ctrl>+<alt>+q': add_parent,
        '<ctrl>+<alt>+r': rem_empty_column,
        '<ctrl>+<shift>+<alt>+w': source_dest_IP,
        '<ctrl>+<alt>+z': two_column,
        '<ctrl>+<alt>+u': unique,
        '<ctrl>+<alt>+b': discover_row_backticking,
        '<ctrl>+<alt>+<shift>+t': timeline_proc_cmd,
        '<ctrl>+<alt>+<shift>+p': phish_obs_statement,
        '<ctrl>+<alt>+<shift>+<esc>': exit}) as listener:
    listener.join()

listener2.stop()
