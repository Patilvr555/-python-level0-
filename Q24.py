type= str(input("f or c")) 

if type=='f':
    
    temp=float(input("give temp in f"))
    if temp:
        tempincel=5*(temp-32)/9
        print("temp in centigrade",tempincel)

if type=='c':
    
    temp2=float(input("give temp in c"))
    if temp2:
        tempinf=(temp2*0.2)+32
        print("temp in f",tempinf)
