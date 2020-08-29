'''
[6ex1]
#Open file resulting in a string of text
#Encrypt every character by switching value +1

TEST CASES:

INPUT(S)   : OUTPUTS(S)

test.txt, 2 : Jg{#"Lwuv"c"ukorng"gzcorng"<F

'''
f = open(input("Enter a file to encrypt:"), "r")
plainText = f.read()
distance = eval(input("Enter Distance:"))
code=""

for ch in plainText:
    ordvalue= ord(ch)
    cipherValue = ordvalue + distance
    if cipherValue > 127:
        
        cipherValue = ((0)+ distance) - ((127)- ordvalue + 1)
                      

    code += chr(cipherValue)

print(code)


