def sorted_words(winter):
    dict = {}
    for line in winter:
    words = line.split()
        for word in words:
            lrt=len(word)
            if word not in dict:
                dict.setdefault(word,rt)
            else:
                dict[word].append(lrt)
        return dict

dict=sorted_words()
lst = []
for word,freq in dict.items():
    pair = (freq,word)
    lst.append(pair)
lst.sort(reverse=true)

print(lst)
