""" sarsa """

import numpy as np

import plot

Q = np.array(np.zeros([11, 3]))

GAMMA = 0.9
ALPHA = 0.1


def action_select(s_s):
    """ action select """
    return np.random.choice([i for i in range(1, 4) if i + s_s < 11])


for i in range(10000):
    S_STATE = 0
    a_state = action_select(S_STATE)
    while S_STATE != 10:
        R = 0.001
        s_state_dash = S_STATE + a_state
        if s_state_dash == 10:
            R = -10
            a_state_dash = 1
        else:
            s_state_dash = action_select(s_state_dash) + s_state_dash
            if s_state_dash == 10:
                R = 10
                a_state_dash = 1
            else:
                a_state_dash = action_select(s_state_dash)

        Q[S_STATE, a_state-1] = Q[S_STATE, a_state-1]+ALPHA * \
            (R+GAMMA * Q[s_state_dash, a_state_dash-1] - Q[S_STATE, a_state-1])

        S_STATE = s_state_dash
        a_state = a_state_dash

print(Q)
plot.plot_func(Q)
