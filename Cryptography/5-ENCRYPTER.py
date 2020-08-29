'''
Encrypter
Convers characters to asii, adds one to the value,
switches to binary, and leftshifts.
TEST CASES:
INPUT(S)   : OUTPUTS(S)
Hey!       : 0010011 1001101 1110101 000101
yeehaw     : 1110101 1001101 1001101 1010011 1000101 1110001
27         : 100111 110001
win3       : 1110001 1010101 1011111 101001 100111
'''
plainText = input("Please enter the message to encrypt:")
code=""
distance=0
for ch in plainText:
    ordValue= ord(ch)
    code+= str(ordValue)
    code+= str(" ") #Used to convert characters into ascii format.
codeSplit=code.split()
codeSplitNum = [int(i) for i in codeSplit]
codeSplitPlus = [x+1 for x in codeSplitNum]#adds one to ascii value.
codeList = []

for x in codeSplitPlus:
    if x == 0:
        print(0)
    else:
        binary = "" #whileloop used to convert to binary
        while x > 0:
            
            remainder = x % 2
            x = x // 2
            binary = str(remainder)+binary

        binary = list(binary)
        leftDig = binary.pop(0)
        binary+=leftDig #binary code is then leftshifted
        binary = "".join(binary)
        codeList.append(binary)
        
binaryStr = ""
for i in codeList:
    binaryStr += "".join(i)+" "

    
print("Your encrypted message is:")
print(binaryStr)

