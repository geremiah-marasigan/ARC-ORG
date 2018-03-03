print("==========IEEE-754 Binary-64 floating point converter==========")
binaryChar = "10."
stdexp = 0

# CHECK IF VALID BINARY INPUT #
def bin_check(inp):
    if(inp.count(".") > 1 or inp[0] is "."):
        return False
    
    return all(x in binaryChar for x in inp)
    
def standardizeBin(binput):
    global stdexp
    stdexp = exp
    while True:
        if(binput[0] is "1" and binput[1] is "."):
            return binput
        elif(binput[0] is "0"):
            binput = str(float(binput) * 10)
            print(binput)
            stdexp = stdexp+1
        else:
            binput = str(float(binput) * 0.1)
            print(binput)
            stdexp = stdexp-1
            
            
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

