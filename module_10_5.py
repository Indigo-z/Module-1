from multiprocessing import Pool
from datetime import datetime

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())


if __name__ == "__main__":

    file_names = [f'./file {number}.txt' for number in range(1, 5)]

    start = datetime.now()
    for file_name in file_names:
        read_info(file_name)
    end = datetime.now()
    print(f'{end - start} линейное время')

    start2 = datetime.now()
    with Pool(processes=4) as pool:
        pool.map(read_info, file_names)
    end2 = datetime.now()
    print(f'{end2 - start2} многопроцессное время')


