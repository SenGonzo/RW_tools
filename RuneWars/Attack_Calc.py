import numpy as np
import itertools


def dice_blob(dice_array):
    # die arrays = [damage, moral, surge, mortal, accuracy]
    blue = np.array([[1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [1, 0, 1, 0, 0],
            [0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [1, 0, 0, 0, 1],
            [0, 0, 2, 0, 0]])
    red = np.array([[1, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 1, 0, 0, 0],
           [2, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 1, 0, 0, 0],
           [1, 0, 1, 0, 1],
           [1, 0, 0, 0, 0]])
    white = np.array([[1, 0, 1, 0, 0],
             [0, 0, 0, 0, 0],
             [1, 0, 0, 0, 0],
             [1, 0, 0, 0, 1],
             [0, 0, 2, 0, 0],
             [1, 1, 0, 0, 0],
             [1, 0, 1, 0, 0],
             [1, 0, 0, 0, 0],
             [1, 0, 0, 0, 0],
             [0, 1, 1, 0, 0],
             [2, 0, 0, 0, 0],
             [0, 0, 0, 1, 0]])

    i = 0
    test_mat = []

    for dice in dice_array:
        if dice == 'red':
            individual_dice_array = red
        elif dice == 'blue':
            individual_dice_array = blue
        elif dice == 'white':
            individual_dice_array = white
        else:
            continue

        test_mat.append(individual_dice_array)

    dice_perm = np.array(list(itertools.product(*test_mat)))
    dice_rez = np.zeros((dice_perm.shape[0], 5))

    for row in dice_perm:
        for item in row:
            dice_rez[i, 0] += item[0]
            dice_rez[i, 1] += item[1]
            dice_rez[i, 2] += item[2]
            dice_rez[i, 3] += item[3]
            dice_rez[i, 4] += item[4]
        i += 1

    return dice_rez, dice_perm

print(dice_blob(['blue', 'red']))
