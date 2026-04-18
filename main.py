def saralash(royxat):
    yangi_royxat = []
    for son in royxat:
        raqamlar = [int(x) for x in str(son)]
        raqamlar.sort(reverse=True)
        yangi_son = int(''.join(map(str, raqamlar)))
        yangi_royxat.append(yangi_son)
    return yangi_royxat

sonlar = [123, 456, 789, 1011, 1213]
print(saralash(sonlar))
