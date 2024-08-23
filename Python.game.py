def funcx(a,x):
    if a>x:
        LCM=a
    elif x>a:
        LCM=x
    
    while True:
        if (LCM%a==0 and LCM%x==0):
            return LCM
        LCM+=1
        

n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    new=[]
    pew=[]
    m=a*b
    for i in range(a+1,m+1):
        k=funcx(a,i)
        new.append(k)
        l=funcx(m,i)
        pew.append(l)
    new.sort()
    pew.sort()
    print(f"{new[0]} {pew[-1]}")