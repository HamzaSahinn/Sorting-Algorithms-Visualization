import time


class Selection_Sort:
    def __init__(self, sorting_list:list) -> None:
        self.sorting_list = sorting_list
        self.next_index = 0
    
    def iter_one_step(self) -> list:
        min_index = self.next_index
        for search_index in range(self.next_index+1, len(self.sorting_list)):
            if self.sorting_list[min_index] > self.sorting_list[search_index]:
                min_index = search_index
        
        self.sorting_list[self.next_index], self.sorting_list[min_index] = self.sorting_list[min_index], self.sorting_list[self.next_index]
        self.next_index += 1
        
        return self.sorting_list
    
    def get_benchmark(self) -> float:
        sort_list = self.sorting_list.copy()
        start_time = time.time()
        for index in range(len(sort_list)):
            
            min_index = index
            for search_index in range(index+1, len(sort_list)):
                if sort_list[min_index] > sort_list[search_index]:
                    min_index = search_index 
            sort_list[index], sort_list[min_index] = sort_list[min_index], sort_list[index]

        return time.time() - start_time

class Quick_Sort:
    def __init__(self, sorting_list:list) -> None:
        self.sorting_list = sorting_list
    
    def iter_one_step() -> list:
        pass


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


class Quick_Sort:
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