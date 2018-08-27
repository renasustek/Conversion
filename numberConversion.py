
def startUpMenu():
    global conversionChoice1, conversionChoice2

    conversionChoice1 = input("Enter your conversion choice one\n>>")
    while conversionChoice1 != "hex" and conversionChoice1 != "denary" and conversionChoice1 != "binary":
        conversionChoice1 = input("Invalid option pick hex,denary or binary\n>>")

    conversionChoice2 = input("Enter your conversion choice two\n>>")
    while conversionChoice2 != "hex" and conversionChoice2 != "denary" and conversionChoice2 != "binary":
        conversionChoice2 = input("Invalid option pick hex,denary or binary\n>>")

    finalConversionChoice = conversionChoice1 + conversionChoice2

    if finalConversionChoice == "hexdenary":
        hexdenary()
    elif finalConversionChoice == "hexbinary":
        hexbinary()
    elif finalConversionChoice == "denaryhex":
        denaryhex()
    elif finalConversionChoice == "denarybinary":
        denarybinary()
    elif finalConversionChoice == "binarydenary":
        binarydenary()
    elif finalConversionChoice == "binaryhex":
        binaryhex()

def printConversionChoice():
    print("You want to convert", conversionChoice1, "to", conversionChoice2)


def hexdenary():
    printConversionChoice()
    binary = input("enter a number: ")
    value = convertToDenary(16, binary)
    print(value)

def hexbinary():
    printConversionChoice()

def convertFromDenary(base, d):
    digits = "0123456789ABCDEF"
    if d <= 0:
        return "0"
    value = ""
    while d >= 1:
        digit = int(d%base)
        value = digits[digit]+value
        d = d/base
    return value

def convertToDenary(base, d):
    value = 0
    index = 0
    for digit in reversed(d):
        value += (int(digit)*(base**index))
        index+=1
    return value

def denaryhex():
    printConversionChoice()
    d = int(input("Enter the number\n>>"))
    print(convertFromDenary(16,d))

def denarybinary():
    printConversionChoice()
    d = int(input("Enter the number\n>>"))
    print(convertFromDenary(2, d))


def binarydenary():
    printConversionChoice()
    binary = input("enter a number: ")
    value = convertToDenary(2,binary)
    print(value)

def binaryhex():
    printConversionChoice()

startUpMenu()
