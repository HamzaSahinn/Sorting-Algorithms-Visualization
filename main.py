from time import sleep
from sorting import *
from ploting import Visualize_Game
import random


def is_sorted(sorted_list):
    return all(sorted_list[i] <= sorted_list[i+1] for i in range(len(sorted_list) - 1))

game = Visualize_Game()
sorting_list = random.sample(range(0, 400), 400)
sorter_object = Selection_Sort(sorting_list)

game.init_elements(sorting_list)

while not is_sorted(sorting_list):
    game.update_state(sorter_object.iter_one_step())
    sleep(0.05)

print(sorter_object.get_benchmark())
