def Active():
    lst=[]
    count=0
    fin=open('Trails.csv')  
    for line in fin:
        words=line.split(",")
        c=words[10]
        if 'INST_YEAR' not in words[10]:
            if c>2000:
                lst.append(c)
                count=count+1
    return lst
result=Active()
print(result)
