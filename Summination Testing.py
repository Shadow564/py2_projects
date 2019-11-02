def summination():
    total = 0
    i = 0.0
    while True:
        total += ((i ^ 3) / ((i ^ 2) - i)) ^ i
        print total
        i += 1
        if i == 1000:
            break
        else: pass

summination()
# float('inf')
