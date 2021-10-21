import numpy as np
import plot
gamma = 0.9
alpha = 0.1

reward = np.array([[0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 1, 1, 10000, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 1, 10000, -10000],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 10000, -10000],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -10000],
                   ])
Q = np.array(np.zeros([11, 11]))

for i in range(10000):
    s_state = 0
    while s_state != 10:
        a_actions = []
        for j in range(11):
            if reward[s_state, j] != 0:
                a_actions.append(j)

        a_state = np.random.choice(a_actions)

        Q[s_state, a_state] = Q[s_state, a_state]+alpha * \
            (reward[s_state, a_state]+gamma *
            Q[a_state, np.random.randint(0,len(Q[a_state, ]))] - Q[s_state, a_state])
        s_state = a_state


def num_over_game(start):
    # path = []
    p_pos = start
    n_pos = p_pos
    result_flag = "win"
    while(n_pos < 10):
        n_pos = np.argmax(Q[p_pos, ])
        # path.append(n_pos)
        if n_pos >= 10 or n_pos == 0:
            result_flag = "lose"
            break
        n_pos += np.random.randint(0, 3)+1
        # path.append(n_pos)
        p_pos = n_pos

    return result_flag

plot.plot_func(num_over_game)
