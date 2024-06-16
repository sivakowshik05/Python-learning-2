# non local is a part of a parent local , it is not a global variable
def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:" , x)

    inner()
    print("outer" , x) # here the reult will be inner: nonlocal
                       #                        outer: nonlocal      

outer

def outer():
    x = "local"
    def inner():
        x = "nonlocal" # here the nonlocal x is cleared for to see a change in the result
        print("inner:" , x)

    inner()
    print("outer" , x) # here the result will be as inner: nonlocal
                       #                            outer: local                     

outer