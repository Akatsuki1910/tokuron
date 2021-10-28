""" Q learning """

import numpy as np
import plot
GAMMA = 0.9
ALPHA = 0.1

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
                   ])
Q = np.array(np.zeros([11, 3]))


def action_select(s_s):
    """ action select """
    return np.random.choice([i for i in range(1, 4) if i + s_s < 11])


for i in range(10000):
    S_STATE = 0
    while S_STATE != 10:
        a_state = action_select(S_STATE)
        r = reward[S_STATE, a_state]
        s_state_dash = S_STATE + a_state

        Q[S_STATE, a_state-1] = Q[S_STATE, a_state-1]+ALPHA * \
            (r+GAMMA * Q[s_state_dash,
             np.argmax(Q[s_state_dash, ])] - Q[S_STATE, a_state-1])
        S_STATE = s_state_dash

plot.plot_func(Q)
