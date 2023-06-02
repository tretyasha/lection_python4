# функция filter по сути говорящая,она у нас фильтрует какие-то значения.на вход принимает два аргумента.это сама функция и объект и функция filter будет возвращать только те элементы объекта для которых вызов функции которой передали вернула значения true 

# data=[15,65,9,36,175] #попробуем применить эту функцию и сделать выборку,выберем числа которые заканчиваются на 5
# res=list(filter(lambda x:x%10==5, data))
# print(res)

# #  "d:/lection4 python/lection_python4/filtr.py"
# [15, 65, 175]
# PS D:\lection4 python\lection_python4> 
# выводятся только те элементы,которые заканчиваются на 5

# функция res похожа на функцию map
# попробуем упростить немного наш код.я здесь расписал нашу фунцию filter

# def filter(f,col): # def where(f,col): увидим что def filter +- прописаны также }удалим
#     return[x for x in col if f(x)]                                              }удалим

# data=[1,2,3,5,8,15,23,38]
# res=map(int,data)
# print(res)
# res=filter(lambda x:x%2==0,res)# res=where изменим на filter(lambda x:x%2==0,res)
# print(res)
# res=list(map(lambda x:(x, x**2),res))
# print(res)

# запустим и увидим,что у нас все также вводится 
# <filter object at 0x00000208EE46BEB0>
# [(2, 4), (8, 64), (38, 1444)]
# PS D:\lection4 python\lection_python4> 
# удалим лишние print
data=[1,2,3,5,8,15,23,38]
res=map(int,data)
res=filter(lambda x:x%2==0,res)
res=list(map(lambda x:(x, x**2),res))
print(res)

# для начала мы написали обычнцю функцию через простой цикл 
# далее мы это преобразовали в виде отдельных функций
# после изучили функцию map
# потом изучили функцию filter
# получился простой,красивый и короткий код

