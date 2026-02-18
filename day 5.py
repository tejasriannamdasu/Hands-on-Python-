m=int(input("Enter the number of entries:"))
requests=[0]*m
for i in range(m):
    requests[i]=int(input("Enter the element:"))
no_demand=[0]*m
low_demand=[0]*m
high_demand=[0]*m
moderate_demand=[0]*m
invalid_requests=[0]*m
n=0
l=0
h=0
mod=0
i=0
valid_entries=0
ignored_entries=0
L=input("Enter your name  without spaces:")
print("Name:",L)
PLI=len(L)%3
print("pli =",PLI)
for i in range(m):
    r=requests[i]
    if r<0:
       ignored_entries+=1
       invalid_requests[i]=r
       i=i+1
    else:
        valid_entries+=1
        if(r==0):
            no_demand[n]=r
            n=n+1
        elif(r>=1 and r<=20):
          low_demand[l]=r
          l=l+1
        elif(r>=21 and r<=50):
          moderate_demand[mod]=r
          mod=mod+1
        else:
          high_demand[h]=r
          h=h+1
print("Total requests are:",m)
print("Total valid entries:",valid_entries)
print("Before Personalization:")
print("low_demand-> ", low_demand)
print("high demand-> ", high_demand)
print("moderate demand->", moderate_demand)
print("invalid_requests->", invalid_requests)
print("After Personalization:")
removed_count=0
if PLI==0:
    print("The number of requests removed due to pli is", l)
    removed_count=l
    l=0
elif PLI==1:
    print("The number of requests removed due to pli is", h)
    removed_count=h
    h=0
else:
    print("The number of requests removed due to pli is", m)
    removed_count=mod
    mod=0
print("low_demand :", low_demand[:l])
print("high demand :", high_demand[:h])
print("moderate demand:", moderate_demand[:m])
print("invalid_requests->", invalid_requests[:i])
print("Total Valid Entries:", valid_entries)
print("Total Ignored Entries:", ignored_entries)



