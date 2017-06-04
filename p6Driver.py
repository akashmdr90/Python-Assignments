import re
from p6At import setVariable, setFormat, replaceVars, printText
###############################################################
"""
Pablo Valero - dwl306
Program 6
	Purpose:

	Notes:
		This implementation opens the file specified in the code, and does not take in
		command line parameters
"""
################################################################
"""
DRIVER
	Purpose:
"""
################################################################
#Declare dictionaries
varDictionary = {}
formatDictionary = {"LM":"1", "RM":"80", "FLOW":"YES", "JUST":"LEFT", "BULLET":"o"}
flag = 1
paragraph =''
with open('p6Input.txt') as f:
		#Read in and operate on each line
		for line in f:
			#If we have VAR command
			if "@. VAR" in line:
				#Leave everything after command
				values = line[8:]
				#Call function to populate dictionary
				setVariable(values, varDictionary)
			#If format comand
			elif "@. FORMAT" in line:
				#keep everything after command
				values = line[10:]
				#Call function to populate array
				setFormat(values, formatDictionary)

			# Handle text lines
			else:
				buffer = line
				# If its a new line, the next one is start of new paragraph
				# This is decremented after each line so it is only 0 for first
				# line of paragraph
				if buffer == "\n":
					flag = 1
				else:
					flag = flag - 1
				# Call routines to format
				replaceVars(buffer, formatDictionary, varDictionary,flag)
				# If a new line is hit we will print the current global string
				if buffer == "\n":
					printText(formatDictionary)

				# replaceVars(buffer, formatDictionary, varDictionary)
