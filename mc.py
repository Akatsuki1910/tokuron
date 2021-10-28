import numpy as np
import plot

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


sr = np.array(np.zeros([11, 11]))
rc = np.array(np.zeros([11, 11]))
for i in range(10000):
    s_state = 0
    epi = 0
    memory = []
    while s_state != 10:
        a_state = action_select(s_state)
        memory.append([s_state,a_state])
        epi+=1
        r = reward[s_state,a_state]
        if r != 1:
            for i in range(epi):
                st = memory[i][0]
                at = memory[i][1]
                rc[st,at] += 1
                sr[st,at] += r * pow(-1,epi+1)
                Q[st,at] = sr[st,at] / rc[st,at]
            epi=0
            memory = []
        s_state = a_state

plot.plot_func(Q)
