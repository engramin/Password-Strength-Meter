from random import *
mixchars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789"
randompass = "".join(choice(mixchars) for x in range(randint(8, 20)))
print("Your Random Password is: ", randompass)