# score = 4
# att = 'good'
# if score > 9 and att =='good':
#     print("Hs gioi")
# elif score < 7 or att == 'good':
#     print("Hs kha")
# else:
#     print("Hs binh thuong")

a = float(input('he so cua x binh'))
b = float(input("he so cua x"))
c = float(input("he so tu do"))
delta = b**2 - 4*a*c
if delta > 0 :
    print("x1 =", (-b - delta**(1/2))/(2*a), "x2 =", (-b + delta**(1/2))/(2*a))
elif delta == 0 :
    print("x =" , -b/(2*a))
else: 
    print('vo nghiem')