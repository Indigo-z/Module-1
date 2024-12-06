import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = str(name)
        self.power = int(power)

    def days_word(self, days):
        if days % 10 == 1 or days % 100 == 11:
            return 'день'
        elif 2 <= days % 10 <= 4 and not (12 <= days % 100 <= 14):
            return 'дня'
        else:
            return 'дней'


    def run(self):
        print(f'{self.name} на нас напали!')
        enemies = 100
        days = 0
        while enemies > 0:
            enemies -= self.power
            days += 1
            print(f'{self.name} сражается {days} {self.days_word(days)}, осталось {enemies} воинов.')
            time.sleep(1)
        print(f'{self.name} одержал победу спустя {days} {self.days_word(days)}!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')
