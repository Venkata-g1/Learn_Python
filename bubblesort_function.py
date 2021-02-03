
def bubblesort(l):
  for j in range(len(l)-1):
    for i in range(len(l)-1):
      while (l[i]>l[i+1]):
        k=l[i]
        l[i]=l[i+1]
        l[i+1]=k
      #print(l) enable this to see stepwise sorting in bubblesort
  return l



# l is list that we are taking as input with space delimeter
l=[int(x) for x in input("enter numbers:").split()]
s=bubblesort(l)
print(s)
