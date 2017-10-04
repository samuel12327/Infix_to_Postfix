from Class import StackClass
user_input = input("Enter Equation: ")

def infixtopostfix(infixexpr):

    s=StackClass()
    outlst=[]
    prec={}
    prec['/']=3
    prec['*']=3
    prec['+']=2
    prec['-']=2
    prec['(']=1

    tokenlst=infixexpr.split()
    for token in tokenlst:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
            outlst.append(token)

        elif token == '(':
            s.push(token)

        elif token == ')':
            topToken=s.pop()
            while topToken != '(':
                outlst.append(topToken)
                topToken=s.pop()
        else:
            while (not s.Empty()) and (prec[s.peek()] >= prec[token]):
                #print token
                outlst.append(s.pop())
                #print outlst
            s.push(token)
            print (s.peek())
    while not s.Empty():
        opToken=s.pop()
        outlst.append(opToken)
        #print outlst
    return outlst
    #return " ".join(outlst)

print(infixtopostfix(user_input))
