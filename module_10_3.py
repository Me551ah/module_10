from threading import Thread, Lock
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            random_number = randint(50, 500)
            self.balance += random_number
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'\nПополнение: {random_number}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            random_number = randint(50, 500)
            print(f'\nЗапрос на {random_number}')
            if random_number <= self.balance:
                self.balance -= random_number
                print(f'\nСнятие: {random_number}. Баланс: {self.balance}')
            else:
                print(f'\nЗапрос отклонён, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)


bk = Bank()

thread1 = Thread(target=Bank.deposit, args=(bk,))
thread2 = Thread(target=Bank.take, args=(bk,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f'Итоговый баланс: {bk.balance}')