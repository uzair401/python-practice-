#  Looping Example
import time

start_time = time.time()

for i in range(90):
    for j in range(123):
        print("0", end = " ")
    print("")
print(round(time.time() - start_time, 2))