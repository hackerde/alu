# blogic.py -- implementation of primitives for representing binary logic 
#   in Python.  All args assumed to be 0 or 1.   $Revision: 1.1 $ 

def binVal(b):
    if b:
        return 1
    else:
        return 0

def band(a, b, c=1, d=1):
    return binVal(a==1 and b==1 and c==1 and d==1)

def bor(a, b, c=0, d=0):
    return binVal(a==1 or b==1 or c==1 or d==1)

def bnot(a):
    return binVal(a==0)

def bxor(a, b):
    return binVal(a+b == 1)
