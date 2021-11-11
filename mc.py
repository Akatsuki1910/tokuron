""" monte carlo """

import numpy as np

import plot

Q = np.array(np.zeros([11, 3]))


def action_select(s_s):
    """ action select """
    return np.random.choice([i for i in range(1, 4) if i + s_s < 11])


sr = np.array(np.zeros([11, 3]))
rc = np.array(np.zeros([11, 3]))
for i in range(10000):
    S_STATE = 0
    EPI = 0
    memory = []
    while S_STATE != 10:
        a_state = action_select(S_STATE)
        R = 0.001
        memory.append([S_STATE, a_state])

        s_state_dash = S_STATE + a_state
        if s_state_dash == 10:
            R = -10
        else:
            s_state_dash = action_select(s_state_dash)+s_state_dash
            if s_state_dash == 10:
                R = 10

        EPI += 1

        if R != 0.001:
            for l in range(EPI):
                st = memory[l][0]
                at = memory[l][1]-1
                rc[st, at] += 1
                sr[st, at] += R
                Q[st, at] = sr[st, at] / rc[st, at]
            EPI = 0
            memory = []

        S_STATE = s_state_dash

print(Q)
plot.plot_func(Q)
