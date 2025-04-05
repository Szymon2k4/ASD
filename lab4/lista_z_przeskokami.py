from typing import Any, List
import random

class ListElem:
    def __init__(self, key: int, value: Any, level: int) -> None:
        self.key = key
        self.value = value
        self.level = level
        self.ne_tab = [None] * level

class SkipList:
    def __init__(self, max_level: int = 10) -> None:
        self.head: ListElem = ListElem(key = None, value = None, level = max_level)
        self.max_level: int = max_level
    
    def insert(self, key: int, value: Any) -> None:
        new_level: int = randomLevel(0.5, self.max_level)
        new_elem = ListElem(key, value, new_level)

        for i in range(new_level):
            current_elem: ListElem = self.head
            next_elem: ListElem = self.head.ne_tab[i]
            check_ishead: List = []
            while next_elem is not None:
                if next_elem.key == new_elem.key:
                    next_elem.value = new_elem.value
                    break
                elif next_elem.key < new_elem.key:
                    check_ishead.append(next_elem)
                    current_elem = next_elem
                    next_elem = next_elem.ne_tab[i]
                    if next_elem is None:
                        current_elem.ne_tab[i] = new_elem
                        break
                else:
                    current_elem.ne_tab[i] = new_elem
                    new_elem.ne_tab[i] = next_elem
                    break

            if not check_ishead:
                self.head.ne_tab[i] = new_elem

    def search(self, s_key: int) -> Any:
        levels_n: int = 0
        for elem in self.head.ne_tab:
            if elem is not None:
                levels_n +=1
            else:
                break

        for i in range(levels_n-1, -1, -1):
            current_elem: None | ListElem = self.head.ne_tab[i]
            while current_elem is not None:
                if current_elem.key == s_key:
                    return current_elem.value
                elif current_elem.key > s_key:
                    break
                else:
                    current_elem = current_elem.ne_tab[i]

        return None
    
    def remove(self, s_key: int) -> None:
        levels_n: int = 0
        for elem in self.head.ne_tab:
            if elem is not None:
                levels_n +=1
            else:
                break

        for i in range(levels_n-1, -1, -1):
            current_elem: None | ListElem = self.head
            while current_elem.ne_tab[i] is not None:
                if current_elem.ne_tab[i].key == s_key:
                    current_elem.ne_tab[i] = current_elem.ne_tab[i].ne_tab[i]
                    break
                elif current_elem.ne_tab[i].key > s_key:
                    break
                else:
                    current_elem = current_elem.ne_tab[i]

        return None
    



        

    def displayList_(self, n_level: int | str = 'all') -> None:
        if n_level == 'all':
            n_level = self.max_level

        node: ListElem = self.head.ne_tab[0]  
        keys: List = [ ]                       
        while node is not None:
            keys.append(node.key)
            node = node.ne_tab[0]

        for lvl in range(n_level - 1, -1, -1):
            print(f"{lvl}  ", end=" ")
            node = self.head.ne_tab[lvl]
            idx: int = 0
            while node is not None:
                while node.key > keys[idx]:
                    print(end=5*" ")
                    idx += 1
                idx += 1
                print(f"{node.key:2d}:{str(node.value):2s}", end="")
                node = node.ne_tab[lvl]
            print()
        





def randomLevel(p: float, maxLevel: int) -> int:
  lvl = 1   
  while random.random() < p and lvl <maxLevel:
        lvl = lvl + 1
  return lvl


def main():
    random.seed(42)
    sl: SkipList = SkipList()
    keys = list(range(1, 16))
    values = [chr(65 + i) for i in range(len(keys))]
    for k, v in zip(keys, values):
        sl.insert(k, v)
    sl.displayList_()
    print()
    print(sl.search(2))
    sl.insert(2, 'Z')
    print(sl.search(2))
    for i in range(5, 8):
        sl.remove(i)
    print()
    sl.displayList_(1)
    print()
    sl.insert(6, 'W')
    sl.displayList_(1)
    print('\n')
    sl: SkipList = SkipList()
    keys = list(range(15, 0, -1))
    values = [chr(65 + i) for i in range(len(keys))]
    for k, v in zip(keys, values):
        sl.insert(k, v)
    sl.displayList_()
    print()
    print(sl.search(2))
    sl.insert(2, 'Z')
    print(sl.search(2))
    for i in range(5, 8):
        sl.remove(i)
    print()
    sl.displayList_(1)
    print()
    sl.insert(6, 'W')
    sl.displayList_(1)
    
    

if __name__ == '__main__':
    main()