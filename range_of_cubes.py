def find_nb(m):

    vol_accumulated = 0
    has_reached_vol = False

    for x in range(1, m + 1):
        vol = x**3
        vol_accumulated += vol

        if vol_accumulated == m:
            cubes = x
            has_reached_vol = True
            break

        if vol_accumulated > m:
            has_reached_vol = False
            cubes = -1
            break

    if (has_reached_vol):
        print(cubes)
        return cubes
    else:
        print(cubes)
        return cubes


find_nb(4183059834009)
find_nb(135440716410000)
find_nb(40539911473216)
find_nb(26825883955641)
find_nb(24723578342962)
