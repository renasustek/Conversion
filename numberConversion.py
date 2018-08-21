#def hexList():
hexListNumbers = [0,1,2,3,4,5,6,7,8,9]


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
    hexOption = int(input("Enter the first hex digit\n>>"))
    hexOption2 = int(input("Enter the first hex digit\n>>"))
    if hexOption and hexOption2 not in hexListNumbers:
        hexdenary()

    optionHexAnswer = (hexOption*16)+(hexOption2)
    print(hexOption + hexOption2,"in denary is",optionHexAnswer)



def hexbinary():
    printConversionChoice()

def denaryhex():
    printConversionChoice()

def denarybinary():
    printConversionChoice()

def binarydenary():
    printConversionChoice()

def binaryhex():
    printConversionChoice()

startUpMenu()
