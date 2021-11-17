""" plot """

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def __nomal_num_over_game(_q_arr):
    """ nomal num over game """
    n_pos = 0
    result_flag = "win"
    while n_pos < 10:
        n_pos += np.random.randint(0, 3)+1
        if n_pos >= 10:
            result_flag = "lose"
            break
        n_pos += np.random.randint(0, 3)+1
    return result_flag


def __num_over_game(q_arr):
    """ num over game """
    # path = []
    n_pos = 0
    result_flag = "win"
    while n_pos < 10:
        n_pos += np.argmax(q_arr[n_pos, ])+1
        # path.append(n_pos)
        if n_pos >= 10:
            result_flag = "lose"
            break
        n_pos += np.random.randint(0, 3)+1
    #     path.append(n_pos)
    # print(path)

    return result_flag


def __play_game(nog, q_arr):
    """ play game """
    win_arr = []
    lose_arr = []
    for _ in range(100):
        win_count = 0
        lose_count = 0
        for _ in range(100):
            if nog(q_arr) == "win":
                win_count += 1
            else:
                lose_count += 1
        win_arr.append(win_count)
        lose_arr.append(lose_count)
    return [win_arr, lose_arr]


def plot_func(q_arr):
    """ plot func """
    nnog = __play_game(__nomal_num_over_game, np.array(np.zeros([10, 3])))
    nog = __play_game(__num_over_game, q_arr)
    points = (nnog[0], nnog[1], nog[0], nog[1])
    _fig, axes = plt.subplots()

    axes.set_xticklabels(
        ["before win", "before lose", "after win", "after lose"])
    axes.boxplot(points)

    plt.title('learning results')
    plt.ylabel('points')

    plt.ylim([0, 100])
    plt.grid()

    plt.show()

    sns.heatmap(q_arr, vmin=-10, vmax=10, annot=True, fmt="1.3f", center=0)
    plt.show()
