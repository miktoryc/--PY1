from random import sample

list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']
for i in range(26):
    list_.append(list_[i].upper())
for i in range(10):
    list_.append(str(i))


def get_random_password() -> str:
    str_ = "".join(sample(list_, k=8))
    return str_


print(get_random_password())
