

team1_num = 5
team2_num = 6
print('В команде Мастера кода участников: %s!' % team1_num )
print('Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))

score_1 = 40
score_2 = 42
team1_time = 18015.2
team2_time = 13587.1
print('Команда Волшебники данных решила задач: {}'.format(score_2))
print('Волшебники данных решили задачи за {}'.format(team1_time))

print(f'Команды решили {score_1} и {score_2} задач')



if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
    print(result)
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
    print(result)
else:
    print('Ничья')

print(f'Сегодня было решено {score_1 + score_2} задач, в среднем по {round((team1_time + team2_time)/(score_1 + score_2), 1)} секунды на задачу!')



team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2