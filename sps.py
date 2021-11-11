"""This is a test program."""

import numpy as np

import plot

Q = np.array(np.zeros([11, 3]))

C_BID = 0.1


def action_select(s_s):
    """ action select """
    return np.random.choice([i for i in range(1, 4) if i + s_s < 11])


for i in range(10000):
    S_STATE = 0
    EPI = 0
    memory = []
    while S_STATE != 10:
        a_state = action_select(S_STATE)
        R = 0.1

        s_state_dash = S_STATE + a_state
        if s_state_dash == 10:
            R = -10
        else:
            s_state_dash = action_select(s_state_dash)+s_state_dash
            if s_state_dash == 10:
                R = 10

        memory.append([S_STATE, a_state, R])
        EPI += 1

        if R != 0.001:
            for l in range(EPI):
                st = memory[l][0]
                at = memory[l][1]-1
                Q[st, at] += C_BID*(memory[l][2]-Q[st, at])
            EPI = 0
            memory = []

        S_STATE += a_state

plot.plot_func(Q)
