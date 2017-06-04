import re
currentline = ""
currentCount = 0
# flag = -1
################################################################
"""
				*** setVariable(atString, varDictionary) ***
		Purpose:
			Sets the variables in the dictionary for their respective keys
		Parameters:
			atString - This is a filtered line that we extract key and variable form
			varDictionary - This is the dictionary that we are going to populate

"""
################################################################
def setVariable(atString, varDictionary):
	#These are our regex rules to parse the values and keys
	keyRE = re.compile(r'([\w^]*)(?==)')
	# varRE = re.compile(r'(=)("|)([\w^]*)( )*([\w^]*)(.)')
	varRE = re.compile(r'(=)("|)([\w^]*)( )*([\w^]*)(.)*')
	#Extract variables
	matchVar = varRE.search(atString)
	matchKey = keyRE.search(atString)
	matchVar = matchVar.group()[1:]
	# print(matchVar)
	#Get rid of possible quotes
	matchVar = matchVar.replace('\"','')
	matchKey = matchKey.group()
	#Populate dictionary
	#Set value for key
	varDictionary[matchKey]=matchVar

    ################################################################
"""
				*** setFormat(atString, formatDictionary) ***
		Purpose:
			Sets the variables in the dictionary for their respective keys
		Parameters:
			atString - This is a filtered line that we extract key and variable form
			varDictionary - This is the dictionary that we are going to populate

"""
################################################################
def setFormat(atString, formatDictionary):

	#Only possible keys
	keyList = ["LM", "RM", "JUST", "BULLET", "FLOW"]
	#Only possible values for JUST
	posJust = ["LEFT", "RIGHT", "BULLET", "CENTER"]
	#Rules for our regex extractions
	keyRE = re.compile(r'([\w^]*)(?==)')
	varRE = re.compile(r'(=)([\w^]*)( )*([\w^]*)(.)')

	# Split at spaces
	varSplit = atString.split()
	#Go thorugh each assignment
	for temp in varSplit:
		#Extract wanted values
		matchVar = varRE.search(temp)
		matchKey = keyRE.search(temp)
		matchVar = matchVar.group()[1:]
		matchKey = matchKey.group()

		#Check the keys
		if not matchKey in keyList:
			print("*** Invalid format, found: " + matchKey + "=" + matchVar)
			continue

		#Check value if key is JUST
		elif matchKey == "JUST":
			#Check for correct value
			if not matchVar in posJust:
				print("*** Bad value for JUST=, found: " + matchVar)
				continue
		#place into formatdict
		formatDictionary[matchKey] = matchVar


############################
### **** replaceVars
def replaceVars(buffer, formatDictionary, varDictionary,flag):
	newline = ""

	# print(buffer)
	lineUnFormatted = buffer.split(" ")
	length = len(lineUnFormatted)

	lineUnFormatted[-1] = lineUnFormatted[-1].strip()
	# print(lineUnFormatted)
	count = 0
	while count < length:
		#Check if line has a variable to replace
		if "@" in lineUnFormatted[count]:
			# print(lineUnFormatted[count])
			#Current word from line
			value = lineUnFormatted[count]
			end = ""
			#If the value ends with period or comma we remove the last char and
			#save it so we can append it after we have replaced it.
			if value[-1]=="," or value[-1]=="." :
				end = value[-1:]
				value = value[:-1]
			lineUnFormatted[count] = varDictionary[value[1:]]
			lineUnFormatted[count]+=str(end)
		# print(lineUnFormatted[count])
		newline += str(lineUnFormatted[count])
		newline += str(" ")
		count = count + 1

	newline = newline.rstrip()
	# No flow,just print line as is with just
	if formatDictionary['FLOW'] == "NO":
		formatWidth = int(formatDictionary["RM"]) - int(formatDictionary["LM"])+1
		printText(formatDictionary)
		# if newline != "\n" or newline != "" or newline != " ":
		print(''.rjust(int(formatDictionary["LM"]))+newline)

	if formatDictionary['FLOW'] == "YES":
		wrapText(newline, formatDictionary,flag)

# Keep adding text to global current line until we hit an empty line.
# Add \n when word doesnt fit anymore.

def wrapText(line, formatDictionary,flag):
	temp = line
	temp = temp.split(" ")
	# print(temp)
	global currentline

	formatWidth = int(formatDictionary["RM"]) - int(formatDictionary["LM"]) +  1
	# print(int(formatDictionary["RM"]))
	# print(int(formatDictionary["LM"]))
	if formatDictionary['JUST'] == "BULLET":
		formatWidth = int(formatDictionary["RM"]) - int(formatDictionary["LM"]) - 1
	count = 0
	width = 54
	# print(temp)
	# print(formatWidth)
	# print(width)
	for word in temp:

		currentWith = (len(currentline) % formatWidth)
		if currentWith + len(word) + 1 < formatWidth:
			currentline += word + " "
		elif currentWith+ len(word) + 1 > formatWidth:
			currentline += "\n"+word+" "
		elif currentWith + len(word)  == formatWidth:
			currentline += word+"\n"
		else:
			currentline += "\n"+word+" "
		# if count == len(temp):
		# 	print("hi")


def printText(formatDict):
	global currentline
	global flag
	if currentline == "\n":
		return None
	if currentline != "":
		# print("         1         2         3         4         5         6         7")
		# print("12345678901234567890123456789012345678901234567890123456789012345678901234567")
		lines = currentline.splitlines()
		counts = 0
		for line in lines:
			if formatDict['JUST'] == "BULLET":
				if counts == 0:
					line = ''.join(('o ',line))
					counts += 1
				else:
					line = ''.join(('  ',line))

			print(''.rjust(int(formatDict["LM"]))+line)
	currentline = ""
