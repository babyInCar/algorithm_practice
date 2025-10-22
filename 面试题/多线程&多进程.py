

from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Process
import time

n = ThreadPoolExecutor(max_workers=5)


def handle_signal(signal_list):
    """
    :param signal_list:
    :return:
    """
    pass


def print_test(param_list):
    for param in param_list:
        time.sleep(1)
        print("hello world!", param)


def mul_process():
    param_list = [1,2,3,4,5]
    param_list2 = ["a","b","c","d","e"]
    p1 = Process(target=print_test, args=(param_list,))
    p2 = Process(target=print_test, args=(param_list2,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


def mul_thread():
    param_list = [1,2,3,4,5]
    param_list2 = ["a","b","c","d","e"]
    n.submit(print_test, param_list)
    n.submit(print_test, param_list2)


if __name__ == '__main__':
    # mul_process()

    mul_thread()