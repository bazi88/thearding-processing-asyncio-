from threading import Thread
from time import sleep, perf_counter

def task(id):
    print(f"Start Work {id}")
    sleep(1)
    print(f"End Work {id}")

start_time = perf_counter()

theard = []
for i in range(1,11):
    t = Thread(target=task, args=(i,))
    theard.append(t)
    t.start()

for t in theard:
    t.join()

end_time = perf_counter()

print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')


