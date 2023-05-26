import time
import threading

def worker(num):
    for i in range(1000000):
        num = num + i

def single_thread():
    start = time.time()
    num = 0
    worker(num)
    end = time.time()
    print("Single Thread Time:", end-start)

def multi_thread():
    start = time.time()
    num1 = 0
    num2 = 0
    t1 = threading.Thread(target=worker, args=(num1,))
    t2 = threading.Thread(target=worker, args=(num2,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end = time.time()
    print("Multi Thread Time:", end-start)

if __name__ == "__main__":
    single_thread()
    multi_thread()
