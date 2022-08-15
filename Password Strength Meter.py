# Password Strength Meter

# 1-5 Characters --- Weak
# 6-9 Characters --- Fair
# 10-14 Characters --- Good
# >= Characters --- Strong

password=input("Type your Password: ")
if len(password) <=5:
    print('Your Password is Weak')
elif len(password) >=6 and len(password) <=9:
    print ('Your Password is Fair')
elif len(password) >=10 and len(password) <=14:
    print('Your Password is Good')
elif len(password) >=15:
    print('Your Password is Strong')