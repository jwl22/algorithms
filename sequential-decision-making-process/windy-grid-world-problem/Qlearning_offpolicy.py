# %%
import random
import numpy as np
import matplotlib.pyplot as plt


# %%
class GridWorld:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.w1 = False
        self.w2 = False

    def step(self, a):
        if self.y == 3 or self.y == 4 or self.y == 5 or self.y == 8:
            self.w1 = True
        if self.y == 6 or self.y == 7:
            self.w2 = True

        if a == 0:
            self.move_right()
        elif a == 1:
            self.move_left()
        elif a == 2:
            self.move_up()
        elif a == 3:
            self.move_down()

        if self.w1 == True:
            self.wind1()
            self.w1 = False
        if self.w2 == True:
            self.wind2()
            self.w2 = False

        reward = -1
        done = self.is_done()

        return (self.x, self.y), reward, done

    def wind1(self):
        self.x -= 1
        if self.x < 0:
            self.x = 0

    def wind2(self):
        self.x -= 2
        if self.x < 0:
            self.x = 0

    def move_right(self):
        self.y += 1
        if self.y > 9:
            self.y = 9

    def move_left(self):
        self.y -= 1
        if self.y < 0:
            self.y = 0

    def move_up(self):
        self.x -= 1
        if self.x < 0:
            self.x = 0

    def move_down(self):
        self.x += 1
        if self.x > 6:
            self.x = 6

    def is_done(self):
        if self.x == 3 and self.y == 7:
            return True
        else:
            return False

    def get_state(self):
        return (self.x, self.y)

    def reset(self):
        self.x = 3
        self.y = 0
        return (self.x, self.y)


# %%
class AgentQlearning:
    def __init__(self):
        self.q_table = np.zeros((7, 10, 4))  # x size, y size, number of action
        self.eps = 0.5
        self.alpha = 0.5

    def select_action(self, s):
        # epsilon-soft greedy policy
        x, y = s
        prob = random.random()
        if prob < self.eps:  # perform random action with epsilon probabilty
            action = random.randint(0, 3)
        else:  # greedy
            action_val = self.q_table[x, y, :]
            action = np.argmax(action_val)
        return action

    def update_table(self, transition):
        # Now, input for the update is a sigle state transition
        s, a, r, s_next = transition
        x, y = s
        x_next, y_next = s_next
        a_next = self.select_action(
            s_next
        )  # Select an action for s_next (Not actually taken one)
        # Q-learning update
        self.q_table[x, y, a] = (1 - self.alpha) * self.q_table[
            x, y, a
        ] + self.alpha * (
            r + np.max(self.q_table[x_next, y_next, :])
        )  # Now, I think you are familiar with Robbins-Monro form
        # self.q_table[x,y,a] = self.q_table[x,y,a] + self.alpha*(r + np.max(self.q_table[x_next,y_next,:]) - self.q_table[x,y,a])

    def anneal_eps(self):
        # annealing part: You may safely ignore this part :) (by Han)
        self.eps -= 0.03
        self.eps = max(self.eps, 0.1)

    def show_table(self):
        # Show me the one action of which results in the best Q(s,a) value
        q_list = self.q_table.tolist()
        best_qvalue = np.zeros((7, 10))
        best_action = np.zeros((7, 10))
        for row_idx in range(len(q_list)):
            row = q_list[row_idx]
            for col_idx in range(len(row)):
                col = row[col_idx]
                qvalue = np.max(col)
                action = np.argmax(col)
                best_qvalue[row_idx, col_idx] = qvalue
                best_action[row_idx, col_idx] = action
        return best_qvalue, best_action


# %%
def main():
    env = GridWorld()
    agent = AgentQlearning()

    for n_epi in range(30000):
        done = False

        s = env.reset()
        while not done:
            a = agent.select_action(s)
            s_next, r, done = env.step(a)
            agent.update_table((s, a, r, s_next))
            s = s_next
        agent.anneal_eps()

    # Show me the result when it has done!
    opt_q, opt_policy = agent.show_table()

    # Display the opt_q
    fig, ax = plt.subplots()
    plt.imshow(opt_policy, cmap="summer", interpolation="nearest")
    for i in range(7):
        for j in range(10):
            tempstr = "{:.1f}".format(opt_q[i][j])
            text = ax.text(j, i, tempstr, ha="center", va="center", color="k")
    plt.show()

    # Display the opt_policy
    # 0:R, 1:L, 2:U, 3:D
    # 0:→, 1:←, 2:↑, 3:↓
    fig, ax = plt.subplots()
    plt.imshow(opt_policy, cmap="summer", interpolation="nearest")
    ax.text(0, 3, "\nSTART", ha="center", va="center", color="k")
    ax.text(7, 3, "\nGOAL", ha="center", va="center", color="k")

    cur_pos = [3, 0]
    next_pos = [3, 0]
    w1 = False
    w2 = False
    while True:
        if cur_pos[0] == 3 and cur_pos[1] == 7:
            break

        if cur_pos[1] == 3 or cur_pos[1] == 4 or cur_pos[1] == 5 or cur_pos[1] == 8:
            w1 = True
        if cur_pos[1] == 6 or cur_pos[1] == 7:
            w2 = True

        if opt_policy[cur_pos[0]][cur_pos[1]] == 0:
            tempstr = "→"
            next_pos[1] += 1
        elif opt_policy[cur_pos[0]][cur_pos[1]] == 1:
            tempstr = "←"
            next_pos[1] -= 1
        elif opt_policy[cur_pos[0]][cur_pos[1]] == 2:
            tempstr = "↑"
            next_pos[0] -= 1
        elif opt_policy[cur_pos[0]][cur_pos[1]] == 3:
            tempstr = "↓"
            next_pos[0] += 1
        # elif opt_policy[cur_pos[0]][cur_pos[1]] == 4:
        #     tempstr = "↗"
        #     next_pos[0] -= 1
        #     next_pos[1] += 1
        # elif opt_policy[cur_pos[0]][cur_pos[1]] == 5:
        #     tempstr = "↙"
        #     next_pos[0] += 1
        #     next_pos[1] -= 1
        # elif opt_policy[cur_pos[0]][cur_pos[1]] == 6:
        #     tempstr = "↖"
        #     next_pos[0] -= 1
        #     next_pos[1] -= 1
        # else:
        #     tempstr = "↘"
        #     next_pos[0] += 1
        #     next_pos[1] += 1

        if w1 == True:
            next_pos[0] -= 1
            if next_pos[0] < 0:
                next_pos[0] = 0
            w1 = False
        if w2 == True:
            next_pos[0] -= 2
            if next_pos[0] < 0:
                next_pos[0] = 0
            w2 = False

        text = ax.text(
            cur_pos[1], cur_pos[0], tempstr, ha="center", va="center", color="k"
        )
        cur_pos = next_pos.copy()
    plt.show()


# %%
main()
