#k thức tự , k thay đổi * , k lập chỉ mục , k trùng lặp
myset={"apple","banana","cherry"} #k thu tu , k dc trung lap ,khong the thay doi cac muc nhung duoc them/xoa
thisset={"apple","banana",True,1} #True & 1 dc coi la cung gia tri
#=============================add & remove==========================
thisset.add("orange")
myset.update(thisset)
thisset.remove("apple")  #apple k ton tai trong thisset thi se loi
thisset.discard("banana") #k bao loi
thisset.pop()  #xoa ngau nhien
thisset.claer()  #lm trong tap
del thisset  #xoa tap
#==================loop======================================
s1=set()
for x in myset:
    s1+=x
#======================join==================================
s1={"s",True}
s2={0,1,3}
st=("banana" , False)
st1={0,"False","sslab"}
t1=("fruit","cake")
s3=s1.union(s2,t1)   #kết hợp nhiều bộ dữ liệu
#s3=s1|s2               #kết hợp nhiều set
s1.update(s2)           #insert this set into that set
s4=s2.intersection(st)  #keep duplicate items
#s4=s2&st /NO             
s5=st.difference(s2)    #st\s2 (ap dụng nhiều bộ dữ liệu)
#s5=st-s2   /NO
s2.difference_update(s2)        #keep the item st no in s2 and change the value of st
s6=st.symmetric_difference(st1)     #keep the item no in st&&st1
#s6=st ^ st1
st.symmetric_difference_updete(st1) 
#=============================frozenset============================
s7= frozenset({"apple","banana",True,20})
#copy()
#difference()   "-"
#intersection()   "&"
#isdisjoint()       //does this set any items in common with that set
#issubset()     "<=/<"
#issuperset()   ">=/>"
#symmetric_difference()     "^"
#union()            "|"

