'''
[5ex4]
Octal to Decimal.
TEST CASES:
INPUT(S)   : OUTPUTS(S)
12         : The interger value is: 10
24         : The interger value is: 20
62         : The interger value is: 50
113        : The interger value is: 75
'''
bitString = input("Enter a string of octals:")
decimal = 0
exponet = len(bitString)-1
for digit in bitString:
    decimal = decimal + int(digit) * 8 ** exponet
    exponet = exponet - 1
    
if decimal == 0:
    print(0)
else:
    print("The interger value is:",decimal)
