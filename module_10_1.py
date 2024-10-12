from threading import Thread
from time import sleep, time


def ite_words(word_count: int, file_name: str) -> None:
    with open(file_name, 'w', encoding='utf-8') as file:
        for word in range(1, word_count + 1):
            file.write(f"Какое-то слово №{word}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


if __name__ == '__main__':

    start_time1 = time()


    ite_words(10, 'example1.txt')
    ite_words(30, 'example2.txt')
    ite_words(200, 'example3.txt')
    ite_words(100, 'example4.txt')


    end_time1 = time()
    execution_time1 = end_time1 - start_time1
    print(f"Время работы 1-го потока {execution_time1:.2f}")


    start_time2 = time()

    thread1 = Thread(target=ite_words, args=(10, 'example5.txt'))
    thread2 = Thread(target=ite_words, args=(30, 'example6.txt'))
    thread3 = Thread(target=ite_words, args=(200, 'example7.txt'))
    thread4 = Thread(target=ite_words, args=(100, 'example8.txt'))

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()

    end_time2 = time()
    execution_time2 = end_time2 - start_time2
    print(f"Время работы 4-х потоков {execution_time2:.2f}")