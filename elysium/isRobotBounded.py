import numpy as np

# instructions = "GL"

# init_position = np.array([0, 0])

# step = np.array([0, 1])

# l_turn = np.array([[0, 1],
#                    [-1, 0]])

# r_turn = np.array([[0, -1],
#                     [1, 0]])

# actions = {'g': lambda position: position + step,
#            'l': lambda position: l_turn @ position,
#            'r': lambda position: r_turn @ position}

# position = init_position.copy()

# counter = 0
# while counter < 10:
#     for instruction in instructions:
#         instruction = instruction.lower()

#         position = actions[instruction](position)

#     counter += 1
#     if np.array_equal(position, init_position):
#         print(f"Success in {counter} iterations!!!")
#         break

##########

# instructions = "GL"

# init_position = np.array([0, 0])

# step = np.array([0, 1])

# l_turn = np.array([[0, 1],
#                    [-1, 0]])

# r_turn = np.array([[0, -1],
#                     [1, 0]])

# counter = 0
# position = init_position.copy()

# while counter < 10:
#     for instruction in instructions:
#         instruction = instruction.lower()

#         if instruction == 'g':
#             position = position + step

#         elif instruction == 'l':
#             step = l_turn @ step

#         elif instruction == 'r':
#             step = r_turn @ step

#     counter += 1

#     if np.array_equal(position, init_position):
#         print(f"Success in {counter} iterations!!!")
#         break

##########

digits = [1, 2, 3]

print(list(map(lambda x: int(x), list(str(int(''.join(list(map(lambda x: str(x), digits)))) + 1)))))