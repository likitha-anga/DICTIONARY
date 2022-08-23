"MISSISSIPPI"
# {'M':1,'I':4,'S':4,'P':2}
a={}
for i in "MISSISSIPPI":
    a[i]=a.get(i,0)+1
print(a)
