#khoi tao
mytuple=('a','b',2)
newtuple='c','d',True,3
#khong the them hoac xoa phan tu trong tuple
print(len(mytuple))
tp1=("a",) #day la tuple 1 phan tu
tp2=("a") #day la str
#============them/xoa phan tu==================
tp3=list(tp1)
tp3.append("orange")
tp1=tuple(tp3)
del tp1 #xoa toan bo giu lieu
#======================giai nen============================
(chua,chub,so2)=mytuple
print(chua)
(chuc,*ptu)=newtuple
print(ptu)
#======================loop=================================
tp4=tuple()
for x in mytuple:
    tp4=x
for i in range(len(newtuple)):
    tp4[i]=i
i=0
while i<len(newtuple):
    i+=1
#=======================method===========================
tp5=(1,2,5,6,2,7,4,4,5,6,7,6)
x=tp5.count(5)  #x = so lan gia tri 5 xuat hien
y=tp5.index(5,3,8)  #y=vi tri dau tien ma gia tri 5 bat dau tu chi muc 3 ket thuc o 8