def count_func_called(func):
    count = 0
    def func_called():
        func()
        nonlocal count
        count += 1
        print ('function called', count, 'times')
    return func_called

@count_func_called
def my_function():
    print ('hey!')
my_function()
my_function()
my_function()
my_function()
my_function()
my_function()
my_function()
my_function()
my_function()
my_function()
