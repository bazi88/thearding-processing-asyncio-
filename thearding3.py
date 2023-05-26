from threading import Thread
from time import sleep, perf_counter
from pathlib import Path


def replace(filename, sub_string, new_string):
    print(f"Open file name {filename}")
    with Path(__file__).with_name(filename).open(filename, "r") as f:
        content = f.read()

    content = content.replace(sub_string, new_string)

    with  Path(__file__).with_name(filename).open(filename, "w") as f:
        f.write(content)

def main():
    filenames = [
        'temp/test1.txt',
        'temp/test2.txt',
        'temp/test3.txt',
        'temp/test4.txt',
        'temp/test5.txt',
        'temp/test6.txt',
        'temp/test7.txt',
        'temp/test8.txt',
        'temp/test9.txt',
        'temp/test10.txt',
    ]

    start_time = perf_counter()
    theard = [Thread(target=replace, args=(filename, "id" , "ids" )) for filename in filenames]
    for thread in theard:
        thread.start()
    
    for thread in theard:
            thread.join()

    end_time = perf_counter()
    print(end_time - start_time)

if __name__ == "__main__":
    import os
    main()