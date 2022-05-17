a=int(input())
k=a 
s=0
while a:
    r=a%10
    s=s+r
    a=a//10
if k%s==0:
    print('True')
else:
    print('False')