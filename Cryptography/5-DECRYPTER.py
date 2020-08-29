'''
Decrypter:
Used to solve example5 by reversing the sequence of events.
TEST CASES:
INPUT(S)   : OUTPUTS(S)
0010011 1001101 1110101 000101:Hey!
1110101 1001101 1001101 1010011 1000101 1110001:yeehaw
100111 110001:27
1110001 1010101 1011111 101001 100111:win3
'''
binaryCode = input("Please enter binary code:")
binaryCode= binaryCode.split()
#splits code into lists

newlist=[]
for i in binaryCode:
    x = list(i)
    newlist.append(x)

newlist2=[]

for i in newlist:
    y= list(i)
    newlist2.append(y)
#converts each binary character into a list
print(newlist2)
newlist3=[]
for i in newlist:
    rightDig = i.pop()
    rightDig = list(rightDig)
    i= rightDig+i
    newlist3.append(i)
#rightshifts binary
    print(newlist3)
    
lists=[]
for list in newlist3:
    jaevla=(''.join(list))
    lists.append(jaevla)
#joins the list

    
print(lists)
lists2=[]
for i in lists:
    decimal = 0
    exponet = len(i)-1
    for digit in i:
            decimal = decimal + int(digit) * 2 ** exponet
            exponet = exponet - 1
    lists2.append(decimal)
#converts to decimal
lists3=[]
for i in lists2:
    i = i-1
    lists3.append(i)
#subtracts one
lists4=[]
for i in lists3:
    i = chr(i)
    lists4.append(i)
#turns to ascii character
message = ""
for i in lists4:
    message += str(i)
#concatenates string
print("Your message is:",message)
            

