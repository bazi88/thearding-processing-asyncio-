from threading import Thread
from time import sleep, perf_counter
from concurrent.futures import ThreadPoolExecutor

number = 0
def counter(val: int) -> int:
    global number
    
    local_counter = number
    local_counter += val

    number = local_counter
    return local_counter

def main() -> None:

    with ThreadPoolExecutor() as executor:
        results = executor.map(counter, [10,20,30])
        for result in results:
            print(f"Number after counter is {result}")
           
if __name__ == '__main__':
    main()