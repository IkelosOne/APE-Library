import re

def calculateFromString(equationString):
		"""Takes an equation as a string containing only real numbers and basic operators. Brackets not yet supported"""
		#parts = equationString.split("(\+|-)") # Splits at + or - but keeps the operator a the beginning of each item
		parts = re.split("(\+|-)",equationString)
		firstOp = []
		secondOp = []
		for i in range(len(parts)):
			if parts[i] == "+" or parts[i] == "-":
				secondOp.append(parts[i])
			else:
				currentFirstOp = parts[i]
				if currentFirstOp.find("*")!=-1:
					currentFirstOp = currentFirstOp.split("*")
					if len(secondOp)>0 and secondOp[len(secondOp)-1] == "-":
						firstOp.append(-float(currentFirstOp[0])*float(currentFirstOp[1]))
						secondOp[len(secondOp)-1] = "+"
					else:
						firstOp.append(float(currentFirstOp[0])*float(currentFirstOp[1]))
				elif currentFirstOp.find("^")!=-1:
					currentFirstOp = currentFirstOp.split("^")
					if len(secondOp)>0 and secondOp[len(secondOp)-1] == "-":
						firstOp.append(float(currentFirstOp[0])**float(currentFirstOp[1]))
						secondOp[len(secondOp)-1] = "+"
					else:
						firstOp.append(float(currentFirstOp[0])**float(currentFirstOp[1]))
				elif currentFirstOp.find("/")!=-1:
					currentFirstOp = currentFirstOp.split("/")
					if len(secondOp)>0 and secondOp[len(secondOp)-1] == "-":
						firstOp.append(-float(currentFirstOp[0])/float(currentFirstOp[1]))
						secondOp[len(secondOp)-1] = "+"
					else:
						firstOp.append(float(currentFirstOp[0])/float(currentFirstOp[1]))
				else:
					#print("No primary operation found in "+currentFirstOp)
					try:
						firstOp.append(float(currentFirstOp))
					except ValueError:
						firstOp.append(0)

		answer = firstOp[0]
		for o in range(1,len(firstOp)):

			if secondOp[o-1] == "+":
				answer += firstOp[o]
			elif secondOp[o-1] == "-":
				answer -= firstOp[o]
			else:
				print("Can't understand this "+secondOp+" operator yet")

		#print(answer)
		return answer