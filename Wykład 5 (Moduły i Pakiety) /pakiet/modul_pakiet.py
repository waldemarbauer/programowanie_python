pakiet_var = 10

pakiet_list = 10

def add(a,b, c = None):
    if c is None:
        return a+b
    else:
        return a + b + c
