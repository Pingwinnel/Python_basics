x=input()
y=x.find('h')
z=x.rfind('h')
print(x[:y]+x[z+1:])
