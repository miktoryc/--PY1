from random import randint


def get_unique_list_numbers() -> list[int]:
    list_ = []
    for i in range(15):
        list_.append(randint(-10, 10))
    return list_


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))

