def isprime(n):
    if(n==1 or n==0 ):
        print(n," is not a prime number")
    elif(n<0):
        print("please enter positive interger")
    else:
        
      for i in range(2,n):
        if (n%i==0):
          print(n," is not a prime number")
          break
      else:
        print(n," is a prime number")



n=int(input("enter number to check prime:"))
isprime(n)