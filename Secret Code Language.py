
s = input("Enter your word:")
p = list(s)
r = len(s)
if r == 2:
    p.reverse()
    print(p)
else:

    q = p.pop(0)
    p.append(q)
    p.insert(0, "z")
    p.insert(1, "x")
    p.insert(2, "y")
    z = ["f", "g", "h"]
    p.extend(z)
    print(p)






















