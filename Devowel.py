def devowel(word):
    vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
    neword = []
    for ele in word:
        vowelless = True
        for vowel in vowels:
            if ele == vowel:
                vowelless = False
            else: pass
        if vowelless == True:
            neword.append(ele)
        else: pass
    return "".join(neword)
            
#yeet

while True:
    buffer = raw_input("Enter: ")
    print devowel(buffer)
