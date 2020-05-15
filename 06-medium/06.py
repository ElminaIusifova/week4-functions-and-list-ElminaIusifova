c1 = ["white", "green", "red", "black", "yellow", "maroon", "grey"]
c2 = ["orange", "yellow", "maroon", "violet", "blue", "red", "purple"]
repeat = []

def superFunction():
    for i in c1:
        if i in c2:
         repeat.append(i)
    return repeat

print(superFunction())
