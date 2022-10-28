def get_count_char(str_):
    string = str_
    string = string.lower()
    dict_str = {}
    list_ = string.split()
    for word in list_:
        for i in word:
            if i.isalpha():
                if dict_str.get(i) is None:
                    dict_str[i] = 1
                else:
                    dict_str[i] = dict_str[i] + 1
    return dict_str


def get_procent_char(dict_):
    sum = 0
    for value in dict_.values():
        sum += value
    for key in dict_.keys():
        dict_[key] = dict_[key] * 100 / sum
    return dict_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))
