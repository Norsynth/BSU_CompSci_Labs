from Stack import Stack

def infixToPostfix(infix):
    prec = {} #dictionary to map precedence of each value
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infix.split() #creates list based on spaces

    for token in tokenList:
        if token in "0123456789":
            postfixList.append(token)
        elif token == '(': 
            opStack.push(token) #pushes onto operator stack
        elif token == ')':
            topToken = opStack.pop() #makes the last pushed operator a toptoken
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:                           #peek is 0 for changed argument requirement
            while (not opStack.isEmpty()) and (prec[opStack.peek(0)] >= prec[token]):
                  postfixList.append(opStack.pop()) #appends operations based on precedence
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList) #joins by spaces

def postfixEval(postfix):
    opStack = Stack()
    tokenList = postfix.split()

    for token in tokenList:
        if token in "0123456789":
            opStack.push(int(token)) #pushes decimal value onto list
        else:
            op2 = opStack.pop() #pops decimals off for doMath()
            op1 = opStack.pop()
            result = doMath(token,op1,op2)
            opStack.push(result) #holds result for future usage and final result
    return opStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

print("("+infixToPostfix("3 * 2 + 1 * 3")+")","equals:",postfixEval("3 2 * 1 3 * +"))
print("("+infixToPostfix("( 4 + 3 ) * 4 - ( 5 - 3 ) * ( 2 + 1 )")+")","equals:",postfixEval("4 3 + 4 * 5 3 - 2 1 + * -"))
print("("+infixToPostfix("7 + 3 * 4 + 2 ")+")","equals:",postfixEval("7 3 4 * + 2 +"))
print("("+infixToPostfix("1 + 2 / 3 ")+")","equals:",postfixEval("1 2 3 / +"))
print("("+infixToPostfix("( 3 * 2 ) + 1 * 3")+")","equals:",postfixEval("3 2 * 1 3 * +"))

