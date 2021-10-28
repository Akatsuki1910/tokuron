""" Q learning """

import numpy as np
import plot
GAMMA = 0.5
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
Q = np.array(np.zeros([11, 11]))


def action_select(s_s):
    """ action select """
    a_actions = []
    for j in range(11):
        if reward[s_s, j] != 0:
            a_actions.append(j)
    return np.random.choice(a_actions)


for i in range(10000):
    COUNT = 0
    S_STATE = 0
    while S_STATE != 10:
        a_state = action_select(S_STATE)
        COUNT += 1

        R = reward[S_STATE, a_state]
        if R == 1:
            R = 0
        R *= pow(-1, COUNT+1)

        Q[S_STATE, a_state] = Q[S_STATE, a_state]+ALPHA * \
            (R+GAMMA * Q[a_state, np.argmax(Q[a_state, ])] -
             Q[S_STATE, a_state])
        S_STATE = a_state

plot.plot_func(Q)
