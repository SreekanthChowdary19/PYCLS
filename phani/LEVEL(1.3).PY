
#WAP CREATE 3*3 MATRIX USING PYTHON.TAKE ALL THE ELEMENTS FROM THE USER.
#AND ALSO PRINT THE SUM OF DIAGONAL ELEMENTS FROM CREATED MATRIX.






R=int(input("enter the number of rows:"))
c=int(input("enter the number of rows:"))
matrix=[]
d1=0
d2=0
print("enter the entires rowwise:")
for i in range(R):
    a=[]
    for j in range(c):
        a.append(int(input()))
    matrix.append(a)
for i in range(R):
    for j in range(c):
        print(matrix[i][j],end=" ")
    print()
for i in range(R):
    for j in range(c):
        if i==j:
            d1+=matrix[i][j]
        if i+j==R-1:
            d2+=matrix[i][j]
print(d1)
print(d2)
