def unique_words(uni):
     lst={}
     for line in uni:
        words=line.split()
        for word in words:
            if word in lst:
               dt[word] = lst[word] + 1
            else:
               lst[word] = 1
        return lst

lst1=unique_words()
dt=[]
for word,freq in lst1.items():
    pair = (freq,word)
    dt.append(pair)
print(dt)
