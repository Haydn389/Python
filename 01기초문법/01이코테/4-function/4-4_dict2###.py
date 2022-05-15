x={100:'hundred',False:0,3.5:[3.5,3.5]}
y= {'apple':5, 'grape':10, 'banana':7,'peach':3,'melon':2}
z=[1,1,5,5,7,8,6,6,8]
print(x)
print(x.items())
print(x.keys())
print(sorted(x))
print(sorted(y,key=lambda i:i[0]))
print(sorted(y.items(),key=lambda i:i[0]))
print(sorted(y.keys(),key=lambda i:i[0]))