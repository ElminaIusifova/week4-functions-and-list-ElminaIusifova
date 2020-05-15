list = [14, 12, 11, 14, 10, 12, 10, 7, 8, 9, 100]

# x = list.count("")
# index()
# remove()

def function():
    array =[]
    for i in list:
        if i not in array:
            array.append(i)
    return array

print(function())







