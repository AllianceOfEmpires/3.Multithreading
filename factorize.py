﻿from concurrent.futures import ThreadPoolExecutor
from multiprocessing import cpu_count
from time import time

result_factorize = []


def factorize(number: int) -> list:
    factors = []
    for inner_number in range(1, number + 1):
        if number % inner_number == 0:
            factors.append(inner_number)
    return factors


def process_factorize(*numbers: list) -> list:
    result = []
    with ThreadPoolExecutor(max_workers=cpu_count()) as executor:
        factorize_result = list(executor.map(factorize, numbers))
        # for l in factorize_result:
        #     result += l
        # return list(set(result))

        return factorize_result


if __name__ == '__main__':
    start_time = time()
    # print(process_factorize([1, 2, 4, 5, 8, 1000222]))
    print(process_factorize(128, 256, 10651060))
    end_time = time()
    print(end_time - start_time)
