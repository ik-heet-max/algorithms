# Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»


# 1.
def is_prime(n):
    for mult in range(2, n):
        if n % mult == 0:
            return False
    return True


def prime(i):
    number = 1
    count = 0
    while count != i:
        number += 1
        if is_prime(number):
            count += 1
    return number


# "exercise2_lesson4.prime(20)"
# 100 loops, best of 5: 123 usec per loop
# ==============================
# "exercise2_lesson4.prime(40)"
# 100 loops, best of 5: 468 usec per loop
# ==============================
# "exercise2_lesson4.prime(60)"
# 100 loops, best of 5: 1.06 msec per loop
# ==============================
# "exercise2_lesson4.prime(80)"
# 100 loops, best of 5: 1.99 msec per loop
# ==============================
# "exercise2_lesson4.prime(100)"
# 100 loops, best of 5: 3.29 msec per loop
#   1    0.001    0.001    0.006    0.006 exercise2_lesson4.py:16(prime)
# 540    0.005    0.000    0.005    0.000 exercise2_lesson4.py:9(is_prime)
# ==============================
# "exercise2_lesson4.prime(200)"
# 100 loops, best of 5: 15.4 msec per loop
#    1    0.003    0.003    0.022    0.022 exercise2_lesson4.py:16(prime)
# 1222    0.019    0.000    0.019    0.000 exercise2_lesson4.py:9(is_prime)
# ==============================
# "exercise2_lesson4.prime(300)"
# 100 loops, best of 5: 38.4 msec per loop
#    1    0.005    0.005    0.054    0.054 exercise2_lesson4.py:16(prime)
# 1986    0.049    0.000    0.049    0.000 exercise2_lesson4.py:9(is_prime)
# ==============================
# "exercise2_lesson4.prime(400)"
# 100 loops, best of 5: 74.2 msec per loop
#    1    0.006    0.006    0.091    0.091 exercise2_lesson4.py:16(prime)
# 2740    0.085    0.000    0.085    0.000 exercise2_lesson4.py:9(is_prime)
# ==============================
# Зависимость похожа на параболическую, много раз вызывается функция is_prime

#=====================================================================================
# 2.
# Не додумался, как реализовать решето с возможностью нахождения произвольного i-того простого числа,
# поскольку оно подразумевает задание предела списка чисел.
# Поэтому как получилось :) 
def sieve(i):
    count = 1
    num = 2
    while count < i:
        num += 1
        rem = 2  # счетчик (для каждого числа) делителей, которые оставляют остаток
        for j in range(2, num):
            if num % j != 0:
                rem += 1
            if rem == num:
                count += 1
    return num


# "exercise2_2_lesson4.sieve(20)"
# 100 loops, best of 5: 544 usec per loop
# =======================================
# "exercise2_2_lesson4.sieve(40)"
# 100 loops, best of 5: 3.2 msec per loop
# =======================================
# "exercise2_2_lesson4.sieve(60)"
# 100 loops, best of 5: 8.52 msec per loop
# =======================================
# "exercise2_2_lesson4.sieve(80)"
# 100 loops, best of 5: 18.4 msec per loop
# =======================================
# "exercise2_2_lesson4.sieve(100)"
# 100 loops, best of 5: 32.9 msec per loop
# 1    0.036    0.036    0.036    0.036 exercise2_2_lesson4.py:4(sieve)
# =======================================
# "exercise2_2_lesson4.sieve(200)"
# 100 loops, best of 5: 188 msec per loop
# 1    0.195    0.195    0.195    0.195 exercise2_2_lesson4.py:4(sieve)
# =======================================
# "exercise2_2_lesson4.sieve(300)"
# 100 loops, best of 5: 505 msec per loop
# 1    0.544    0.544    0.544    0.544 exercise2_2_lesson4.py:4(sieve)
# =======================================
# "exercise2_2_lesson4.sieve(400)"
# 100 loops, best of 5: 980 msec per loop
# 1    1.042    1.042    1.042    1.042 exercise2_2_lesson4.py:4(sieve)
# =======================================
# Эта тоже похожа на параболу, но растет быстрее, то есть алгоритм медленнее,
# но функция одна-единственная, и стек не забивается.
# Первый вариант мне нравится больше