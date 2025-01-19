"""
Homegrown timing tools for function calls.
Does total time, best-of time, and best-of-totals time
"""
from time import time, process_time


def total(reps, func, *pargs, **kargs):
    """
    Total time to run func() reps times.
    Returns (total time, last result)
    """
    repslist = list(range(reps))
    start = time()
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = time() - start
    return elapsed, ret


def bestof(reps, func, *pargs, **kargs):
    """
    Quickest func() among reps rens.
    Returns (best time, last result)
    """
    best = 2 ** 32
    for i in range(reps):
        start = time()
        ret = func(*pargs, **kargs)
        elapsed = time() - start
        if elapsed < best: best = elapsed
    return best, ret


def bestoftotal(reps1, reps2, func, *pargs, **kargs):
    """
    Best of totals:
    (best of reps1 runs of (total of reps2 runs of func))
    """
    return bestof(reps1, total, reps2, func, *pargs, **kargs)

# start = process_time()
# print(total(1000, pow, 2, 1000))
# print(total(1000, str.upper, 'spam'))
# print(bestof(1000, str.upper, 'spam'))
# print(bestoftotal(50, 1000, str.upper, 'spam'))
# print(min(total(10000, str.upper, 'spam') for i in range(500)))
# end = process_time() - start
# print(end)
