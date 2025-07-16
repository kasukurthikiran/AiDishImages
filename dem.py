import threading
import time
import requests

start = time.time()
def addition():
    print("[Addition] Task started")
    result = 10 + 5
    time.sleep(1)
    print("[Addition] Result:", result)

def subtraction():
    print("[Subtraction] Task started")
    result = 10 - 5
    time.sleep(1)
    print("[Subtraction] Result:", result)


def multiplication():
    print("[Multiplication] Task started")
    result = 10 * 5
    time.sleep(1)
    print("[Multiplication] Result:", result)

t1 = threading.Thread(target=addition)
t2 = threading.Thread(target=subtraction)
t3 = threading.Thread(target=multiplication)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print('time taken: ',round(time.time() - start,2))