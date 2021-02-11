x=["Srikanth","Rakesh","Pavan","Giri","Sudheer","Giri","Suresh","Venkat"]

for i in x:
      if i[0]=="S":
            print(i) 

lit1=[i for i in x if i[0]=="S"]
print(lit1)


c={'Srikanth':23,'Pavan':21,'Rakesh':22,'Giri':26,'Suresh':22,'Sudheer':50}
for i in c:
      if i[0]=='S':
            c[i]=100
print(c)
            
            

