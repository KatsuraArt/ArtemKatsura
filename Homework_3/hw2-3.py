



def thesaurus(*names):

    res = {}

    for name in names:

        key = name.split()
        key_name = key[0][0]
        key_surname = key[1][0]

        if key_surname not in res:
            res[key_surname] = {}
            res[key_surname][key_name] = []
            res[key_surname][key_name].append(name)
        elif key_name in res[key_surname]:
            res[key_surname][key_name].append(name)
        else:
            res[key_surname][key_name] = []
            res[key_surname][key_name].append(name)
    return res



print(thesaurus("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))