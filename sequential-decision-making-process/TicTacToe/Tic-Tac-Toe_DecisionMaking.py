import os
import numpy as np
import copy

# P1 = -1, P2(COM) = 1
# P1이 먼저 착수


class Node:
    def __init__(self, data):
        self.value = 0
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)


def update_tree(root, P):
    if (
        (root.data[0, :] == -P).all()
        or (root.data[1, :] == -P).all()
        or (root.data[2, :] == -P).all()
        or (root.data[:, 0] == -P).all()
        or (root.data[:, 1] == -P).all()
        or (root.data[:, 2] == -P).all()
        or (np.diag(root.data) == -P).all()
        or (np.diag(np.fliplr(root.data)) == -P).all()
    ):
        root.value = -P
        return root.value

    for i in range(9):
        if root.data[i // 3][i % 3] == 0:
            tmp = root.data.copy()
            tmp = tmp.flatten()
            tmp[i] = P

            root.add_child(Node(tmp.reshape(3, 3)))
            # updated_value = update_tree(Node(tmp.reshape(3, 3)), -P)
            updated_value = update_tree(root.children[len(root.children) - 1], -P)
            if updated_value == P:
                root.value = P
                break


def endchk(root):
    if root.children == []:
        if root.value == 0:
            print("Draw!")
        elif root.value == -1:
            print("You Win!")
        else:
            print("You Lose!")

        exit(0)


root = Node(np.zeros((3, 3), dtype=int))

os.system("cls")
print("Use Decision Making")
print("Loading...")
update_tree(root, -1)

while True:
    os.system("cls")
    board_print = root.data.astype(str)
    board_print = np.where(board_print == "0", " ", board_print)
    board_print = np.where(board_print == "-1", "O", board_print)
    board_print = np.where(board_print == "1", "X", board_print)

    for i in range(3):
        print(board_print[i][0] + "|" + board_print[i][1] + "|" + board_print[i][2])
    print()

    endchk(root)

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
            break

    for node in root.children:
        if node.children == []:
            if (node.data == root.data).all():
                root = node
                break
        else:
            if (node.data == root.data).all():
                best_v = -2
                for node2 in node.children:
                    if node2.value > best_v:
                        best_v = node2.value
                        best_node = node2

                root = best_node
                break
