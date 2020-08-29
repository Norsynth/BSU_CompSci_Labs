import random
import time
import string
letters = list(string.ascii_lowercase)

def MakeWord(n):
    '''Used to create a word of n characters'''
    word=[]
    wordstr=''
    for i in range(n):
        word.append(random.choice(letters))
        wordstr=''.join(map(str, word))
    return wordstr


def anagramSolution1(s1,s2): #O(n^2) Checking off method
    stillOK = True
    if len(s1) != len(s2):
        stillOK = False

    alist = list(s2)
    pos1 = 0

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 = pos1 + 1

    return stillOK




def anagramSolution2(s1,s2): #O(n log n) Sort and compare method
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos]==alist2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches



def anagramSolution4(s1,s2): #O(n) Count and Compare method
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(s1)):
        pos = ord(s1[i])-ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    stillOK = True
    while j<26 and stillOK:
        if c1[j]==c2[j]:
            j += 1
        else:
            stillOK = False

    return stillOK


def main():
    file = open("BigOTimes.csv","w")
    trial = 0
    for n in range(4):
        print("Test Trial",str((n+1))+":")
        print('%0s, %15s, %12s , %13s'%('WordLength','AnagramO(n^2)','AnagramO(n log n)','AnagramO(n)'))
        print("---------------------------------------------------------------")
        trial+=1
        for i in range(500,7501,500):
                
            wrd = MakeWord(i)
            wrd2 = wrd[::-1] #reverse of words
                
            n2s = time.time() #start clock
            n2 = anagramSolution1(wrd,wrd2)
            n2e = time.time() #end clock
                
            nlogns = time.time()  
            nlogn = anagramSolution2(wrd,wrd2)
            nlogne= time.time() #subtract from start to find total

            ns= time.time()
            n= anagramSolution4(wrd,wrd2)
            ne= time.time()
            
            print("%s, %15.5f, %15.5f, %15.5f" %(i,n2e-n2s,nlogne-nlogns,ne-ns))
            print("")
            file.write("%s,%s,%.10f,%15.5f,%26.5f\n"%(trial,i,n2e-n2s,nlogne-nlogns,ne-ns))

    file.close()



if __name__ == "__main__":
    main()



