# Написать функцию-декоратор для кеширования значений функции
#Написать функцию seq(n)
#n = 0 ....N
#(1 + n) ** n возвращает [x1, x2, x3, , , , xn]
#(**) с помощью декоратора-логгера создать лог функции (с замером времени выполнения функции)
import datetime
import time


def log_dec(func):
    def wrapper(arg):
        log_msg = f'{datetime.datetime.now():%d.%m.%y %H:%M:%S}'
        start = time.time_ns()
        res = func(arg)
        finish = time.time_ns()
        log_msg += f' {arg} = {res}, время: {finish - start} нс\n'
        with open('log_file.log', 'a', encoding='utf-8') as lf:
            lf.write(log_msg)
        return res
    return wrapper


def cache_dec(func):
    cache = {}

    def wrapper(arg):
        res = func(arg)
        key = arg
        if key not in cache:
            cache[key] = res
        print(cache)
        return res
    return wrapper


@log_dec
@cache_dec
def seq(n):
    res_list = [(1 + i) ** i for i in range(0, n + 1)]
    return res_list


def main():
    print(seq(15))
    print(seq(5))
    print(seq(2))
    print(seq(136))


main()