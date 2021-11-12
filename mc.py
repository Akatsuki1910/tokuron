""" monte carlo """

import numpy as np

import plot

Q = np.array(np.zeros([11, 3]))


def action_select(s_s, epsilon):
    """ action select """
    arr = [i for i in range(1, 4) if i + s_s < 11]

    if np.random.randint(0, 100) < 10:
        epsilon = 1

    return np.argmax(Q[s_s, :max(arr)])+1 if epsilon == 0 else np.random.choice(arr)


sr = np.array(np.zeros([11, 3]))
rc = np.array(np.zeros([11, 3]))
for i in range(10000):
    S_STATE = 0
    EPI = 0
    memory = []
    while S_STATE != 10:
        a_state = action_select(S_STATE, 0)
        R = 0
        memory.append([S_STATE, a_state])

        s_state_dash = S_STATE + a_state
        if s_state_dash == 10:
            R = -10
        else:
            s_state_dash = action_select(s_state_dash, 1)+s_state_dash
            if s_state_dash == 10:
                R = 10

        EPI += 1

        if R != 0:
            for l in range(EPI):
                st = memory[l][0]
                at = memory[l][1]-1
                rc[st, at] += 1
                sr[st, at] += R
                Q[st, at] = sr[st, at] / rc[st, at]
            EPI = 0
            memory = []

        S_STATE = s_state_dash

plot.plot_func(Q)
