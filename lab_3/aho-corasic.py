import time


def calculate_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        print(func())
        return time.time() - start

    return wrapper


@calculate_time
def create_list():
    return [x for x in range(100000)]


print(create_list())
