"""This is a test program."""

import numpy as np
import plot
C_BID = 0.1

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
    S_STATE = 0
    EPI = 0
    memory = []
    while S_STATE != 10:
        a_state = action_select(S_STATE)
        memory.append([S_STATE, a_state])
        EPI += 1
        r = reward[S_STATE, a_state]
        if r != 1:
            for l in range(EPI):
                st = memory[l][0]
                at = memory[l][1]
                Q[st, at] += C_BID*(r * pow(-1, l % 2)-Q[st, at])
            EPI = 0
            memory = []

        S_STATE = a_state

plot.plot_func(Q)
