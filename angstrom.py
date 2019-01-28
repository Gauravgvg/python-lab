#name: maitreyee chaudhari
#div:p #batch:p1
'''write a pytho programme to find that user entered number is an armstrong number'''
x=int(input('the number entered by the user '))
q1=x//10
r1=x%10
q2=q1//10
r2=q1%10
z=r1**3+q2**3+r2**3
if x==z:
  print('armstrong number')
else:
  print('not an armstrong number')
