i1='MOTRAN'
i2=234
i3=234
print("TRUE") if len(i1)>20 else print("FALSE")
print("i2>i3") if i2>i3 else print("=") if(i2==i3) else print("<")

age = 25
is_student = False
has_discount_code = True
if (age < 18 or age > 65) and not is_student or has_discount_code:
  print("Discount applies!")

#if so sanh va khong lam gi
a = 33
b = 200
if b > a:
  pass          #câu lệnh giữ chỗ tránh báo lỗi(câu lệnh k lm j cả)
