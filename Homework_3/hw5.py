

from random import uniform

def get_jokes(count):
    result = []
    objects = ["автомобиль", "лес", "огонь", "город", "дом"]
    time_of_day = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    for i in range(count):
        result.append(f'{objects[int(uniform(0,len(objects) - 1))]}, {time_of_day[int(uniform(0,len(time_of_day) - 1))]}, {adjectives[int(uniform(0,len(adjectives) - 1))]}')
    return result

print(get_jokes(5))