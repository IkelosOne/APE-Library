import re
import StandardFunctions
import Formatting
import math


def calculateFromString(equationString):
    """Uses recursion to break down an equation to its smallest calculations (V2)
    :rtype float
    """

    numberList = []
    operatorList = []
    x = 0
    while x < len(equationString):
        try:
            if equationString[x] == equationString[x + 1]:  # Gets rid of double + and double - when encountered
                if equationString[x] == "+" or equationString[x] == "-":
                    equationString = equationString[0:x] + "+" + equationString[x + 2:]
        except IndexError:
            pass

        if equationString[x] == "(":  # Deals with pesky brackets
            for i in range(x, len(equationString)):
                if equationString[i] == ")":
                    numberList.append(calculateFromString(
                        equationString[x + 1:i]))  # Will send whats inside the bracket to get processed
                    break
            x = i  # Stops doing everything else in the bracket as it will be done in the reccursion
        elif equationString[x] == "+" or equationString[x] == "-" or equationString[x] == "*" or equationString[
            x] == "/" or equationString[x] == "^":  # Deals with pesky operators (minus is the worst)
            if (equationString[x] == "-" and x == 0) or (equationString[x] == "-" and (
                    equationString[x - 1] == "+" or equationString[x - 1] == "*" or equationString[x - 1] == "/" or
                    equationString[x - 1] == "^")):  # Handles negative numbers
                for i in range(x + 1, len(equationString)):
                    if (Formatting.isType(equationString[i], "int") == False and equationString[i] != ".") or (
                            i + 1 == len(equationString)):  # Keeps going until the number ends and there is an operator or until it gets to the end
                        try:
                            numberList.append(float(equationString[x:i]))
                            x = i - 1
                        except ValueError:
                            numberList.append(float(equationString[x]))
                        break
            else:
                operatorList.append(equationString[x])
        elif Formatting.isType(equationString[x], "int"):  # Yay, actual, easy-to-understand, numbers!
            for i in range(x, len(equationString) + 1):
                if i > len(equationString) - 1:  # Checks if this is the last digit in equationString
                    numberList.append(float(equationString[x:i]))
                    x = i - 1
                    break
                elif Formatting.isType(equationString[i], "int") == False and equationString[
                    i] != ".":  # Keeps going until the number ends and there is an operator
                    try:
                        numberList.append(float(equationString[x:i]))
                        x = i - 1
                    except ValueError:
                        numberList.append(float(equationString[x]))
                    break

        x += 1  # Doesn't use for loop because some segments get skipped over in one loop cycle so x increment is not consistent

    answer = numberList[0]  # Final compiler
    for n in range(len(
            operatorList)):  # Performs operations to all the numbers in chromatic order (BIDMAS rules don't apply yet)
        if operatorList[n] == "+":
            answer += numberList[n + 1]
        elif operatorList[n] == "-":
            answer -= numberList[n + 1]
        elif operatorList[n] == "*":
            answer *= numberList[n + 1]
        elif operatorList[n] == "/":
            answer /= numberList[n + 1]
        elif operatorList[n] == "^":
            try:
                # answer = answer**(numberList[n+1])
                answer = math.pow(answer, numberList[n + 1])  # This can throw errors and not do stupid complex numbers
            except ValueError:
                answer = -((-answer) ** (
                    numberList[n + 1]))  # Cheating? Makes it not negative, then makes it negative afterwards
    return answer


def toDecimal(number, base):
    """This function is so incredibly based
    :rtype int
    """
    number = str(number)
    digits = len(number)
    decimal = 0
    for x in range(digits):
        digit = number[x]
        if Formatting.isType(digit, "string"):
            digit = ord(digit.upper()) - 65 + 10  # Allows use of letters to represent numbers above 9
        if x == digits - 1:  # 0^0 = 1 according to python so had to manually fix this
            decimal += int(digit)
        else:
            decimal += (int(digit) * base) ** (digits - x - 1)
    return decimal


def decimalToBinary(decimal, negMode="ignore"):
    """Takes any positive decimal integer and returns the binary number. Sign magnitude can be used for negative
    :rtype: int
    """

    negative = False
    if str(decimal)[0] == "-":  # Removes negative sign to do initial conversion to binary
        negative = True
        decimal = str(decimal)[1:]

    decimal = int(decimal)
    binary = ""

    remaing = decimal

    if decimal == 0:
        return 0
    elif decimal == 1:
        if negMode == "ignore":
            return 1
        elif negMode == "signMagnitude":
            if negative:
                return "11"
            else:
                return "01"
        elif negMode == "twoCompliment":
            if negative:
                return compliment(1, 2)
            else:
                return "01"
    binDigits = int(simpleRound(math.log2(decimal) + 0.5))  # Rounds up to find the numebr of digits
    for x in range(binDigits):
        i = binDigits - x - 1
        if 2 ** (i) <= remaing:
            binary += "1"
            remaing -= 2 ** i
        else:
            binary += "0"

    if negMode == "ignore":
        return int(binary)
    elif negMode == "signMagnitude":
        if negative:
            return int("1" + str(binary))
        else:
            return int("0" + str(binary))
    elif negMode == "two'sCompliment":
        if negative:
            return compliment(binary, 2)
        else:
            return int("0" + str(binary))


def equaliseNumLengths(number1, number2):
    """Makes both numbers the same length by putting "0"'s before the number. Numbers returned in array as strings so formatting is kept
    :rtype list[str]
    """

    number1 = str(number1)
    number2 = str(number2)
    if len(number1) < len(number2):  # Makes number2 shorter
        temp = number1
        number1 = number2
        number2 = temp

    lenDiff = len(number1) - len(number2)

    for l in range(lenDiff):  # Makes both numbers the same length
        number2 = "0" + number2
    return [number1, number2]


def addBasedNumbers(number1, number2, base, overflow=True):
    """Well you see, you have one number and this other number and you add them but the base might not be base 10 because I'm probably using it for binary so you can't use normal rules. No. You have to make sure you carry digits over after base amounts. Well actually I guess the limit is base-1 as base ten only actually goes up to 9 because you include the zero as one of the ten digits in base ten you see. So yeah, you can do that with other bases now with this you see? You see? Yeah.
    :rtype int
    """

    # Makes both numbers the same length
    eqNumbers = equaliseNumLengths(number1, number2)
    number1 = eqNumbers[0]
    number2 = eqNumbers[1]

    # Makes both numbers in to strings
    number1 = str(number1)
    number2 = str(number2)

    if int(number1) < int(number2):  # Makes sure the overflow is limited to the same as the largest numebr
        temp = number1
        number1 = number2
        number2 = temp

    length = len(str(number1))
    answer = []

    for i in range(length):
        answer.append("0")

    for x in range(length):  # Uses reccursion to sort out carried digits
        digit = int(str(number1)[length - x - 1]) + int(str(number2)[length - x - 1])
        digit = digit + int(answer[length - x - 1])
        if digit > base - 1:
            digit -= base
            addition = "1"
            for z in range(x + 1):
                addition += "0"
            answer = list(Formatting.arrayToString(addBasedNumbers(Formatting.arrayToString(answer), addition, 2)))

        else:
            # answer = str(answer)[:-x-1] + str(digit) + str(answer)[-x-0:]
            answer[length - x - 1] = str(digit)
    if len(answer) > length and overflow == False:
        answer = answer[1:]  # Assumes only one digit must be removed as this is what is expected
    return answer


def compliment(number, base):
    """Performs base's compliment. If base is 2 it will return 2's compliment
    :rtype int
    """

    number = str(number)
    lesserCompliment = ""
    for x in range(len(number)):
        lesserCompliment += str(base - int(number[x]))
    lesserCompliment = int(lesserCompliment)

    return lesserCompliment + 1


def simpleRound(number, unit=1):
    """Rounds in a simple manner, returning a float. Not bankers round
    :rtype: float
    """

    number += unit / 2
    if (number % unit) - number >= unit / 2:
        return (number // unit) * unit + unit
    else:
        return (number // unit) * unit


if __name__ == "__main__":
    """Use the space below for testing. Any code here will not run when the file is imported as a module. Delete it once you're finished testing."""

    # print(calculateFromString("2+(3-(5*4))"))
    # print(4,": "+str(decimalToBinary(4,negMode = "ignore")))

    """
    for x in range(20):
        print(-x+1,": "+str(decimalToBinary(-x+1,negMode = "signMagnitude")))
    """

    print(decimalToBinary(20))

    None
