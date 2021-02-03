#binary search function definition
def binarysearch(l,n):
  start=0
  end=len(l)-1
  while(start<=end):
    mid=(start+end)//2
    if l[mid]==n:
      return mid
    elif l[mid]<n:
      start=mid+1
    else:
      end=mid-1
  return -1




# l is list here
l=[int(x)for x in input("enter numbers:").split()]
n=int(input("enter number to be searched:"))
s=binarysearch(l,n)# function calling
print(s)