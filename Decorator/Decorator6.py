def authentication_Check(func):
    def user_permission(**kwargs):
        if kwargs['admin']:
            print ('User authorized to run the function')
            func(**kwargs)
        else:
            print ('User is not authorized!')
    return user_permission

@authentication_Check
def my_function1(**user):
     print ('ok')
my_function1(name = 'eli', admin = False)










