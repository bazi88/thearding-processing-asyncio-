from time import sleep, perf_counter
from concurrent.futures import ThreadPoolExecutor

def task(id):
    print(f"Starting task {id}")
    sleep(1)
    return (f"Finished task {id}")

start = perf_counter()

# def main():
#     with ThreadPoolExecutor() as executor:
#         t1 = executor.submit(task, 1)
#         t2 = executor.submit(task, 2)

#         print(t1.result())
#         print(t2.result())
#     end = perf_counter()

#     print(f"Finished in {end - start} seconds")

def mainWithMap():
    with ThreadPoolExecutor() as executor:
        results = executor.map(task, [1,2])
        for result in results:
            print(result)

    end = perf_counter()

    print(f"Finished in {end - start} seconds")

if __name__ == '__main__':
    # main()
    mainWithMap()