import time
from testcase_generation import *
from solver import *
from UI import UI
from Cups_UI import Cups
# cur_index_file = 10
# while 1:
#     file_name = 'hard_testcase' + str(cur_index_file) + '.txt'
#     num_color = 80
#     generate(file_name, num_color)
#     m = WaterSortSolver(file_name)
#     start2 = time.time()
#     result = m.search('A_Star')
#     end2 = time.time()
#     print(str(end2 - start2))
#     if result is not None:
#         cur_index_file += 1


# main

# if __name__ == '__main__':
#
#     type = ''
#     print('--Choose testcase--')
#     testcase = input('Input is a number from 0 to 14: ')
#     print('--Choose algorithm--')
#     alg = 1
#     alg = int(input('Input is a number (1 : DFS, 2 : BFS, 3 : A Star): '))
#     if alg == 1:
#         type = 'DFS'
#     elif alg == 2:
#         type = 'BFS'
#     else:
#         type = 'A_Star'
#
#     print()
#     print('Solving...')
#     m = WaterSortSolver("./testcase/testcase"  + testcase + '.txt')
#     start2 = time.time()
#     m.search(type)
#     end2 = time.time()
#     print(str(end2 - start2))
#     ui = UI(Cups(m.initial, m.num_cups, m.capacity, None, m.path, m.Color)).run()
m = WaterSortSolver("./testcase/testcase3"+ '.txt')
m.search('A_Star')
# ui = UI(Cups(m.initial, m.num_cups, m.capacity, None, m.path, m.Color)).run()






