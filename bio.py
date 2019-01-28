#Name:Gaurav Giri
#Batch:P      #Roll no.:21
d={}
x=int(input('no. of students: '))

for i in range(0,x):    
    n=str(input('Name of student: '))
    g=int(input('Gr. No.  '))
    b=str(input('Batch: '))
    d[g]=(n,b)
    print(d)
