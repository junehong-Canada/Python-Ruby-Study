import hello

print('main.py __name__:', __name__)

def add(a, b):
    return a + b

def mul(a, b):
    return a * b

if __name__ == '__main__': # if __name__ is __main__, entry point of program. 
    print(add(10, 20))
    print(mul(10, 20))
