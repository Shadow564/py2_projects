test = {"red" : 4, "green" : 5, "blue" : 6}

print test["red"]
testiterate = []
for i in test:
  testiterate.append(i)
  print testiterate

key_wanted = 0
print testiterate[len(testiterate) - (key_wanted + 1)]
