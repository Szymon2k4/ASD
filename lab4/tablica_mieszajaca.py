from typing import List, Any

class MixTab:
    def __init__(self, size: int, c1: int = 1, c2: int = 0) -> None:
        self.tab: List = [None for _ in range(size)]
        self.size = size
        self.c1 = c1
        self.c2 = c2
        
    def mix_fun(self, key: int | str) -> int:
        if isinstance(key, str):
            return sum(ord(c) for c in key) % self.size
        else:
            return key % self.size
            

    def kolizja(self, key: int | str) -> int:
        index: int | None = self.mix_fun(key)
        free_index = None

        for i in range(self.size):
            new_index = (index + self.c1*i + self.c2 * i**2) % self.size
            if self.tab[new_index] is None or self.tab[new_index] == 'N':
                if free_index is None:
                    free_index = new_index
                continue
            if self.tab[new_index].key == key:
                return new_index
            
        if free_index is not None:
            return free_index
        return 
        
    def search(self, key: int | str) -> Any:
        index: int | None = self.mix_fun(key)

        if self.tab[index] is None or self.tab[index] == 'N' or self.tab[index].key != key:
            index = self.kolizja(key)
            if index == None or self.tab[index] is None or self.tab[index] == 'N':
                return 
        return self.tab[index].value
        
    def insert(self, key: int | str, value: Any) -> None:
        index: int | None = self.mix_fun(key)

        if self.tab[index] == 'N':
            index = self.kolizja()
            if index is None:
                print('Brak miejsca')
                return
            self.tab[index] = TabElem(key, value)
            return

        if self.tab[index] is None:
            self.tab[index] = TabElem(key, value)
            return

        if self.tab[index].key == key:
            self.tab[index].value = value
            return
        
        index = self.kolizja(key)
        if index is None:
            print('Brak miejsca')
            return
        self.tab[index] = TabElem(key, value)    
        return    
        
    def remove(self, key: int | str) -> None:
        index: int | None = self.mix_fun(key)

        if self.tab[index] is None or self.tab[index] == 'N' or self.tab[index].key != key:
            index = self.kolizja(key)
            if index == None or self.tab[index] is None or self.tab[index] == 'N':
                return 
        self.tab[index] = 'N'
        
    def __str__(self) -> str:
        return str({elem.key: elem.value for elem in self.tab if isinstance(elem, TabElem) })
      
    
class TabElem:
    def __init__(self, key: int | str, value: Any) -> None:
        self.key = key 
        self.value = value
        
    def __str__(self) -> str:
        return f"{self.key}: {self.value}"
    

def test1(size: int, c1: int, c2: int):
    mixTab = MixTab(size, c1, c2)
    keys = list(range(1, 16))
    keys[5] = 18
    keys[6] = 31
    values = [chr(65 + i) for i in range(len(keys))]
    for key, value in zip(keys, values):
        mixTab.insert(key, value)
    print(mixTab)
    s = mixTab.search(5)
    print(s) if s is not None else print('Brak danej')
    s = mixTab.search(14)
    print(s) if s is not None else print('Brak danej')
    mixTab.insert(5, 'Z')
    s = mixTab.search(5)
    print(s) if s is not None else print('Brak danej')
    mixTab.remove(5)
    print(mixTab)
    print(mixTab.search(31))

def test2(size: int, c1: int, c2: int):
    mixTab = MixTab(size, c1, c2)

    keys = [i * 13 for i in range(1, 16)]
    values = [chr(65 + i) for i in range(len(keys))]

    for key, value in zip(keys, values):
        mixTab.insert(key, value)
    print(mixTab)


    
def main():
    test1(13, 1, 0)
    print()
    test2(13, 1, 0)
    print()
    test2(13, 0, 1)
    print()
    test1(13, 0, 1)
    
if __name__ == '__main__':
    main()