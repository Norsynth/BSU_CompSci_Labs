'''
[5ex4]
Decimal to Octal:
Converts decimal form to octal

TEST CASES:
INPUT(S)   : OUTPUTS(S)
10         : The octal is:12
20         : The octal is:24
50         : The octal is:62
75         : The octal is:113
'''
decimal = int(input("Enter a decimal integer:"))
if decimal == 0:
    print(0)
else:
    print("Quotient Remainder Octal")
    octString = ""
    while decimal > 0:
        remainder = decimal % 8
        decimal = decimal // 8
        octString = str(remainder)+octString
        print("%5d%8d%12s" % (decimal, remainder, octString))
    print("The octal is:", octString)
