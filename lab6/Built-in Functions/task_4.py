import math
import time

long_sqrt = lambda delay, num: (
    time.sleep(delay / 1000), math.sqrt(num)
)[1]


num = int(input())
delay = int(input())

print(long_sqrt(delay, num))


