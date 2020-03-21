from random import choice
import time

a = [i for i in range(0, 100, 5)]

while 1:
    print(choice(a))
    time.sleep(1)