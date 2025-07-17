a=int(input("enter the number a"))
b=int(input("enter the number b"))
c=int(input("enter the number c"))

if a>=b and a>=c:
    print("a is greater no.")
elif b>=a and b>=c:
    print("b is greater no.")
elif c>=a and c>=b:
    print("c is greater no.")
elif a==b or b==c or c==a:
    print("both are same ")
else:
    print("invalid no.")