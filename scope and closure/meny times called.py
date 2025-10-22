def meny_times_called():
    count = 0
    def one_time():
        nonlocal count
        count += 1
        print (f'This function was called {count} times.')
    return one_time

called_function = meny_times_called()
called_function1 = meny_times_called()




