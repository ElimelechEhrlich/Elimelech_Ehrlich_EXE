x = 10

def show():
    global x
    x = 5
    print("Inside:", x)

show()
print("Outside:", x)

