#мы могли заметить сходство map и select. 

# def select(f,col):
#     return[f(x) for x in col]

# def where(f,col):
#     return[x for x in col if f(x)]

# data=[1,2,3,5,8,15,23,38]
# res=select(int,data)
# print(res)
# res=where(lambda x: x%2==0,res)
# print(res)
# res=list(select(lambda x:(x,x**2),res))
# print(res)

# давайте упростим этот код

def where(f,col):
    return[x for x in col if f(x)]

data=[1,2,3,5,8,15,23,38]
res=map(int,data)
print(res)
res=where(lambda x: x%2==0,res)
print(res)
res=list(map(lambda x:(x,x**2),res))
print(res)

# мы сделали из селект мэп.по сути одно и тоже.просто селект прописали явно,а мэп в модулях