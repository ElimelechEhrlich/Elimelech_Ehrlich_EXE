def my_decoratot(func):
    def print_status():
        print ("Start function")
        func()
        print ("End function")
    return print_status

@my_decoratot
def my_function():
    print ('hey! from my_function')
my_function()
