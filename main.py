from time import sleep
from ploting import Visualizer
import random
import sorting


frame_rate_sleep = 0.001
screen_size = 500

def is_sorted(sorted_list):
    return all(sorted_list[i] <= sorted_list[i+1] for i in range(len(sorted_list) - 1))


game = Visualizer(screen_width=screen_size, screen_height=screen_size, sleep_time=frame_rate_sleep)

sorting_list = random.sample(range(0, screen_size), screen_size)

sorter_object = sorting.Heap_Sort(sorting_list, game)


game.init_elements(sorting_list)
while not is_sorted(sorting_list):
    sorter_object.run_sort()


