
def selectionsort(l):
  for i in range(len(l)-1):
    for j in range(i+1,len(l)):
      while( l[j]<l[i]):
        k=l[i]
        l[i]=l[j]
        l[j]=k
    #print(l) enable this print to know the step wise list values
  return l














# l is the list of elements
l=[int(x)for x in input("enter numbers:").split()]
sorted_l=selectionsort(l)
print(sorted_l)