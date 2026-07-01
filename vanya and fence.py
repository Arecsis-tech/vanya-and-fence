n,h=map(int,input().split())
a=list(map(int,input().split()))
x=0
for i in range(n):
    if a[i]<=h:
        x=x+1
    else:
        x=x+2
print(x)
