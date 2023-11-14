try:
    print("++++++++++++++++++++++++++++++++++++++")
    Sentence = input("Type some sentence: ")
    Senlist = Sentence.split()
    print("++++++++++++++++++++++++++++++++++++++")
    print(f"numbers of word are: {len(Senlist)}")
    
    sameword = list()
    
    for data in Senlist:
        number = Senlist.count(data)
    if number > 1:
        sameword.append(data)

    sameword2 = set(sameword)
    print(f"There are {len(sameword2)} sameword, It's have {' '.join(str(data) for data in sameword2)}")
    
    fill_list = list()
    for data in Senlist:
        number = Senlist.count(data)
        if number > 1 and not fill_list.count(data) > 0 :
            fill_list.append(data)
            print(f"The word {data} have same {number} words")

except Exception:
    pass