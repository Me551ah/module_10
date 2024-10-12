import multiprocessing
import time


def read_info(name: str) -> None:
    """Считывает файл построчно и добавляет строки в список"""
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            all_data.append(line.strip())
            if not line:
                break


# создаем список файлов (в нашем случае они находятся в той же папке, что и наш проект)

file_names = [f'./file {i}.txt' for i in range(1, 5)]

# линейно вызываем функцию read_info с каждым файлом из списка file_list
# замеряем и выводим время работы

start_time = time.time()
for file_name in file_names:
    read_info(file_name)
end_time = time.time()
res = end_time - start_time
print(f'Время выполнения {res:.2f} секунд(ы)') # 13 секунд при линейном решении

# вызываем функцию read_info с каждым файлом из списка file_list используя многопроцессный подход
# поскольку мы заранее знаем, что в file_list у нас название 4-х файлов, то запустим 4 процесса
# замеряем время работы

if __name__ == '__main__':
    start_time = time.time()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, file_names)
    end_time = time.time()
    res = end_time - start_time
    print(f'Время выполнения {res:.2f} секунд(ы)') # 7 секунд при многопоточном решении

