import numpy as np
gamma = 0.9
alpha = 0.1

reward = np.array([[0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 1, 1, 10000, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 1, 10000, -10000],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 10000, -10000],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -10000],
                   ])
Q = np.array(np.zeros([11, 11]))

for i in range(10000):
    p_state = np.random.randint(0, 10)
    n_actions = []
    for j in range(11):
        if reward[p_state, j] != 0:
            n_actions.append(j)

    n_state = np.random.choice(n_actions)

    # Q[p_state, n_state] = (1-alpha)*Q[p_state, n_state]+alpha * \
    #     (reward[p_state, n_state]+gamma*Q[n_state, np.argmax(Q[n_state, ])])
    Q[p_state, n_state] = Q[p_state, n_state]+alpha * \
        (reward[p_state, n_state]+gamma *
         Q[n_state, np.argmax(Q[n_state, ])] - Q[p_state, n_state])


def num_over_game(start):
    # path = []
    p_pos = start
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


win_count = 0
lose_count = 0
for ji in range(100):
    if "win" == num_over_game(0):
        win_count += 1
    else:
        lose_count += 1

print(win_count, lose_count)
