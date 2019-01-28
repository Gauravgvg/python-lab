#name:maitreyee 
#div:p batch:1
'''write a python program to convert seconds into days,hours,minutes and days'''
x=int(input('time in seconds '))
q1=x//86400
r1=x%86400
q2=r1//3600
r2=r1%3600
q3=r2//60
r3=r2//60
q4=r3
print(q1,q2,q3,q4)
