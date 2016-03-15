#This input method is shit, fix it
#def userPrompt():

    '''
    If temp is Kelvin, Enter K
    If temp is Fahrenheight, Enter F
    If temp is Celsius, enter C:
    '''

    convertResult = 0
    print inTypePrompt
    userInTemp = input("enter input Temp type:")
    userInTemp.upper()
    inputTemp = input("enter input temp:")

    #if inTypePrompt == "K":
        #if

        print inTypePrompt
        userOutTemp = input("enter output temp type:")
        userOutTemp.upper()


userPrompt()
if inTypePrompt == "K":
    if userOutTemp == "C":
        KelvinToC(inputTemp, convertResult):
    elif userOutTemp == "F":
        KelvinToF(inputTemp, convertResult)
elif inTypePrompt == "F":
    if userOutTemp == "K":
        FahrenheightToK(inputTemp, convertResult)
    elif userOutTemp == "C":
        FahrenheightToC(inputTemp, convertResult)
elif inTypePrompt == "C":
    if userOutTemp == "F":
        CelsiusToF(inputTemp, convertResult)
    elif userOutTemp == "K":
        CelsiusToK(inputTemp, convertResult)
else:
    print "invalid option entered"
    print "to try again, enter 1"
    print "to quit, enter 2"
    decError = input("enter:")
    if decError == 2:
        print "goodbye"
        pass
    elif decError == 1:
        print "trying again"
        userPrompt():




def KelvinToF():
    '''
    description
    '''

def KelvinToC():
    '''
    0 C = 273.15 K
    '''


def FahrenheightToK():
    '''
    description
    '''

def FahrenheightToC():
    '''
    description
    '''

def CelsiusToK():
    '''
    description
    '''

def CelsiusToF():
    '''
    description
    '''
