from threading import Thread, Event
from time import sleep, perf_counter

def task(event: Event, id):
    print(f'Thread {id} started. Waiting for the signal....')
    event.wait()
    print(f'Received signal. The thread {id} was completed.')

def main():
    event = Event()
    t1 = Thread(target=task, args=(event, 1))
    t2 = Thread(target=task, args=(event, 2))

    t1.start()
    t2.start()

    print('Blocking the main thread for 3 seconds...')
    sleep(3) 
    event.set()


if __name__ == "__main__":
    main()
    