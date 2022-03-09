import multiprocessing as mp
from threading import Thread, Barrier
from time import time


def fib(n):
    a, b = 0, 1
    if n == 1:
        return a

    for _ in range(n - 2):
        a, b = b, a + b

    return b


def seq_fib(n, k):
    start = time()
    for _ in range(k):
        fib(n)
    return (time() - start) / k


def fib_barrier(n, barrier):
    fib(n)
    barrier.wait()


def thread_fib(n, k):
    start = time()
    barrier = Barrier(k + 1)
    for _ in range(k):
        Thread(target=fib_barrier, args=(n, barrier)).start()

    barrier.wait()

    return (time() - start) / k


def proc_fib(n, k):
    start = time()
    barrier = mp.Barrier(k + 1)
    for _ in range(k):
        mp.Process(target=fib_barrier, args=(n, barrier)).start()

    barrier.wait()

    return (time() - start) / k


if __name__ == "__main__":
    n, k = int(5e5), 10
    with open("artifacts/easy/easy.txt", "w") as f:
        f.writelines([
            f"Sync: {seq_fib(n, k): .3f}\n",
            f"Thread: {thread_fib(n, k): .3f}\n",
            f"Process: {proc_fib(n, k): .3f}"
        ])
