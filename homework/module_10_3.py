import threading
import time
import random


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            money = (random.randint(50, 500))
            self.balance += money
            print(f'Пополнение: {money}. Текущий баланс: {self.balance}')
            time.sleep(0.001)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)



    def take(self):
        for _ in range(100):
            money = (random.randint(50, 500))
            print(f'Запрос на {money}')
            time.sleep(0.001)
            if money <= self.balance:
                self.balance -= money
                print(f'Снятие: {money}. Текущий баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)

bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')