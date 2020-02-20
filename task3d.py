def character_word_count(stream):
    hist = {}
    for line in stream:
    words = line.split()
        for word in words:
            lenval=len(word)
            if word not in hist:
                hist.setdefault(word,lenval)
            else:
                hist[word].append(lenval)
        return hist

hist=sorted_words()
print(hist)
