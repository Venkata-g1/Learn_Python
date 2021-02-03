
def merge(l1,l2):
  count=0
  i=0
  while (i<=len(l1)-1):
    if(l1[i]<=l2[count]):
      l3.append(l1[i])
      i=i+1
    else:
      l3.append(l2[count])
      count=count+1
  return l3





# l1 is list1 and l2 is list2
l1=[int(x)for x in input().split()]
l2=[int(x)for x in input().split()]
l3=list()
s=merge(l1,l2)
print(s)


# If lists are not sorted then combine those 2 lists and perform bubble sort or selection sort or any sorting algorithm