#Diffie hellman example - First attempt
from random import randint
from math import sqrt


publicSharedPrimeModulus = 0
publicSharedBase = randint(100, 20000)
AliceSecretExponent = randint(100, 20000)
AliceSharedCalc = 0
BobSecretExponent = randint(100, 20000)
BobSharedCalc = 0
#Miller-Rabin Primality test, randint passed into function until 
#return == true

seed = randint(100, 20000)
seedBool = False
maxCount = 100
AliceSecretKey = 0
BobSecretKey = 0
SharedSecretKey = 0
#Fancy formatting stuff
strBorder = "----------------------------------------------------------------------------------"

def prime(seed):
    if seed < 2: return False
    for x in range(2, int(sqrt(seed)) + 1):
        if seed % x == 0:
            return False
    return True

while (prime(seed) == False or prime(seed) == None) == True: 
	seed = randint(100, 20000)
	prime(seed)

publicSharedPrimeModulus = seed
print(strBorder)
print(strBorder)
print("\t" + "Select a PseudoRandom prim number")
print("\t" + "Shared Prime Modulus" + "\t")
print(" \t" + "|" + "\t" + str(seed) + "\t" + "|" + "\t")
#print(strBorder)
#print("Shared p")
#print(str(seed) + " " + "shared prime modulus")
print(strBorder)
print(strBorder)
print("\t" + "Public Shared Base" + "\t")
print(" \t" + "|" + "\t" + str(publicSharedBase) + "\t" + "|" + "\t")
#print(str(publicSharedBase) + " " + "public shared base")
print(strBorder)
print(strBorder)
print("\t" + "Alice Secret Exponent" + "\t")
print(" \t" + "|" + "\t" + str(AliceSecretExponent) + "\t" + "|" + "\t")
print(strBorder)
print(strBorder)
print("\t" + "Bob's Secret Exponent" + "\t")
print(" \t" + "|" + "\t" + str(BobSecretExponent) + "\t" + "|" + "\t")

#print(str(AliceSecretExponent) + " " + "Alice secret exponent")

#Calculate AliceSharedCalc

AliceSharedCalc = pow(publicSharedBase, AliceSecretExponent, publicSharedPrimeModulus)
print(strBorder)
print(strBorder)
print("\t" + "Alice shared Calculation" + "\t")
print("\t" + "let Alice Shared Calculation = AC" + "\t")
print("\t" + "AC = {(Public Shared Base ^ (Alice's Secret Exponent)} Mod Public Shared Modulus")
print("\t" + "AC = " + "{" + str(publicSharedBase) + "^" + str(AliceSecretExponent) + "}" + "Mod" + " " + str(publicSharedPrimeModulus))
print("\t" + "|" + "\t" + str(AliceSharedCalc) + "\t" + "|" + "\t")


#Calculate Bob 
BobSharedCalc = pow(publicSharedBase, BobSecretExponent, publicSharedPrimeModulus)
print(strBorder)
print(strBorder)
print("\t" + "Bob's secret exponent" + "\t")
print("\t" + "let Bob Shared Calculation = BC" + "\t")
print("\t" + "BC = {(Public Shared Base ^ (Bob's Secret Exponent)} Mod Public Shared Modulus")
print("\t" + "BC = " + "{" + str(publicSharedBase) + "^" + str(BobSecretExponent) + "}" + "Mod" + " " + str(publicSharedPrimeModulus))
print(" \t" + "|" + "\t" + str(BobSharedCalc) + "\t" + "|" + "\t")

AliceSecretKey = pow(BobSharedCalc, AliceSecretExponent, publicSharedPrimeModulus)
print(strBorder)
print(strBorder)
print("\t" + "Alice Secret Key" + "\t")
print("\t" + "Let Alice Secret Key = ASK")
print("\t" + "ASK = {(BC ^ (Alice's Secret Exponent)} Mod Public Shared Modulus")
print("\t" + "ASK = " + "{" + str(BobSharedCalc) + "^" + str(AliceSecretExponent) + "}" + "Mod" + " " + str(publicSharedPrimeModulus))
print(" \t" + "|" + "\t" + str(AliceSecretKey) + "\t" + "|" + "\t")

BobSecretKey = pow(AliceSharedCalc, BobSecretExponent, publicSharedPrimeModulus)
print(strBorder)
print(strBorder)
print("\t" + "BobSecretKey" + "\t")
print("\t" + "Let Bob Secret key = BSK")
print("\t" + "BSK = {(AC ^ (Bob's Secret Exponent)} Mod Public Shared Modulus")
print("\t" +  "BSK = " + "{" + str(AliceSharedCalc) + "^" + str(BobSecretExponent) + "}" + "Mod" + " " + str(publicSharedPrimeModulus))
print(" \t" + "|" + "\t" + str(BobSecretKey) + "\t" + "|" + "\t")
print(strBorder)
#print(str(BobSecretKey) + " " + "Bob Secret Key")
print(strBorder)
print("\t" + "Lets Confirm the two calculations are the same ")
if AliceSecretKey == BobSecretKey: 
	print("\t" + str(BobSecretKey) +" "+"="+" "+str(AliceSecretKey))
	print("\t" + "shared key worked")
else: 
	print("\t" + "did not work")
print(strBorder)
print(strBorder)