name = "Tom"

def greet():
    global name
    name = "Ben"
    print("Hi", name)

greet()
print ('Bye', name)


# added 'global' on the variable
