l1=[1,2,3,4,5]
l3=[int(x) for x in input().split()]
print(l3)
l2=int(input("number:"))
if l2 in l1:
  print(l1.index(l2))
else:
  print(-1)
#print(l1[-1:-len(l1)-1:-1])