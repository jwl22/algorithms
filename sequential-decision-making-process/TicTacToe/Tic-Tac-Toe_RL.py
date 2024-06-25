import os
import numpy as np
import copy
import random
import math

# P1 = -1, P2(COM) = 1
# P1이 먼저 착수


class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.children = []
        self.parent = parent
        self.visits = 0
        self.wins = 0

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def is_fully_expanded(self):
        # return len(self.children) == np.sum(self.data == 0)
        if is_terminal(self)[0] == True or (
            len(self.children) == np.sum(self.data == 0)
        ):
            return True
        else:
            return False

    def best_child(self, c_param=7):
        choices_weights = [
            (child.wins / child.visits)
            + c_param * math.sqrt((math.log(self.visits) / child.visits))
            for child in self.children
        ]
        return self.children[np.argmax(choices_weights)]

    def most_visited_child(self):
        return max(self.children, key=lambda child: child.visits)


def is_terminal(node):
    data = node.data
    for i in range(3):
        if (
            (data[i, :] == -1).all()
            or (data[:, i] == -1).all()
            or (np.diag(data) == -1).all()
            or (np.diag(np.fliplr(data)) == -1).all()
        ):
            return True, -1
        if (
            (data[i, :] == 1).all()
            or (data[:, i] == 1).all()
            or (np.diag(data) == 1).all()
            or (np.diag(np.fliplr(data)) == 1).all()
        ):
            return True, 1
    if np.all(data != 0):
        return True, 0
    return False, None


def expand(node, player):
    available_moves = np.argwhere(node.data == 0)
    while True:
        move = random.choice(available_moves)
        new_data = node.data.copy()
        new_data[move[0], move[1]] = player
        flag = 0
        for child in node.children:
            if (child.data == new_data).all():
                flag = 1
                break
        if flag == 0:
            break
    child_node = Node(new_data, node)
    node.add_child(child_node)
    child_node.parent = node
    return child_node


def simulate(node, player):
    current_data = node.data.copy()
    current_player = player
    while True:
        terminal, winner = is_terminal(Node(current_data))
        if terminal:
            return winner
        available_moves = np.argwhere(current_data == 0)
        move = random.choice(available_moves)
        current_data[move[0], move[1]] = current_player
        current_player = -current_player


def backpropagate(node, result, player):
    while node is not None:
        # while True:
        node.visits += 1
        # if result == current_player:
        #     node.wins += 1
        # elif result == -current_player:
        #     node.wins += -1
        # if result == 0 and node.parent is not None:
        #     node.wins += 0.5
        # elif result == 1 and node.parent is not None:
        #     node.wins += -1
        # elif result == -1 and node.parent is not None:
        #     node.wins += 1

        node.wins += result
        if result == 0:
            node.wins += 0.5
        elif result == -1:
            node.wins -= 1

        node = node.parent


def mcts(root, player, iterations=1000):
    # node = Node(root.data.copy())
    for _ in range(iterations):
        node = root
        current_player = player

        # while is_terminal(node)[0] == False:
        #     if node.is_fully_expanded():
        #         node = node.best_child()
        # # Selection
        while not is_terminal(node)[0]:
            if node.is_fully_expanded():
                node = node.best_child()
                current_player = -current_player
            else:
                node = expand(node, current_player)
                current_player = -current_player
                break

        # while node.is_fully_expanded() and node.children:
        #     node = node.best_child()

        # # Expansion
        # if not node.is_fully_expanded():
        #     node = expand(node, current_player)

        # Simulation
        result = simulate(node, current_player)

        # Backpropagation
        backpropagate(node, result, current_player)

    # return node.most_visited_child()
    return root.best_child(c_param=0)


root = Node(np.zeros((3, 3), dtype=int))

while True:
    os.system("cls")
    board_print = root.data.astype(str)
    board_print = np.where(board_print == "0", " ", board_print)
    board_print = np.where(board_print == "-1", "O", board_print)
    board_print = np.where(board_print == "1", "X", board_print)

    for i in range(3):
        print(board_print[i][0] + "|" + board_print[i][1] + "|" + board_print[i][2])
    print()

    print("Your Turn")
    print("Enter the row and column number (0~2)")
    while True:
        row = int(input("Row: "))
        col = int(input("Col: "))
        if board_print[row][col] != " ":
            print("Invalid Position")
            continue
        else:
            root.data[row][col] = -1
            if root.children == []:
                break
            else:
                for child in root.children:
                    if (child.data == root.data).all():
                        root = child
                        break
            break

    terminal, winner = is_terminal(root)
    if not terminal:
        print("Loading..")
        root = mcts(root, 1)
        terminal, winner = is_terminal(root)

    if terminal:
        if winner == 0:
            print("Draw!")
        elif winner == -1:
            print("You Win!")
        else:
            print("You Lose!")
        break
