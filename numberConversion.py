

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

def hexbinary():
    printConversionChoice()

def denaryhex():
    printConversionChoice()
    d = int(input("Enter the number\n>>"))
    digits = "0123456789ABCDEF"
    if d <= 0:
        return "0"
    base = 16
    hex = ""
    while d >= 0:
        digit = int(d%base)
        hex = digits[digit]+hex
        d = d/base
    print(hex)

def denarybinary():
    printConversionChoice()

def binarydenary():
    printConversionChoice()

def binaryhex():
    printConversionChoice()

startUpMenu()
