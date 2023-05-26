import time
import multiprocessing
def task(n):
    while n:
        n -= 1

if __name__ == "__main__":
    start = time.time()
    t1 = multiprocessing.Process(target=task, args=[100000000])
    t2 = multiprocessing.Process(target=task, args=[100000000])
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print(time.time() - start)
