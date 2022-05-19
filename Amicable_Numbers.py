n=int(input())
m=int(input())
s=0
sl=0
for x in range(1,n):
    if n%x==0:
        s=s+x
for y in range(1,m):
    if m%y==0:
        sl=sl+y
if s==m and sl==n:
    print('Amicable')
else:
    print('Not Amicable')