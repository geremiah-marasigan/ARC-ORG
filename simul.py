print("==========IEEE-754 Binary-64 floating point converter==========")
binaryChar = "10.-"
stdexp = 0
signBit = 0
# CHECK IF VALID BINARY INPUT #
def bin_check(inp):
    global signBit
    if(inp.count(".") > 1 or inp.count("-") > 1 or "-" in inp and inp[0] is not "-"):
        return False
    
    if(inp[0] is "-"):
        signBit = 1
        if(inp[0] is "."):
            return False
    else:
        if(inp[0] is "."):
            return False

    return all(x in binaryChar for x in inp)
    
def standardizeBin(binput):
    global stdexp
    stdexp = exp
    
    first = 0
    if(signBit is 1):
        first = 1
    
    while True:
        if(binput[first] is "1" and binput[first+1] is "."):
            return binput
        elif(binput[first] is "0"):
            binput = str(float(binput) * 10)
            print(binput)
            stdexp = stdexp-1
        else:
            binput = str(float(binput) * 0.1)
            print(binput)
            stdexp = stdexp+1
            
            
while True:
    binary_input = input("Input binary number: ")
    if bin_check(binary_input):
        break
    else:
        print("ERROR: INVALID INPUT. TRY AGAIN")




while True:
    try:
        exp = int(input("Input exponent base-2: "))
        break
    except ValueError:
        print("ERROR: INVALID INPUT. TRY AGAIN")

print("Input is " + binary_input + " x 2^" + str(exp))        

stdBin = standardizeBin(binary_input)
print("Standardized Input is " + stdBin + " x 2^" + str(stdexp))

ePrime = stdexp + 1023



if(signBit is 0):
    floatingBits = stdBin[2:]
else:
    floatingBits = stdBin[3:]

ePrime = "{0:011b}".format(ePrime)
    
while(len(floatingBits) < 52):
    floatingBits = floatingBits + "0"

print("Sign Bit: " + str(signBit))
print("Eprime: " + ePrime)
print("F: " + floatingBits)

final = hex(int(str(signBit) + str(ePrime) + floatingBits, 2))

print("Hex: " + final)


