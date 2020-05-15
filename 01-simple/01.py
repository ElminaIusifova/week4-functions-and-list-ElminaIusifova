
def myFunction():
    array = []
    n = 0
    while n < 5:
      x = int(input("Enter a number: "))
      n+=1
      array.append(x**2)
    return array


print(myFunction())

