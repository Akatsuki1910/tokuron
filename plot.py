import matplotlib.pyplot as plt
import numpy as np

def __num_over_game():
    # path = []
    n_pos = 0
    result_flag = "win"
    while(n_pos < 10):
        n_pos += np.random.randint(0, 3)+1
        # path.append(n_pos)
        if n_pos >= 10:
            result_flag = "lose"
            break
        n_pos += np.random.randint(0, 3)+1
        # path.append(n_pos)
    return result_flag

def __play_game(nog):
    win_arr = []
    lose_arr = []
    for i in range(100):
        win_count = 0
        lose_count = 0
        for j in range(100):
            if "win" == nog():
                win_count += 1
            else:
                lose_count += 1
        win_arr.append(win_count)
        lose_arr.append(lose_count)
    return [win_arr,lose_arr]

def plot_func(num_over_game):
    nnog = __play_game(__num_over_game)
    nog = __play_game(num_over_game)
    points = (nnog[0],nnog[1], nog[0], nog[1])
    fig,ax = plt.subplots()

    ax.set_xticklabels(["before win","before lose","after win","after lose"])
    ax.boxplot(points)

    plt.title('learning results')
    plt.ylabel('points')

    plt.ylim([0,100])
    plt.grid()

    plt.show()