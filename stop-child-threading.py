from threading import Thread, Event
from time import sleep, perf_counter

def task(event: Event):
    for i in range(1, 10):
        print(f"Start with task {i}")
        sleep(1)

        if event.is_set():
            print(f"Stop with task {i}")
            break
        else:
            print(f"Continue with task {i}")
    else:
        print("Stop child thread")
def main() -> None:

    event = Event()
    thread = Thread(target=task, args=(event,))
    
    # start the thread
    thread.start()

    # suspend  the thread after 3 seconds
    sleep(3)

    # stop the child thread
    event.set()    
   

if __name__ == '__main__':
    main()