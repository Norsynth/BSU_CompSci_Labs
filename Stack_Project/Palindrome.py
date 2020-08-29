from Stack import Stack


def PalinCheck(text):
    '''checks if inputed word is the same inside and out'''
    s=Stack()
    word=''
    reverseWord = ''
    for i in text:
        s.push(i)
        word+=i #creates initial word
    for i in range(s.size()):
        reverseWord += s.pop() #pops off stack to create new word

    if word == reverseWord: #compares words
        return print(True)
    else:
        return print(False)
    

PalinCheck("wassamassaw")
PalinCheck("finland")
PalinCheck("paraparap")
PalinCheck("kenya")
PalinCheck("malayalam")



