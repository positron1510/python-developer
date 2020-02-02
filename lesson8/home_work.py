import time
import os
import psutil


def time_and_memory(f):
    def wrapper(*args, **kwargs):
        start = time.time()

        proc = psutil.Process(os.getpid())
        print('Memory start: {}'.format(str(proc.memory_info().rss / 1000000)))

        f(*args, **kwargs)

        proc = psutil.Process(os.getpid())
        print('Memory finish: {}'.format(str(proc.memory_info().rss / 1000000)))

        print("Total time: {}".format(time.time() - start))
    return wrapper


@time_and_memory
def make_list(n):
    print('Making list..')
    return [x for x in range(n + 1)]


@time_and_memory
def make_generator(n):
    print('Making generator..')
    return (x for x in range(n + 1))


N = 1000000

make_list(N)
print()
make_generator(N)