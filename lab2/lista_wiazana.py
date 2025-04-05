from typing import Any

class Lwj:
    def __init__(self) -> None:
        self.head: None | ListElem = None
        

    def destroy(self) -> None:
        self.head = None
        

    def add(self, elem: Any) -> None:
        new_elem: ListElem = ListElem(elem)
        if self.is_empty():
            self.head = new_elem
            return
        new_elem.next = self.head
        self.head = new_elem


    def append(self, elem: Any) -> None:
        new_elem: ListElem = ListElem(elem)
        if self.is_empty():
            self.head = new_elem
            return
        current_elem: ListElem = self.head
        while current_elem.next:
            current_elem = current_elem.next
        current_elem.next = new_elem

            
    def remove(self) -> None:
        if self.is_empty():
            raise ValueError('Lista jest pusta')
        self.head = self.head.next
        

    def remove_end(self) -> None:
        if self.is_empty():
            raise ValueError('Lista jest pusta')
        current_elem: ListElem = self.head

        if not current_elem.next:
            self.head = None
            return
        
        l = self.length()
        for i in range(l-2):
            current_elem = current_elem.next
        current_elem.next = None
        
    
    def is_empty(self) -> bool:
        if not self.head:
            return True
        return False
        

    def length(self) -> int:
        lth: int = 0
        current_elem: ListElem = self.head
        while current_elem:
            lth += 1
            current_elem = current_elem.next
            
        return lth

    def get(self) -> Any:
        return self.head.data
    

    def display(self) -> None:
        current_elem = self.head
        if not current_elem:
            print('Empty List')
        while current_elem:
            print(f"-> {current_elem.data}")
            current_elem = current_elem.next

        
    
class ListElem:
    def __init__(self, data):
        self.data: Any = data
        self.next: None | ListElem = None



def main():
    data = [('AGH', 'Kraków', 1919),
            ('UJ', 'Kraków', 1364),
            ('PW', 'Warszawa', 1915),
            ('UW', 'Warszawa', 1915),
            ('UP', 'Poznań', 1919),
            ('PG', 'Gdańsk', 1945)]
    uczelnie: Lwj = Lwj()
    for d in data[:3]:
        uczelnie.append(d)
    for d in data[3:]:
        uczelnie.add(d)
    uczelnie.display()

    print(f"\n{uczelnie.length() = }")

    uczelnie.remove()
    print(f"\n{uczelnie.get() = }\n")

    uczelnie.remove_end()
    uczelnie.display()

    uczelnie.destroy()
    print(f"\n{uczelnie.is_empty() = }")
    try:
        uczelnie.remove()
    except ValueError as e:
        print("Nie da się usunąć pierwszego elementu listy:", e)

    try:
        uczelnie.remove_end()
    except ValueError as e:
        print("Nie da się usunąć ostatniego elementu listy:", e)

    uczelnie.append(data[0])
    uczelnie.remove_end()
    print(f"\n{uczelnie.is_empty() = }\n")
    

if __name__ == '__main__':
    main()
        


    
    
    
    
    