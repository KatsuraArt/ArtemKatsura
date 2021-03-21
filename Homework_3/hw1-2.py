words = {
    'Zero': 'Ноль',
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
    'Five': 'Пять',
    'Six': 'Шесть',
    'Seven': 'Семь',
    'Eight': 'Восемь',
    'Nine': 'Девять',
    'Ten': 'Десять',
}

def num_translate():

    word = input("Введите слово на анг: ")
    test_words = word.capitalize()
    return words.get(test_words)

num_translate()
