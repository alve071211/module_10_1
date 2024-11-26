import time
from datetime import datetime
from nt import write
import os
from pprint import pprint
from time import sleep
import threading


def write_words(word_count, file_name):
    count_ = 0
    with open(file_name, 'a', encoding='utf-8') as file:

        while count_ < word_count:
            count_ += 1
            file.write(f'Какое-то слово № {count_}' + '\n')
            time.sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')


def write_words1(word_count, file_name):
    count_ = 0
    with open(file_name, 'a', encoding='utf-8') as file:
        time.sleep(0.1)
        while count_ < word_count:
            count_ += 1
            file.write(f'Какое-то слово № {count_}' + '\n')

time_start = datetime.now()

result1 = write_words(10, 'example1.txt')
result2 = write_words(30, 'example2.txt')
result3 = write_words(200, 'example3.txt')
result4 = write_words(100, 'example4.txt')


time_stop = datetime.now()
time_res = time_stop - time_start

print(f'Время работы функций {time_res}')

time2_start = datetime.now()

#thr_first = Thread(target=write_words, args= (10, 'example5.txt'))


thread1 = threading.Thread(target=write_words(10, 'example5.txt'))
thread2 = threading.Thread(target=write_words(30, 'example6.txt'))
thread3 = threading.Thread(target=write_words(200, 'example7.txt'))
thread4 = threading.Thread(target=write_words(100, 'example8.txt'))

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

time2_stop = datetime.now()
time2_res = time2_stop - time2_start

print(f'Время работы функций {time2_res}')


print(f'Использование Потоков быстрее функций на {time_res-time2_res} секунд')
