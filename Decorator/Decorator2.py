import time
def runtime(func):
    def runtime_check():
        before =  time.time()
        print (before)
        func()
        after =  time.time()
        print (after)
        print ('run time is:', after - before)
    return runtime_check

@runtime
def my_function1():
    print ("hey")
my_function1()


@runtime
def my_function2(): 
    a = 0
    for i in range(100000):
        for j in range(100):
            a += i * j
    print (a)
my_function2()





        
