import math
while True:
    op=input()
    if op=="exit":
        break
    if op =="sin" or op=="sin" or op=="cos"or op=="tan"or op=="cot"or op=="fact" or op=="log":
        a=int(input())    
    else:
        a=int(input())
        b=int(input())  
    if op=="+":
        result=a+b
    elif op=="-":
        result=a-b
    elif op=="*"    :
        result=a*b
    elif op=="/"    :
        if b!=0:
            result=a/b 
        else:
            result="cannot divide by zero" 
    elif op=="^"  :
        result=a**b
    elif op=="sin"  :
        result=math.sin(a)
    elif op=="cos"  :
        result=math.cos(a) 
    elif op=="tan"  :
        result=math.tan(a) 
    elif op=="cot"  :
        result=1/math.tan(a) 
    elif op=="fact"  :
        result=math.factorial(a) 
    elif op=="log"  :
        result=math.log10(a) 
    else:
        result= "i dont no"  
        print(result)   
