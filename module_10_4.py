from threading import Thread
from queue import Queue
from time import sleep
from random import randint


class Table:
    def __init__(self, number: int, guest: str = None) -> None:
        self.number = number
        self.guest = guest


class Guest(Thread):
    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name

    def run(self):
        random_time = randint(3, 10)
        sleep(random_time)


class Cafe:
    def __init__(self, *tables) -> None:
        """
        Принимает коллекцию столов
        :param tables: список столов (экземпляры класса Table).
        queue: очередь (объект класса Queue).
        """
        self.tables = list(tables)
        self.queue = Queue()

    def guest_arrival(self, *guests: Guest) -> None:
        """
        Принимает неограниченное количество гостей.
        Если есть свободный стол, то садит гостя за стол.
        Если свободных столов не осталось, то помещает гостя в очередь (queue).
        :param guests: Список гостей (экземпляры класса Guest - потоки).
        """
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f'{guest.name} садится за стол номер {table.number}')
                    break  # гость за столом, прекращаем поиск свободного стола
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self) -> None:
        """
        Имитирует обслуживание гостей.
        Обслуживание должно проходить пока очередь (queue) не пуста или хотя бы один стол занят.
        :return:
        """
        while not self.queue.empty() or any(table.guest for table in self.tables):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f'{table.guest.name} уходит')
                    table.guest = None
                    print(f'Стол номер {table.number} свободен')

                    if not self.queue.empty():
                        guest_name_from_the_queue = self.queue.get()
                        table.guest = guest_name_from_the_queue
                        guest_name_from_the_queue.start()
                        print(f'{guest_name_from_the_queue.name} из очереди '
                              f' садится за стол номер {table.number}')


if __name__ == '__main__':
    # Создание столов
    tables = [Table(number) for number in range(1, 6)]
    # Имена гостей
    guests_names = [
        'Дарья', 'Максим', 'Иван', 'Константин', 'Ирина', 'Эдуард',
        'Амалия', 'Кирилл', 'Нина', 'Николай', 'Евгений', 'Артём'
    ]
    # Создание гостей
    guests = [Guest(name) for name in guests_names]
    # Заполнение кафе столами
    cafe = Cafe(*tables)
    # Приём гостей
    cafe.guest_arrival(*guests)
    # Обслуживание гостей
    cafe.discuss_guests()