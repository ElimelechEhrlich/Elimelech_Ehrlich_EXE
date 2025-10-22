def make_multiplier(factor):
    def multiply(x):
       return (x * factor)
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)


print(double(5))   # Expected: 10
print(triple(5))   # Expected: 15
print(double(10))  # Expected: 20
print(triple(7))   # Expected: 21
print(triple(5))   # Expected: 15
