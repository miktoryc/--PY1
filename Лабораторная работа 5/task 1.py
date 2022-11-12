from pprint import pprint

list_ = []

for i in range(16):
    cart = {"dec": i, "bin": bin(i), "oct": oct(i), "hex": hex(i)}
    list_.append(cart)

pprint(list_)
