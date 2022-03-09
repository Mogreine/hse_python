import concurrent.futures
import logging
import math
import multiprocessing as mp
import os

from time import time

from functools import partial

import pandas as pd


def integrate(f, a, b, n_iter=1000):
    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step
    return acc


def rec_internal(x, f, step):
    logger.info(f"x: {x}")
    return f(x) * step


def integrate_thread(f, a, b, n_iter=10000, n_jobs=1):
    step = (b - a) / n_iter
    args = [a + i * step for i in range(n_iter)]

    with concurrent.futures.ThreadPoolExecutor(max_workers=n_jobs) as executor:
        results = executor.map(partial(rec_internal, f=f, step=step), args)

    return sum(results)


def integrate_proc(f, a, b, n_iter=10000, n_jobs=1):
    step = (b - a) / n_iter
    args = [(a + i * step,) for i in range(n_iter)]

    with mp.Pool(processes=n_jobs) as pool:
        results = pool.starmap(partial(rec_internal, f=f, step=step), args)

    return sum(results)


def time_func(f, k, *args, **kwargs):
    start = time()
    for _ in range(k):
        f(*args, **kwargs)

    return (time() - start) / k


if __name__ == "__main__":
    n_iter = int(1e4)
    n_calls = 1

    logging.basicConfig(filename=os.path.join('.', 'artifacts', 'medium', f'log.txt'),
                        level=logging.INFO,
                        format="%(asctime)s;%(levelname)s;%(message)s")
    logger = logging.getLogger(os.path.basename(__file__))

    thread_res = [
        time_func(integrate_thread, n_calls, math.cos, 0, math.pi / 2, n_iter, n_jobs=n_jobs) for n_jobs in range(1, 9)
    ]
    proc_res = [
        time_func(integrate_proc, n_calls, math.cos, 0, math.pi / 2, n_iter, n_jobs=n_jobs) for n_jobs in range(1, 9)
    ]

    df = pd.DataFrame(
        {
            "n_jobs": range(1, 9),
            "thread": thread_res,
            "process": proc_res,
        }
    )

    df.to_csv("artifacts/medium/res.csv", index=False)
