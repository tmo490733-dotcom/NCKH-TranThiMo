i = 1
while i < 6 and i>0:
  print(i)
  i += 1

#dừng hẳn thuật toán
while i < 6 :
  print(i)
  if i == 3:
    break
  i += 1

#bỏ qua vòng lặp đấy 
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)