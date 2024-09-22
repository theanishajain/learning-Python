# scope or namespace and closure or  factory function
def chaicoder(num):
    def actual(x):
        return x**num
    return actual