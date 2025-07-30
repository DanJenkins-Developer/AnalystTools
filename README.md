<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- PROJECT LOGO -->
<br />


<h3 align="center">Matthew's Cyber Paste</h3>

  <p align="center">
    A set of hotkeys I've made to make formatting easier and to help with investiagations.
  </p>
</div>

## Installation

1. Download the Files from GitHub
2. Download and Install [Python](https://www.python.org/downloads/)
3. In a terminal Install [pyperclip](https://pypi.org/project/pyperclip/), and [pynput](https://pypi.org/project/pynput/). <br>
  ```pip install pyperclip pynput ``` <br>
  I believe that `requirments.txt` should cover this step.
4. In the terminal, navigate to the location of Cyber_Paste.py <br>
  `cd <path>` 
5. In the terminal start the program (You should see a list of the available hotkeys)<br>
  ```python Cyber_Paste.py```
6. Press `ctrl+alt+shift+esc` to exit 



<!-- USAGE EXAMPLES -->

## Notes on Formatting
Anytime \s(space) \t(tab) or \n(newline) is seen, this is to show the formatting kibana has for the respective object, if you just copy and pasted it, and does not need to be added to get the hotkeys to function properly.

Arrows( → , &#8627; ) indicate what that line is transformed into after the hotkey. Arrows( → , &#8627; ) without anything to their left indicates that this hotkey inserts the stuff on the right of the Arrow( → , &#8627; ) in its formatting process. 

Curly Braces( { } ) indicate text that is not in the formating but that helps with clarity.

## Usage
All hotkeys used after copying their respective information to your clipboard, the hotkey will then put the formatted version of the information back into your clipboard, ready for you to paste it into your case or discover.

### `Hotkey Combination`: Hotkey Name

### `ctrl+alt+v`: Format
- This hotkey takes alert fields and capitalizes and adds spaces to the field name and puts the feild content in backticks. It will apply the formating to as many lines as you have copied from the alert tab. <br>
&ensp;   eg. <br>
&ensp; &ensp; <span style="color: red">this.example.field \t field content</span> → <span style="color: green">This Example Field \`field content\`</span>
- Adds Group \`\` on a new line under the User field as well as adding a black line to seperate Host, User, and Group from the rest of the info that is copied at that time. <br>
&ensp; eg. <br>
&ensp; &ensp; <span style="color: red">host.name \t exampleHost</span> → <span style="color: green">Host \`exampleHost\`</span> <br>
&ensp; &ensp; <span style="color: red">user.name \t exampleUser</span> → <span style="color: green">User \`exampleUser\`</span> <br>
&ensp; &ensp; → <span style="color: green">Group ``</span><br>
&ensp; &ensp; → <span style="color: green">{empty line}</span><br>
&ensp; &ensp; <span style="color: red">process.executable \t exampleProcess.exe</span> → <span style="color: green">Process Executable \`exampleProcess.exe\`</span>
- Removes extrenous parts of field names: Events, events, text, pe, name, or process if the next word is parent or command
- Removes uninteresting fields from the overview tab: agent.status, or Endpoint.policy.applied.artifacts.global.channel

### `ctrl+alt+shift+v`: Observation Statement Format 
- This hotkey takes the host, user, group and the last line copied and converts it into my standard Observation Statement format <br>
&ensp; eg. <br>
&ensp; &ensp; <span style="color: red">Host \`exampleHost\`</span> <br>
&ensp; &ensp; <span style="color: red">User \`exampleUser\`</span> <br>
&ensp; &ensp; <span style="color: red">Group \`exampleGroup\`</span> <br>
&ensp; &ensp; <span style="color: red">{any number of inrelevant lines, your choice based off what you copy}</span> <br>
&ensp; &ensp; <span style="color: red">Process Executable \`exampleProcess.exe\`</span> <br>
&ensp; &ensp; <span style="color: red">File Path \`exampleFile.path\`</span> <br>
&ensp; &ensp; &#8627; <span style="color: green">File Path \`exampleFile.path\` flagged for {you would insert the alert name here} on Host \`exampleHost\` under User \`exampleUser\` at Group \`exampleGroup\`.</span>

### `ctrl+win+shift+v`: Duplicate Format (MacOS Cmd Key)
- This hotkey takes the url for a hive case and optionally the case number and formates into a duplicate hive case link.
- To add the case number, copy it to your clipboard and then use the `Extra Text` hotkey to store it. Then copy the url and use this hotkey.
- <span style="color: red">hiveCase.URL</span> → <span style="color: green">Duplicate of \[Hive Case #{value stored with the Extra Text Hotkey}\](hiveCase.URL)</span>

### `ctrl+alt+shift+a`: Extra Text Format
- This hotkey stores your clipboard for another hotkey to use later.

### `ctrl+alt+1`: Extra Text 1 Format
- This hotkey is to store additional info, currently only used to store the User Job Title in the `Person Info` hotkey.

### `ctrl+alt+2`: Extra Text 2 Format
- This hotkey is to store additional info, currently only used to store the User Department in the `Person Info` hotkey.

### `ctrl+alt+c`: Column Format
- This hotkey takes a column from discover and puts each entry in backticks( \` ). This version cuts off the first and last charcter of each entry since copying a column from discover has quotes( " ) around the values.
- Will also put anything stored with the Extra Text hotkey at the start of the column. 


### `ctrl+win+c`: Column Format - Non Destructive (MacOS Cmd Key)
- This hotkey is the same as Column Format but doesnt remove the first and last character of each entry.

### `ctrl+alt+d`: Discover Link Format
- This hotkey takes the link to discover and makes the hyperlink format.
- <span style="color: red">discovertab.URL</span> → <span style="color: green">This \[Discover tab\](discovertab.URL) shows</span>

### ``ctrl+` ``: Quote Format
- This hotkey puts what ever you have copied into backticks( \` ).<br>
&ensp; eg. <br>
&ensp; &ensp; <span style="color: red"> exampleText</span> → <span style="color: green">\`exampleText\`</span>

### `ctrl+alt+p`: Person Info Format
- This hotkey takes the hyperlink to people finder and adds text to have the users title and department listed easily.
- Optionally will put the user name, title, and department into the formated text. <br>
&ensp; eg. <br>
&ensp; &ensp; <span style="color: red">people\finder.URL</span> → <span style="color: green">\[{Extra Text}\](people\finder.URL) is a \`{Extra Text 1}\` in the \`{Extra Text 2}\` department.</span>

### `ctrl+alt+h`: Hive Search Format
- This hotkey puts the copied text into a format to search in hive.
- ie. put astricks( * ) around each word and replacing special characters( - \s \\ _ ) with astricks( * ) as well.

### `ctrl+alt+q`: Add Parent Format 
- This hotkey puts .parent inbetween process and name or pid for discover queries. <br>
&ensp; eg. <br>
&ensp; &ensp; <span style="color: red">(process.name: example.exe and process.pid: 1234)</span> → <span style="color: green">(process.parent.name: example.exe and process.parent.pid: 1234)</span>

### `ctrl+alt+r`: Remove ' - ' From Column Format
- This hotkey removes any blank lines when copying a coulmn from discover. This will also put backticks( \` ) around each row.

### `ctrl+alt+shift+w`: Source-Destination IP Format
- This hotkey takes the ip info from the timeline view and formats it nicely. <br>
&ensp; eg. <br>
&ensp; &ensp; <span style="color: red">source 123.456.7.890 : 1234, destination 098.765.4.321 : 4321</span> → <span style="color: green">Source \`123.456.7\[.\]890\` : \`1234\` \n Destination \`098.765.4\[.\]321\` : \`4321\`</span>

### `ctrl+alt+z`: Two Column Format
- This hotkey puts two columns next to each other with a vertical line( | ) between the two columns.
- The coulmn that you want on the left should be stored by fromatting into column format and then use the `Extra Text 1` Hotkey. Then copy your new column and use this hotkey and it will format your right hand column and put the two columns next to each other.

### `ctrl+alt+u`: Unique Columns Format
- This hotkey will remove duplicate entries in the column format. This will also put backticks( \` ) around each row.

### `ctrl+alt+b`: Discover Row with Backticking
- This hotkey puts backticks( \` ) around each field when copying from a row in discover. <br>
&ensp; eg. <br>
&ensp; &ensp; <span style="color: red"> Timestamp @ 10 \t exampleField1 \t example field 2</span> → <span style="color: green">\`Timestamp @ 10\` \`exampleField1\` \`example field 2\`</span>
- Also works with any tab deliniated line.

### `ctrl+alt+shift+t`: Timeline Process and Command Format
- This hotkey takes a copied line from the timeline view and puts the process in backticks( \` ) and puts the command on a new line. By combining the process args together and puts the command in backticks( \` ) as well. <br>
&ensp; eg.
&ensp;&ensp; <span style="color: red">process.exe \n (process.pid field) \n processArg1 \n porcessArg2 \n ect.</span> <br>
&ensp;&ensp; &#8627; <span style="color: green">{Type if this is the Process or the Parent from the timeline view}\`process.exe\`<br>
&ensp;&ensp; &#8627; <span style="color: green">Command \`processArg1 processArg2 ect.\`</span>
- This is used on the line within the timeline view that has <br>
`user.name` \\ `user.domain` @ `host.name` in `process.working_directory` started process `process.name` `process.pid` `process.args` with exit code `process.exit_code` via parent process `process.parent.name` `process.parent.pid` with result `event.outcome`

### `ctrl+alt+shift+p`: Phishing Email Observationg Statement Format
- This hotkey takes the Email To Address, Email From Address Email Subject, and Email Reporter fields to write an observation statement. <br>
&ensp; eg. <br>
&ensp; &ensp; <span style="color: red">Email To Address \`example@address.ex1\`</span> <br>
&ensp; &ensp; <span style="color: red">Email From Address \`example@address.ex2\`</span> <br>
&ensp; &ensp; <span style="color: red">Email Subject \`exampleSubject\`</span> <br>
&ensp; &ensp; <span style="color: red">{any number of inrelevant lines, your choice based off what you copy}</span> <br>
&ensp; &ensp; <span style="color: red">Email Reporter \`example@address.ex3\`</span> <br>
&ensp; &ensp; &#8627; <span style="color: green">Email with Subject \`exampleSubject\` from  \`example@address.ex2\` sent to \`example@address.ex1\` was flagged as a Phishing Email by \`example@address.ex3\`.</span>

<p align="right">(<a href="#readme-top">back to top</a>)</p>
