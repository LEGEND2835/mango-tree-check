n=int(input("Matrix Dimension: "))
t=int(input("Enter tree number: "))
if t<=n or (t-1)%n==0 or t%n==0:
    print("Yes")
else:
    print("No")
