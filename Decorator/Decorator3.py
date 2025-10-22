def prints_arguments_passed(func):
    def print_arguments_passed(*args):
        print (*args)
        func(*args)
    return print_arguments_passed

@prints_arguments_passed
def my_function(*args):
    return ('hey', args)
my_function('eli', 'ehrlich')

    