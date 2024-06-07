# parameters
def say_hello(name, emoji):
    print(f'helllooooo {name} {emoji}') # the name and the emoji here  are the parameters
# these types of parametrers are called as the positional parameters 

# arguments
say_hello("BuriBuri", "._. (:")
say_hello("Blob", "._. (:")
say_hello("Money", "._. (:") # these type of arguments are known as the positional arguments
# positional arguments are the arguments that require to be in a proper position

# keyword arguments 
say_hello(emoji = "._. (:", name = "BuriBuri")

def say_hello(name = 'Darth Vader', emoji = ":_:"):
    print(f'hellloooooo {name}{emoji}')
say_hello()
say_hello("Tommy")