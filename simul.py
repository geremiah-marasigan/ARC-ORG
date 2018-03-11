print("==========IEEE-754 Binary-64 floating point converter==========")

# CHARACTERS ALLOWED IN INPUT
binaryChar = "10.-"

# INITILIZATION
stdexp = 0
signBit = 0

# CHECK IF VALID BINARY INPUT #
def bin_check(inp):
    global signBit
    signBit = 0
    if(inp.count(".") > 1 or inp.count("-") > 1 or ("-" in inp and inp[0] is not "-")):
        return False
    
    if(inp[0] is "-"):
        signBit = 1
        if(inp[1] is "."):
            return False
    else:
        if(inp[0] is "."):
            return False

    return all(x in binaryChar for x in inp)

# USES FLOAT
'''
def standardizeBin(binput):
    global stdexp
    stdexp = exp
    
    first = 0
    if signBit is 1:
        first = 1
    
    while True:
        if binput[first] is "1" and binput[first+1] is ".":
            return binput
        elif "1" not in binput:
            return "0.0"
        # MOVES FLOATING POINT TO THE RIGHT, SUBTRACTS EXPONENT
        elif binput[first] is "0":
            binput = str(float(binput) * 10)
            print(binput)
            stdexp = stdexp-1
        # MOVES FLOATING POINT TO THE LEFT, ADDS EXPONENT
        else:
            binput = str(float(binput) / 10)
            print(binput)
            stdexp = stdexp+1
'''

# USES STRING
def standardizeBin(binput):
    global stdexp
    stdexp = exp
    
    first = 0
    if signBit is 1:
        first = 1
    
    while True:
        if binput[first] is "1" and binput[first+1] is ".":
            return binput
        elif "1" not in binput:
            return "0.0"
        # MOVES FLOATING POINT TO THE RIGHT, SUBTRACTS EXPONENT
        elif binput[first] is "0":
            binput = list(binput)
            point = binput.index(".")
            switch = point + 1
            temp = binput[switch]
            binput[switch] = "."
            binput[point] = temp
            binput = "".join(binput)
            print(binput)
            stdexp = stdexp-1
        # MOVES FLOATING POINT TO THE LEFT, ADDS EXPONENT
        else:
            binput = list(binput)
            point = binput.index(".")
            switch = point - 1
            temp = binput[switch]
            binput[switch] = "."
            binput[point] = temp
            binput = "".join(binput)
            print(binput)
            stdexp = stdexp+1

# ASKS FOR BINARY INPUT, BREAKS ONLY WHEN VALID                       
while True:
    binary_input = input("Input binary number: ")
    if bin_check(binary_input):
        break
    else:
        print("ERROR: INVALID INPUT. TRY AGAIN")

# ASKS FOR EXPONENT, BREAKS ONLY WHEN VALID
while True:
    try:
        exp = int(input("Input exponent base-2: "))
        break
    except ValueError:
        print("ERROR: INVALID INPUT. TRY AGAIN")

# ADDS .0 IF THERE'S NO .
if binary_input.count(".") is 0:
    binary_input += ".0"

print("Input is " + binary_input + " x 2^" + str(exp))        


stdBin = standardizeBin(binary_input)

# CUT
if len(stdBin) > len(binary_input):
    stdBin = stdBin[:len(binary_input)]


print("Standardized Input is " + stdBin + " x 2^" + str(stdexp))

# CONSIDER SPECIAL CASES
# CASE: 0
if "1" not in stdBin:
    ePrime = 0
    floatingBits = "0"
# CASE: INFINITY
elif stdexp > 1023 and "0" not in stdBin:
    ePrime = 2047
    floatingBits = "0"
# CASE: DENORMALIZED
elif stdexp < -1022:
    ePrime = 0
    while stdexp < -1022:
        stdBin = str(float(stdBin) / 10)
        stdexp += 1
    if signBit is 0:
        floatingBits = stdBin[2:]
    else:
        floatingBits = stdBin[3:]
# NORMAL CASE
else:
    ePrime = stdexp + 1023
    if signBit is 0:
        floatingBits = stdBin[2:]
    else:
        floatingBits = stdBin[3:]

# CONVERTS E-PRIME TO A 11 DIGIT BINARY STRING
ePrime = "{0:011b}".format(ePrime)

# ADDS TRAILING 0s, REMOVES EXCESS 0s
while(len(floatingBits) < 52):
    floatingBits = floatingBits + "0"
while(len(floatingBits) > 52):
    floatingBits = floatingBits[:-1]

# CUTS FLOATING
#floatingBits = floatingBits[:52]
    
print("Sign Bit: " + str(signBit))
print("Eprime: " + ePrime)
print("F: " + floatingBits)

# BUILT IN HEX CONVERTER
convertedHex = hex(int(str(signBit) + str(ePrime) + floatingBits,2))
padding = convertedHex.split('x')
paddedHex = padding[1].zfill(16)
final = '0x' + paddedHex
print("Hex: " + final)
