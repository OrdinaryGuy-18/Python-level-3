n=int(input())
lst=[]
for _ in range(n):
    lst.append(input())
for x in lst:
    if len(x)>=10:
        print(x[0],len(x)-2,x[len(x)-1],sep="")
    else:
        print(x)
