print("==========IEEE-754 Binary-64 floating point converter==========")
binaryChar = "10."

# CHECK IF VALID BINARY INPUT #
def bin_check(inp):
    if(inp.count(".") > 1):
        return False
    
    return all(x in binaryChar for x in inp)

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