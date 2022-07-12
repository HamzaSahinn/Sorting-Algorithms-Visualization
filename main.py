from time import sleep
from ploting import Visualizer
import random
import sorting
import importlib
importlib.reload(sorting)


def is_sorted(sorted_list):
    return all(sorted_list[i] <= sorted_list[i+1] for i in range(len(sorted_list) - 1))

game = Visualizer()
sorting_list = random.sample(range(0, 400), 400)
sorter_object = sorting.Merge_Sort(sorting_list, game)


game.init_elements(sorting_list)
while not is_sorted(sorting_list):
    sorter_object.run_sort()


