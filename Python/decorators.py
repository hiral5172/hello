def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")
# Take function f and add another function named wrapper
# add functionality

def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")
    return wrapper
    
@announce # this is decorators
def hello():
    print("Hello world")
hello()
"""
Output:
About to run the function...
Hello world
Done with the function.
"""