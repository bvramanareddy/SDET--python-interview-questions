def swap_values(a, b):
    a,b = b,a
    return  a, b
a=10
b=20
print("Values before swapping for a, b are ", a, b)
print("Values swapped After for a, b are ", swap_values(a,b))
