
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
    A = 10
    B = 11
    C = 12
    D = 13
    E = 14
    F = 15
    printConversionChoice()
    digits = input("Enter your hex digit\n>>")
    if len(digits) == 2:
        answer = digits[0] * 16 + digits[1]
        print(answer)

def hexbinary():
    printConversionChoice()

def convertFromDenary(base, d):
    digits = "0123456789ABCDEF"
    if d <= 0:
        return "0"
    hex = ""
    while d >= 1:
        digit = int(d%base)
        hex = digits[digit]+hex
        d = d/base
    return hex

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
    decimal = 0
    for digit in binary:
        decimal = decimal * 2 + int(digit)
    print(decimal)


def binaryhex():
    printConversionChoice()

startUpMenu()
