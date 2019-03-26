#아이디어 제공: 이희준
m=int(input())
n=int(input())
List=[]
q=0
if m>n:
    high=m
    low=n

else :
    high=n
    low=m

for i in range(low,high+1):
    for o in range(2,high):
        if i==2:
            q=q+i
            List.append(i)
            break
        elif i%o==0 or i==1:
            break
        else :
            q=q+i
            List.append(i)
            break
        
print(q)
print(min(List))

            
            
