
import time
from multiprocessing import Pool, cpu_count

def slow_square(n):
    total = 0
    for i in range(10_000_000):
        total += i* n
    return total

if __name__ == "__main__":

    numbers = list(range(14)) #14 is the max number of processes on my machine, so I can see the difference between sequential and parallel execution

    start = time.perf_counter()
    single = [slow_square(n) for n in numbers]
    print(f"Seq: {time.perf_counter() - start:.2f}s")

    print (f"Cores: {cpu_count()}")

    start = time.perf_counter()
    with Pool() as pool:
        multi = pool.map(slow_square, numbers)
    print(f"Par: {time.perf_counter() - start:.2f}s")