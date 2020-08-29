'''
[5ex5]
Bitshift to right.\

TEST CASES:
INPUT(S)  : OUTPUTS(S)
01011     : 10101
0001      : 1000
10110     : 01011
0111      : 1011
'''
bitString = list((input("please enter bitString: ")))
rightDig = bitString.pop(-1)
bitString = "".join(bitString)
bitString = rightDig+bitString

print(bitString)

    

