from benchmark import perf
import numpy as np

DATA = np.random.rand(30_000_000)

with perf():
    mean = DATA.sum() / len(DATA)
    result = DATA - mean