f=open("ing.text","r")
file=f.read()
data=file.split()
i=0
count=0
name=''
while i<len(data):
    if "ing" in data[i]:

        name=name+data[i]
    
    
        count=count+1
    i=i+1
print(count,name)