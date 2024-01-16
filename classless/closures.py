#https://stackoverflow.com/questions/36636/what-is-a-closure

def outer(message):
    a = "Hello world, "
    def inner():        
        print(a + message)
    return inner


fnc = outer('Its casper here')
fnc()