import hashlib

hash_dict = dict()

for i in range(100000):
    hash_dict.update(
        {hashlib.sha512(("%05d" % i).encode()).hexdigest().upper(): i})

print(hash_dict[input()])
