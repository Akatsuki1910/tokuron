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
                   [0, 0, 0, 0, 0, 0, 0, 1, 1, 10, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 1, 10, -10],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 10, -10],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -10],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -10],
                   ])
Q = np.array(np.zeros([11, 11]))

def action_select(s):
    a_actions = []
    for j in range(11):
        if reward[s, j] != 0:
            a_actions.append(j)
    return np.random.choice(a_actions)

for i in range(10000):
    s_state = 0
    a_state = action_select(s_state)
    while s_state != 10:
        a_state_dash = action_select(a_state)

        r = reward[s_state, a_state]
        if(r == 1):
            r = 0

        Q[s_state, a_state] = Q[s_state, a_state]+alpha * \
            (reward[s_state, a_state]+gamma *
            Q[a_state, a_state_dash] - Q[s_state, a_state])
        s_state = min(10,a_state +np.random.randint(0, 3)+1)
        a_state = a_state_dash

def num_over_game():
    # path = []
    p_pos = 0
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
