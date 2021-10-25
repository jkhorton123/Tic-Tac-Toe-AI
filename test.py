l = [1, 3]
for i in range(4):
    if not i in l:
        l.append(i)

a = (0, 2)
b = (0, 1, 2)
if set(a).issubset(b):
    print("yes")

l = [2, 3]

lnew = l.copy()
lnew.append(1)
print(lnew)
                    

