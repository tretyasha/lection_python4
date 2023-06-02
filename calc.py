# def calk1(a):
#     return a+a

# def calk2(a):
#     return a*a

# def math(op, x):
#     print(op(x))

# math(calk2,5)

# мы передаем в функцию math функцию кальк 2.наша переменная op имеет ссылку на calc2 и потом мы ее просто вызываем и выводим на экран.тоже самое можно делать с несколькими переменными

def calk1(a,b):
    return a+b

def calk2(a,b):
    return a*b

def math(op, x, y):
    print(op(x,y))

math(calk1,5,45)

# если напишем math(calk1,5,45) то он сложит,если math(calk2,5,45) то перемножит