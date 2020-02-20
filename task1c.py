def ctiv():
    count=0
    fin=open("Trail.csv", 'r')
    for line in fin:
        words=line.split(",")
        c=words[12]
        d=words[15]
        e=words[23]
        f=words[25]
        if d == 'Active':
            count = count +1
            print("status" + count)
            continue
        elif c == 'Yes'
            count1 = count1 +1    
            print("lightning Roads are:" + count1)
            continue
        elif e == 'Yes' and f == 'Yes'
            count2 = count2 +1
            print("walking and biking  Roads are:" + count2)

result=ctiv()
