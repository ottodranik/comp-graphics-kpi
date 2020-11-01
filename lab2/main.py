import time
from lab2_core import main_core
from lab2_1 import rotate as lab2_1_rotate, rotate_and_move as lab2_1_rotate_and_move
from lab2_2 import rotate as lab2_2_rotate, rotate_and_move as lab2_2_rotate_and_move
from lab2_3 import rotate as lab2_3_rotate, rotate_and_move as lab2_3_rotate_and_move


# ------ Send rotate and rotate_and_move functions to main core to start process -----
main_core(lab2_1_rotate, lab2_1_rotate_and_move, 'Матричні обчислення. Розширений вектор')

print('Wait 5 seconds...')
time.sleep(5)

main_core(lab2_2_rotate, lab2_2_rotate_and_move, 'Послідовні матричні обчислення')

print('Wait 5 seconds...')
time.sleep(5)

main_core(lab2_3_rotate, lab2_3_rotate_and_move, 'Скалярні обчислення')