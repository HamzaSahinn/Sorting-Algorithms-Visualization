import time
from ploting import Visualizer
import pygame


class Selection_Sort:
    def __init__(self, sorting_list:list, game:Visualizer) -> None:
        self.sorting_list = sorting_list
        self.next_index = 0
        self.game_visualizer = game
    
    def run_sort(self) -> None:
        for index in range(len(self.sorting_list)):
            
            min_index = index
            for search_index in range(index+1, len(self.sorting_list)):
                if self.sorting_list[min_index] > self.sorting_list[search_index]:
                    min_index = search_index 
            self.sorting_list[index], self.sorting_list[min_index] = self.sorting_list[min_index], self.sorting_list[index]
            self.game_visualizer.update_state(self.sorting_list)


class Quick_Sort:
    def __init__(self, sorting_list:list, visualizer:Visualizer) -> None:
        self.sorting_list = sorting_list
        self.low_index = 0
        self.high_index = len(sorting_list) - 1
        self.game_visualizer = visualizer
    
    def _partition(self, low, high):
        pivot, ptr = self.sorting_list[high], low

        for i in range(low, high):
            if self.sorting_list[i] <= pivot:
                self.sorting_list[i], self.sorting_list[ptr] = self.sorting_list[ptr], self.sorting_list[i]
                self.game_visualizer.update_state(self.sorting_list)
                ptr += 1

        self.sorting_list[ptr], self.sorting_list[high] = self.sorting_list[high], self.sorting_list[ptr]
        self.game_visualizer.update_state(self.sorting_list)
        
        return ptr

    def _quicksort(self, low, high):
        if len(self.sorting_list) == 1:
            return self.sorting_list
        
        if low < high:
            pi = self._partition(low, high)
            self._quicksort(low, pi-1)
            self._quicksort(pi+1, high)
            
        return self.sorting_list
         
    def run_sort(self) -> None:
        self._quicksort(0, len(self.sorting_list)-1)


class Insertion_Sort:
    def __init__(self, sorting_list:list) -> None:
        self.sorting_list = sorting_list
    
    def iter_one_step() -> list:
        pass


class Merge_Sort:
    def __init__(self, sorting_list:list) -> None:
        self.sorting_list = sorting_list
    
    def iter_one_step() -> list:
        pass


class Bubble_Sort:
    def __init__(self, sorting_list:list) -> None:
        self.sorting_list = sorting_list
    
    def iter_one_step() -> list:
        pass


class Heap_Sort:
    def __init__(self, sorting_list:list) -> None:
        self.sorting_list = sorting_list
    
    def iter_one_step() -> list:
        pass