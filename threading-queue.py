from threading import Thread
from queue import Queue, Empty
from time import sleep

def producer(q: Queue):
    for i in range(1,11):
        print(f"Put {i} in queue")
        q.put(i)
        sleep(1)

def consumer(q: Queue):
    while True:
        try:
            item = q.get()
        except Empty:
            print("Cannot get from queue")
        else:
            print(f"Get {item} from queue")
            sleep(2)
            
def main():
    q = Queue(maxsize=10)
    t1 = Thread(target=producer, args=(q,))
    t1.start()

    t2 = Thread(target=consumer, args=(q,), daemon=True)
    t2.start()

    t1.join()

    q.join()

if __name__ == '__main__':
    main()