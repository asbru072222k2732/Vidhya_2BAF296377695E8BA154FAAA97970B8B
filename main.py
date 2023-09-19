#program to find a factorial of a given number
def factorial(n):
  if n==0 or n==1:
    return 1;
  else:
    return n*factorial(n-1)
num=8
result=factorial(num)
print("Factorial of {} is {} .".format(num,result))

