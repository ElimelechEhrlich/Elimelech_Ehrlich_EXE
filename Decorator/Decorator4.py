def converts_str_to_uppercase(func):
    def converted(args):
        print (func(args))
        if isinstance(args,str):
            return func(args).upper()
    return converted


@converts_str_to_uppercase
def my_function(args):
    return (args)
print(my_function('eli'))