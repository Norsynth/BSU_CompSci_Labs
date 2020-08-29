'''
[6ex4]
Fibonnacci Sequence: given number of terms>
(starting at 0)

TEST CASE(S):
INPUT(S)   : OUTPUTS(S)
7  : 0 1 1 2 3 5 8 
5  : 0 1 1 2 3
1  : 0
'''
f = open("4numsin.txt","r")
start=[]
for line in f:
    line = line.strip('\n')
    start.append(line)
f.close()

a=start[0]
b=start[1]
a=int(a)
b=int(b)

fout = open('4numsout.txt', "w")

#Fibonnachi Sequence
n = eval(input("Enter terms of Fibonnacci Sequence:"))
numbers=[]
if n==1:
    print(a)
    numbers.append(a)
else:
    print(a)
    print(b)
    numbers.append(a)
    numbers.append(b)
    for i in range (2,n):
        c = a + b
        a = b
        b = c
        print(c)
        numbers.append(c)


for i in numbers:
    fout.write(str(i)+"\n")

fout.close()

