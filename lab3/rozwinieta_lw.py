from typing import List, Any

MaxElemSize = 6

class ListElem:
    def __init__(self) -> None:
        self.tab: List = [None for _ in range(MaxElemSize)]
        self.ac_size: int = 0
        self.next_elem: None | ListElem = None
        
class LW:
    def __init__(self) -> None:
        self.head: None | ListElem = None
        self.t_size: int = 0
    def get(self, index) -> Any:
        if index < 0 or index >= self.t_size:
            raise IndexError('Indeks poza przedziałem')
        
        current_elem: ListElem = self.head
        ind: int = index
        while True:
            if ind <= current_elem.ac_size:
                return current_elem.tab[ind]     
            else:
                ind = ind - current_elem.ac_size
                current_elem = current_elem.next_elem

    def insert(self, index: int, value: Any) -> None:
        if index < 0:
            raise IndexError('Do indeksow nalezy odwolywac sie poprzez dodanie liczby naturalne')
        
        if self.head == None:
            self.head = ListElem()
        current_elem = self.head
        
        ind: int = index if index < self.t_size else self.t_size
        while True:
            if ind <= current_elem.ac_size:
                if current_elem.ac_size == MaxElemSize:
                    new_tab: ListElem = ListElem()
                    current_elem.next_elem = new_tab
                    new_tab.tab = current_elem.tab[MaxElemSize//2:] + [None]*(MaxElemSize//2)
                    current_elem.tab = current_elem.tab[:MaxElemSize//2] + [None]*(MaxElemSize//2)
                    current_elem.ac_size = MaxElemSize//2
                    new_tab.ac_size = MaxElemSize//2
                    if MaxElemSize % 2 == 1:
                        new_tab.ac_size +=1
                else:
                    current_elem.tab = current_elem.tab[:ind] + [value] + current_elem.tab[ind:(MaxElemSize-1)]
                    current_elem.ac_size += 1
                    break
            else:
                ind = ind - current_elem.ac_size
                current_elem = current_elem.next_elem
             
                
        self.t_size += 1
                
    def delete(self, index):
        if index < 0 or index >= self.t_size:
            raise IndexError('Indeks poza przedziałem')
        
        current_elem: ListElem = self.head
        ind: int = index

        while True:
            if ind <= current_elem.ac_size:
                current_elem.tab[ind] = None
                while True:
                    try:
                        if current_elem.tab[ind+1] != None:
                            current_elem.tab[ind] = current_elem.tab[ind+1]
                            ind += 1
                        else:
                            current_elem.tab[ind] = None
                            break
                    except IndexError:
                        break
                current_elem.ac_size -=1
                
                

                if current_elem.ac_size < MaxElemSize//2:
                    if current_elem.next_elem == None:
                        break
                    s: int= current_elem.ac_size + current_elem.next_elem.ac_size
                    if s <= MaxElemSize:
                        current_elem.tab = current_elem.tab[:current_elem.ac_size] + current_elem.next_elem.tab[:current_elem.next_elem.ac_size] + [None]*(MaxElemSize-s)
                        current_elem.ac_size+= current_elem.next_elem.ac_size
                        current_elem.next_elem = current_elem.next_elem.next_elem
                        break
                    else:
                        while current_elem.ac_size <= MaxElemSize//2:
                            ind_n:int = 0
                            current_elem.tab[ind] = current_elem.next_elem.tab[ind_n]
                            while True:
                                try:  
                                    if current_elem.next_elem.tab[ind_n+1] != None:
                                        current_elem.next_elem.tab[ind] = current_elem.next_elem.tab[ind+1]
                                        ind_n += 1
                                    else:
                                        break
                                except IndexError:
                                        break
                                
                                ind +=1
                        break
                else:
                    break
                            
            else:
                ind = ind - current_elem.ac_size
                current_elem = current_elem.next_elem

            self.t_size -=1





    def print_list(self) -> None:
        current_elem = self.head
        rst: List = list()
        while current_elem:
            rst += current_elem.tab[:current_elem.ac_size]
            current_elem = current_elem.next_elem
        print(rst)

    def test_print(self):
        current_elem = self.head
        while current_elem:
         
            print(current_elem.tab[:MaxElemSize+5], end=" -> ")
            
            current_elem = current_elem.next_elem
        print("None")



def main():
    lw: LW = LW()
    for i in range(0, 9):
        lw.insert(i, i+1)
    print(lw.get(4))
    lw.insert(1, 10)
    lw.insert(8, 11)
    lw.print_list()
    lw.delete(1)
    lw.delete(2)
    lw.print_list()

main()