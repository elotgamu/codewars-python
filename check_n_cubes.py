def volume(cubes):
    """ Return the sum of power values of range """
    cube_row_number = [x**3 for x in range(1, cubes + 1)]
    total_vol = sum(cube_row_number)

    print(total_vol)
    return total_vol


volume(45)
