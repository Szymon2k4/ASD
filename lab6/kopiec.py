
from typing import Self, List

class Heap:
    def __init__(self) -> None:
        self.tab: List = list()
        self.size: int = 0

    def is_empty(self) -> bool:
        if self.size == 0:
            return True
        return False
     
    def peek(self) -> "Node":
        if self.is_empty():
            return None
        return self.tab[0]
    
    def dequeue(self) -> "Node":
        if self.is_empty():
            return None
        root: Node = self.tab[0]
        self.tab[0] = self.tab[self.size - 1]
        self.size -= 1
        current_idx: int = 0
        while True:
            left_idx: int = self.left(current_idx)
            right_idx: int = self.right(current_idx)
            largest_idx: int = current_idx
            if left_idx < self.size and self.tab[left_idx] > self.tab[largest_idx]:
                largest_idx = left_idx
            if right_idx < self.size and self.tab[right_idx] > self.tab[largest_idx]:
                largest_idx = right_idx
            if largest_idx == current_idx:
                break
            self.tab[current_idx], self.tab[largest_idx] = self.tab[largest_idx], self.tab[current_idx]
            current_idx = largest_idx
        return root
    
    def enqueue(self, new_elem: "Node") -> None:
        current_size: int = self.size
        if current_size == len(self.tab):
            self.tab.append(new_elem)
        else:
            self.tab[current_size] = new_elem
        self.size += 1

        current_idx: int = current_size
        while current_idx > 0:
            parent_idx = self.parent(current_idx)
            if self.tab[parent_idx] < self.tab[current_idx]:
                self.tab[parent_idx], self.tab[current_idx] = self.tab[current_idx], self.tab[parent_idx]
                current_idx = parent_idx  
            else:
                break
        
    def left(self, index: int) -> int:
        return 2*index + 1
    def right(self, index: int) -> int:
        return 2*(index+1)
    def parent(self, index: int)-> int:
        return (index-1)//2
    
    def print_tab(self):
        print('{', end=' ')
        print(*self.tab[:self.size], sep=', ', end=' ')
        print('}')

    def print_tree(self, idx, lvl):
        if idx < self.size:
            self.print_tree(self.right(idx), lvl + 1)
            print(2 * lvl * '  ', self.tab[idx] if self.tab[idx] else None)
            self.print_tree(self.left(idx), lvl + 1)
    
class Node:
    def __init__(self, __data, __priority) -> None:
        self.__data = __data
        self.__priority = __priority

    def __lt__(self, other: Self) -> bool:
        return self.__priority < other.__priority
    
    def __gt__(self, other: Self) -> bool:
        return self.__priority > other.__priority
    
    def __repr__(self) -> str:
        return f"{self.__priority} : {self.__data}"
    



    

def main():
    queue: Heap = Heap()
    priorities: List = [7, 5, 1, 2, 5, 3, 4, 8, 9]
    data: str = "GRYMOTYLA"
    for priority, value in zip(priorities, data):
        node = Node(value, priority)
        queue.enqueue(node)
    queue.print_tree(0, 0)
    queue.print_tab()
    rmw_node: Node = queue.dequeue()
    print(queue.peek())
    queue.print_tab()
    print(rmw_node)
    while not queue.is_empty():
        print(queue.dequeue())  
    queue.print_tab()

if __name__ == '__main__':
    main()





