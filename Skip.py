while True:
    l = []
    word = raw_input("Enter a word: ")
    for ele in word:
        l.append(ele)
    l = sorted(l)
    l = "".join(l)
    print l
