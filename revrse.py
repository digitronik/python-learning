# Python program to reverse a given number

n = int(input("enter the number : "))
rev = 0
while(n>0):
    dig = n%10
    rev = rev*10+dig
    n = n//10
print "reverse of number is :", rev