#https://stackoverflow.com/questions/36636/what-is-a-closure

def outer():
    a = "Hello world"
    def inner():        
        print(a)
    return inner


fnc = outer()
fnc()