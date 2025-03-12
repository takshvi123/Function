def add(a,d):
    sum=a+d
    return sum
def less(l,e):
    diff=l-e
    return diff
def multiply(m,u):
    product=m*u
    return product
def division(d,i):
    divide=d/i
    return divide
num1=int(input("Enter the FIRST NUMBER "))
num2=int(input("Enter the SECOND NUMBER "))
s=add(num1,num2)
print(f"The SUM of {num1} and {num2} is {s}.")

l=less(num1,num2)
print(f"The SUBTRACTION of {num1} and {num2} is {l}.")

m=multiply(num1,num2)
print(f"The MULTIPLICATION of {num1} and {num2} is {m}.")

d=division(num1,num2)
print(f"The DIVISION of {num1} and {num2} is {d}.")