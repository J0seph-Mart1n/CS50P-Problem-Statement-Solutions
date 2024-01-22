x,y,z = map(str,input("Expression: ").split())
if y=="+":
    print(float(int(x)+int(z)))
elif y=="-":
    print(float(int(x)-int(z)))
elif y=="*":
    print(float(int(x)*int(z)))
elif y=="/" and z!='0':
    print(float(int(x)/int(z)))

