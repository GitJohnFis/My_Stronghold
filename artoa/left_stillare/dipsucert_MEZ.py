
import time
from multiprocessing import Pool, cpu_count

def slow_square(n):
    total = 0
    for i in range(10_000_000):
        total += i* n
    return total

if __name__ == "__main__":

    numbers = list(range(14))

    start = time.perf_counter()
    singles = [slow_square(n) for n in numbers]
    print(f"Seq: {time.perf_counter() - start:.2f}s")

    print (f"Coers: {cpu_count()}")

    start = time.perf_counter()
    with Pool() as pool:
        multi = pool.map(slow_square, numbers)
    print(f"Par: {time.perf_counter() - start:.2f}s")