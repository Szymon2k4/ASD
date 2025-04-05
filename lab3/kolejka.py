from typing import List, Any

class Queue:
    def __init__(self) -> None:
        self.size = 5
        self.que: List = [None for _ in range(self.size)]
        self.write_i: int = 0
        self.read_i: int = 0
        
    
    def is_empty(self) -> bool:
        if self.write_i == self.read_i:
            return True
        return False
    
    def peek(self) -> Any:
        if self.is_empty():
            return None
        return self.que[self.read_i]
    
    
    def dequeue(self) -> Any:
        if self.is_empty():
            return None
        current_elem: Any = self.que[self.read_i]
        self.que[self.read_i] = None
        self.read_i = (self.read_i+1)%self.size
        return current_elem
    
    def enqueue(self, data: Any) -> Any:
        self.que[self.write_i] = data
        self.write_i = (self.write_i+1)%self.size
        
        if self.write_i == self.read_i:
            self.que = self.que[:self.write_i+1] + [None for _ in range(self.size-1)] + self.que[self.read_i:]
            self.read_i += 5
            self.size = 2*self.size

    def __str__(self):
        it: int = self.read_i
        rst: List = list()
        for i in range(it, self.write_i):
            if self.que[i] == None:
                break
            rst.append(self.que[i])
            
        return str(rst)
    
    def test_display(self) -> List:
        return self.que
    
    
def main():
    queue: Queue = Queue()
    for i  in range(1, 5):
        queue.enqueue(i)

    print(queue.dequeue())
    print(queue.peek())
    print(queue)

    for i  in range(5, 9):
        queue.enqueue(i)

    print(queue.test_display())


    while not queue.is_empty():
        print(queue.dequeue())
    print(queue)

if __name__ == '__main__':
    main()