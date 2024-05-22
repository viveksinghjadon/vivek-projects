a=int(input("Enter the number="))
b=int(input("Enter the number="))
print("1.Addition")
print("2.Subtract")
print("3.Multiplication")
print("4.Division")
choice=input("Enter choice(1/2/3/4):")
if choice =="1":
    print(a+b)
elif choice=="2":
    print(a-b)
elif choice=="3":
    print(a*b)
elif choice=="4":
    print(a/b)
else:
    print("invalid sentex")