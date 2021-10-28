import numpy as np
import plot
gamma = 0.5
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
    while s_state != 10:
        a_state = action_select(s_state)

        r = reward[s_state, a_state]
        if(r == 1):
            r = 0

        Q[s_state, a_state] = Q[s_state, a_state]+alpha * \
            (r+gamma *Q[a_state, np.argmax(Q[a_state, ])] - Q[s_state, a_state])
        s_state = min(10,a_state +np.random.randint(0, 3)+1)

plot.plot_func(Q)
