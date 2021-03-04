
shapeSelected = ""
shapeSize = ""
outlineSelected = ""
shapes = ["square", "triangle", "diamond", "pyramid"]
selectableOutline = ["whole", "outline", "special"]
specialCharacters = ["*","!", "@", "#","$","%", "^", "&"]


def main():    
        
    shapeSelected = ""
    while (not shapeSelected in shapes):
        print ("Which shape would you like to print")
        print ("\n\nThe options available are \"square\", \"triangle\", \"diamond\", and \"pyramid\".\nGive your answer without paratheses")
        shapeSelected = input().lower()
    

    shapeSize = ""
    while (not isinstance(shapeSize, int)):
        print ("\n\nWhat should the size of the shape be?\nChoose a whole number")
        shapeSize = int(input())

        while (shapeSize < 5 or shapeSize > 80):
            print ("\n\nWhat should the size of the shape be?\nChoose a number from 5 to 80")
            shapeSize = int(input())


    outlineSelected = ""
    while (not outlineSelected in selectableOutline):
        print ("\n\nShould this be the whole shape, only the outline, or a special shape")
        print ("The options available are \"whole\", \"outline\" or \"special\"")
        print ("Give your answer without paratheses")
        outlineSelected = str(input().lower())

    if shapeSelected.lower() == "square":
        wholeSquare(shapeSize, outlineSelected)

    elif shapeSelected.lower() == "triangle":
        WholeTriangle(shapeSize, outlineSelected)

    elif shapeSelected.lower() == "diamond":
        WholeDiamond(shapeSize, outlineSelected)

    elif shapeSelected.lower() == "pyramid":
        WholePyramid(shapeSize, outlineSelected)

    # End of main

def wholeSquare (size, outlineSelected):
    stringBuilder = ""

    if outlineSelected == "outline":
        firstLine = "*" * size
        otherLines = "*" + " " * (size - 2) + "*"

        for i in range (size):
            if i == 0 or i == size - 1:
                print (firstLine)
            else:
                print (otherLines)

    elif outlineSelected == "special":
        for i in range(size):
            print (SpecialCharacterFunction(size))

    
    else:
        for i in range (size):
            stringBuilder += "*"
        
        for i in range (size):
            print (stringBuilder)

def WholeTriangle(size, outlineSelected):
    stringBuilder = ""

    if outlineSelected == "outline":
        for i in range (size):
            stringBuilder += "*"
            if (i > 1 and i != size - 1):
                print ("*" + stringBuilder[1:size-1].replace("*", " ") + "*")
            else:
                print (stringBuilder.replace(" ", "*"))

    if outlineSelected == "special":
        for i in range (size + 1):
            print(SpecialCharacterFunction(i))

    
    else:
        for i in range (size):
            stringBuilder += "*"
            print (stringBuilder)

def WholePyramid(size, outlineSelected):
    stringBuilder = ""    
    lineBuiler = ""
    
    if outlineSelected == "outline":
        for j in range (size):
            for i in range (size - j):
                stringBuilder += " "
            lineBuiler =  "*" * int((j) * 2 + 1)

            if (len(lineBuiler) != 1 and j != size - 1):
                lineBuiler = "*" + lineBuiler[1:len(lineBuiler) - 1].replace("*", " ") + "*"
            stringBuilder += lineBuiler

            if not j == size - 1:
                stringBuilder += "\n"

    if outlineSelected == "special":
        for j in range (size):
            for i in range (size - j):
                stringBuilder += " "
            stringBuilder +=  SpecialCharacterFunction((j - 1) * 2 + 1)
            if not j == size - 1:
                stringBuilder += "\n"

    else:
        for j in range (size):
            for i in range (size - j):
                stringBuilder += " "
            stringBuilder +=  "*" * int((j - 1) * 2 + 1)
            if not j == size - 1:
                stringBuilder += "\n"
    
    print (stringBuilder)

def WholeDiamond(size, outlineSelected):
    stringBuilder = ""
    reverseString = ""
    lineBuilder = ""
    space = ""

    if outlineSelected == "outline":
        for j in range (size):
            for i in range (size - j):
                stringBuilder += " "

            if (j == 0):
                lineBuilder = "*"
            else:
                lineBuilder =  "*" + ("*" * int((j) * 2 + 1))[1:-1].replace("*", " ") + "*" 

            if not j == size - 1:
                stringBuilder += lineBuilder + "\n"
                reverseString = "\n" + reverseString
            
            if j < size - 1 :
                reverseString = (size - j) * " " +  "*" + ("*" * int((j - 1) * 2 + 1)).replace("*", " ") + "*"  + reverseString
        print (stringBuilder + "*" + (len(lineBuilder) - 2) * " " + "*" + "\n " + reverseString[1:-2])

    if outlineSelected == "special":
        for i in range(size):
	        print (" " * (size - i) + SpecialCharacterFunction((i + 1) * 2 -1))

        for i in range(size + 1):
	        print (" " * (i) + SpecialCharacterFunction((size + 1 - i) * 2 -1))
    
    else:
        for j in range (size):
            for i in range (size - j):
                stringBuilder += " "
            stringBuilder +=  "*" * int((j - 1) * 2 + 1)
            if not j == size - 1:
                stringBuilder += "\n"
                reverseString = "\n" + reverseString
            
            if j < size - 1 :
                reverseString =  (size - j) * " " + "*" * int((j - 1) * 2 + 1)  + reverseString
        print (stringBuilder + "\n" + reverseString)     

def SpecialCharacterFunction (numberOfCharacters):

    if numberOfCharacters == 0 or numberOfCharacters == -1:
        return ""

    returnString = ""

    for i in range (int(numberOfCharacters/2)):
        returnString += specialCharacters[i  % 8]

    if (numberOfCharacters % 2 == 1):
        return returnString + specialCharacters[int(numberOfCharacters / 2) % 8]+ returnString[::-1]

    else:
        return returnString + returnString[::-1]

    



if __name__ == "__main__":
    main()

