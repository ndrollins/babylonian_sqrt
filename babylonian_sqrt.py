number = int(input("Enter a number to square root: "))

def Square_Root():
    x = 1
    for i in range(100):
        x = (x + number / x) / 2
        sqrt = x
    print(sqrt)

Square_Root()
