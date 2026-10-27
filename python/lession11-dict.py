#co thu tu, duoc thay doi va khong trung lap(cac value co cung key thi value sau se ghi de len value truoc)
d1={"brand":"Ford","model":"Mustang","year":1964}
d2={"brand" : "Ford",
    "electric":False,
    "year":1964,
    "colors":["red","green","blue"]
    }
print(d2["colors"][1])
d3=d1.get("model")
d3=d1.keys()
d1["brand"] = "laly"
d4=d2.values()
d5=d2.items()
if "model" in d1:
    d6=d1["model"]
#=====================add=========================
d1.update({"year":2020,"age":60})
#========================remove==========================
d1.pop("model")
d2.popitem()        #remove item last
d1.clear()
del d1
#=========================loop==========================
for x in d2:
    d11=d2[x]
for x in d2.values():
    d12=x
for x in d2.keys():
    d13=x
for x,y in d2.items():
    d14={x:y}
#=============================copy==========================
d6=d14.copy()
#d6=dict(d14)
#====================dict nested=============================
d7={
    "information_1":{
            "name":"Mo",
            "age":19
    },
    "information_2":{
        "name":"Ngoc",
        "age":18
    },
    "information_3":{
        "name":"Vui",
        "age":25
    }
}

car_1={
    "name":"vmw",
    "color":"black"
}
car_2={
    "name":"mec",
    "color":"white"
}
d8={
    "car_1":car_1,
    "car_2":car_2
}
#print(d8["car_1"]["name"])
for x , obj in d7.items():
    print(x)
    for y in obj:
        print(y," : ",obj[y])
#++++++++++++++++++++++phuong phap tu dien++++++++++++++++++++++++++++
"""
clear()
copy()
fromkeys()              #tra ve 1 dict voi cac key va value duoc chi dinh
    x=("mot","hai")
    y=1
    d1.fromkeys(x,y)
get()
items()
keys()
pop()
popitem()
setdefault()    #x= mustang , vì model tồn tại trong dict car , mà phương pháp này không thể ghi đè lên model gốc ; nếu như trong dict car không có key model thì phương pháp này sẽ ghi thêm key với value đc chỉ định vào car và khi này x = value đc chỉ ddinhj
    car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }

    x = car.setdefault("model", "Bronco")

    print(x)
update()
values()
"""