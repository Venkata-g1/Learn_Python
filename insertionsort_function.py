
def insertsort(l):
  for j in range(1,len(l)):
    for i in range(0,j):
      while(l[j]<l[i]):
        K=l[i]
        l[i]=l[j]
        l[i+1]=K
      #print(l) to check all the steps
  return l








# l is the list of elements
l=[int(x)for x in input("enter numbers:").split()]
insertsort_l=insertsort(l)
print(insertsort_l)