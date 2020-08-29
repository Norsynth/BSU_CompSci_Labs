'''
[5ex1.py]
Encrypter:
This program encrypts a message my altering each characters ascii value.

TEST CASES:
INPUT(S)   : OUTPUTS(S)
testing,5  : yjxynsl
cameron,2  : ecogtqp
priorlake,4: tvmsvpeoi
bemidji,10 : lowsnts
'''
plainText = input("Enter a one-word lowercase message:")
for x in range(30):
    distance = x
    code=""

    for ch in plainText:
        ordvalue= ord(ch)
        cipherValue = ordvalue + distance
        if cipherValue > ord('z'):
            cipherValue = (ord('a')+ distance) - (ord('z')- ordvalue + 1)
                      

        code += chr(cipherValue)

    print(code)


#int(input("Enter a Distance:"))



