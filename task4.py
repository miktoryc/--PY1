import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(file) -> list[dict]:
    with open(file) as f:
        list_ = []
        index = 0
        for element in f:
            if index == 0:
                heads = element.strip('\n').split(',')
            else:
                dict_ = {}
                i = 0
                j = 0
                for head in heads:
                    for elemental in element.strip('\n').split(','):
                        if i == j:
                            dict_[head] = elemental
                        j += 1
                    i += 1
                    j = 0
                    list_.append(dict_)
            index += 1
    return list_


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
