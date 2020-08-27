#-------------------------------------------------------------------------------
# Name:        Conversion
# Purpose:	   To have all APE Library funcions for converting from format to another

import sys
sys.path.append("S:\Documents\GitHub\APE-Library")
import APEFunctions

def IntToWord(integer):
	unitsDict = {0:"",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine"}
	tensDict = {10:"Ten",20:"Twenty",30:"Thirty",40:"Forty",50:"Fifty",60:"Sixty",70:"Seventy",80:"Eighty",90:"Ninety"}
	teensDict = {10:"Ten",11:"Eleven",12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Nineteen"}

	integer = str(integer)
	integer = int(integer)
	integer = str(integer)  # Gets rid of 0's at start of number
	word = ""
	# Starts from left side and appends on right
	if len(integer) > 12:
		if integer[12] != "0":
			word += IntToWord(integer[:-12]) + "Trillion"
	if len(integer) > 9:
		if integer[9] != "0":
			word += IntToWord(integer[-12:-9]) + "Billion"
	if len(integer) > 6:
		if integer[6] != "0":
			word += IntToWord(integer[-9:-6]) + "Million"
	if len(integer) > 3:
		if integer[3] != "0":
			word += IntToWord(integer[-6:-3]) + "Thousand"
	if len(integer) > 2:
		if integer[2] != "2":
			word += unitsDict[int(integer[-3:-2])] + "Hundred"
	if len(integer) > 1:
		if len(integer) > 2:  # Adds and inbetween hundreds and tens value
			if integer[-3:-2] != "0":
				word += "And"
		if integer[-2:-1] != "1":
			if integer[-2:-1] != "0":  # stops *00 being recognised as tens
				word += tensDict[int(integer[-2:-1])*10]
		else:  # Teens
			word += teensDict[int(integer[-2:])]
	if len(integer) > 0:
		if len(integer) == 1 and integer[0] == "0":
			return "Zero"
		else:
			word += unitsDict[int(integer[-1:])]

	return word

inp = input("")
print(APEFunctions.InsertCommas(inp))
print(IntToWord(inp))