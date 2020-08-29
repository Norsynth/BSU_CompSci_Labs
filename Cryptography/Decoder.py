'''
[5ex2.py]
Decoder
This program uses a string of characters and reverses the order

TEST CASES:
INPUT(S)   : OUTPUTS(S)
yjxynsl,5  : testing
ecogtqp,2  : cameron
tvmsvpeoi,4: priorlake
lowsnts,10 : bemidji
'''
code = input("Enter the coded message:")
distance = int(input("Enter the distance value:"))
plainText=""

for ch in code:
    ordvalue= ord(ch)
    cipherValue = ordvalue - distance
    if cipherValue < ord('a'):
        cipherValue = ((ord('z')- distance) - (ord('a')- ordvalue - 1))
                      
    plainText += chr(cipherValue)

print(plainText)


