def sum(num1, num2):
    return num1 + num2

# a function should do one thing really well.
# a function should return something.

total = sum(10, 5)
print(sum(10, total)) # or print(sum(10, sum(10, 5)))

def sum(num1, num2):
    def another_func(n1, n2):    
        return n1 + n2
    return another_func

total = sum(10, 20)
print(total(10, 20)) # or we can code as print(total)