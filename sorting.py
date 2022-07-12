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
    def __init__(self, sorting_list:list, game:Visualizer) -> None:
        self.sorting_list = sorting_list
        self.game_visalizer = game
    
    def run_sort(self) -> None:
        for index in range(1, len(self.sorting_list)):
 
            key = self.sorting_list[index]
    
            point_index = index - 1
            while point_index >=0 and key < self.sorting_list[point_index] :
                    self.sorting_list[point_index+1] = self.sorting_list[point_index]
                    self.game_visalizer.update_state(self.sorting_list)
                    point_index -= 1
            self.sorting_list[point_index+1] = key


class Merge_Sort:
    def __init__(self, sorting_list:list, game:Visualizer) -> None:
        self.sorting_list = sorting_list
        self.game_visalizer = game
        
    def merge(self, l, m, r):
        n1 = m - l + 1
        n2 = r - m
    
        L = [0] * (n1)
        R = [0] * (n2)
    
        for i in range(0, n1):
            L[i] = self.sorting_list[l + i]
    
        for j in range(0, n2):
            R[j] = self.sorting_list[m + 1 + j]
    
        i = 0 
        j = 0 
        k = l 
    
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                self.sorting_list[k] = L[i]
                i += 1
            else:
                self.sorting_list[k] = R[j]
                j += 1
            
            self.game_visalizer.update_state(self.sorting_list)
            k += 1
    
        while i < n1:
            self.sorting_list[k] = L[i]
            i += 1
            k += 1
            self.game_visalizer.update_state(self.sorting_list)
            
        while j < n2:
            self.sorting_list[k] = R[j]
            j += 1
            k += 1
            self.game_visalizer.update_state(self.sorting_list)
    
    def mergeSort(self, l, r):
        if l < r:
            m = l+(r-l)//2
    
            self.mergeSort(l, m)
            self.mergeSort(m+1, r)
            self.merge(l, m, r)
        
    def run_sort(self) -> None:
        self.mergeSort(0, len(self.sorting_list)-1)


class Bubble_Sort:
    def __init__(self, sorting_list:list, game:Visualizer) -> None:
        self.sorting_list = sorting_list
        self.game_visalizer = game
    
    def run_sort(self) -> None:
        list_size = len(self.sorting_list)
        swapped = False

        for first_index in range(list_size - 1):
            for second_index in range(0, list_size - first_index - 1):
                if self.sorting_list[second_index] > self.sorting_list[second_index + 1]:
                    swapped = True
                    self.sorting_list[second_index], self.sorting_list[second_index + 1] = self.sorting_list[second_index + 1], self.sorting_list[second_index]
                    self.game_visalizer.update_state(self.sorting_list)
            if not swapped:
                return
        

class Heap_Sort:
    def __init__(self, sorting_list:list, game:Visualizer) -> None:
        self.sorting_list = sorting_list
        self.game_visualizer = game
    
    def heapify(self, n, i): 
        largest = i 
        l = 2 * i + 1 
        r = 2 * i + 2 
         
        if l < n and self.sorting_list[i] < self.sorting_list[l]: 
            largest = l 
         
        if r < n and self.sorting_list[largest] < self.sorting_list[r]: 
            largest = r 
         
        if largest != i: 
            self.sorting_list[i],self.sorting_list[largest] = self.sorting_list[largest],self.sorting_list[i]
            self.game_visualizer.update_state(self.sorting_list) 
         
            self.heapify(n, largest) 
    
    def run_sort(self) -> None:
        list_size = len(self.sorting_list) 
        
        for i in range(list_size // 2 - 1, -1, -1): 
            self.heapify(list_size, i) 
        
        for i in range(list_size-1, 0, -1): 
            self.sorting_list[i], self.sorting_list[0] = self.sorting_list[0], self.sorting_list[i] 
            self.game_visualizer.update_state(self.sorting_list)
            self.heapify(i, 0) 