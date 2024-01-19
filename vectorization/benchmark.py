import timeit
from contextlib import contextmanager

@contextmanager
def timing_context():
    start_time = timeit.default_timer()
    yield
    end_time = timeit.default_timer()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time} seconds")