"""
Lesson 6 — GIL: threads vs asyncio vs multiprocessing
Run:  python "Python/Problems/lesson06_gil_concurrency.py"
Goal: MEASURE that threads DON'T speed up CPU-bound work (GIL), but DO help
      I/O-bound work; and that multiprocessing DOES speed up CPU-bound work.
"""
import time
import threading
import multiprocessing
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


# ---------------------------------------------------------------------------
# CPU-BOUND task: pure-Python number crunching (the GIL bites here).
# ---------------------------------------------------------------------------
def cpu_task(n):
    total = 0
    for i in range(n):
        total += i * i
    return total

N = 5_000_000
WORKERS = 4


def time_it(label, fn):
    start = time.perf_counter()
    fn()
    print(f"   {label:<28} {time.perf_counter() - start:.3f}s")


def cpu_sequential():
    for _ in range(WORKERS):
        cpu_task(N)

def cpu_threads():
    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        list(ex.map(cpu_task, [N] * WORKERS))

def cpu_processes():
    with ProcessPoolExecutor(max_workers=WORKERS) as ex:
        list(ex.map(cpu_task, [N] * WORKERS))


# ---------------------------------------------------------------------------
# I/O-BOUND task: sleeping simulates waiting on network/API (GIL released).
# ---------------------------------------------------------------------------
def io_task(_):
    time.sleep(0.5)          # pretend this is an API/LLM call we wait on
    return "done"

def io_sequential():
    for _ in range(WORKERS):
        io_task(None)

def io_threads():
    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        list(ex.map(io_task, range(WORKERS)))


def main():
    print("CPU-BOUND (expect: threads ~= sequential because of GIL;")
    print("           processes FASTER because separate interpreters):")
    time_it("cpu sequential", cpu_sequential)
    time_it("cpu threads", cpu_threads)        # PREDICT vs sequential
    time_it("cpu processes", cpu_processes)    # PREDICT vs sequential

    print("\nI/O-BOUND (expect: threads MUCH faster; waits overlap):")
    time_it("io sequential", io_sequential)    # ~4 * 0.5 = 2.0s
    time_it("io threads", io_threads)          # PREDICT: ~0.5s? why?


if __name__ == "__main__":     # REQUIRED for multiprocessing on Windows
    main()
