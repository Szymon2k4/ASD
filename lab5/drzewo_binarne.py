from typing import Any, Dict, Union, List

class BST:
    def __init__(self) -> None:
        self.node: None | TreeNode = None

    def search(self, key: int):
        rst: None | TreeNode = self.__search(key, self.node)
        return rst.data if rst is not None else None
        
    def __search(self, key: int, current_elem: Union[None, "TreeNode"]):
        if current_elem is None:
            return 
        
        if key == current_elem.key:
            return current_elem
        elif key < current_elem.key:
            return self.__search(key, current_elem.left_child)
        else:
            return self.__search(key, current_elem.right_child)


    def insert(self, key: int, data: Any) -> None:
        self.node = self.__insert(key, data, self.node)

    def __insert(self, key: int, data: Any, current_node:  Union[None, "TreeNode"]) -> "TreeNode":
        if current_node is None:
            return TreeNode(key, data)

        if current_node.key == key:
            current_node.data = data
        elif current_node.key < key:
            current_node.right_child = self.__insert(key, data, current_node.right_child)
        else:
            current_node.left_child = self.__insert(key, data, current_node.left_child)
        
        return current_node

    def delete(self, key) -> None:
        self.node = self.__delete(self.node, key)

    def __delete(self, current_elem:  Union[None, "TreeNode"], key) -> "TreeNode":
        if current_elem.key < key:
            current_elem.right_child = self.__delete(current_elem.right_child, key)
        elif current_elem.key > key:
            current_elem.left_child = self.__delete(current_elem.left_child, key)
        else:
            if current_elem.left_child is None:
                return current_elem.right_child
            elif current_elem.right_child is None:
                return current_elem.left_child
            else:
                smallest_elem: None | TreeNode = current_elem.right_child
                while smallest_elem.left_child:
                    smallest_elem = smallest_elem.left_child
                current_elem.key = smallest_elem.key
                current_elem.data = smallest_elem.data
                current_elem.right_child = self.__delete(current_elem.right_child, smallest_elem.key)    
        return current_elem

    
    def print_tree(self):
        print("==============")
        self.__print_tree(self.node, 0)
        print("==============")

    def __print_tree(self, node, lvl):
        if node != None:
            self.__print_tree(node.right_child, lvl+5)

            print()
            print(lvl*" ", node.key, node.data)
     
            self.__print_tree(node.left_child, lvl+5)


    def height(self) -> int:
        return self.__height(self.node) 
    
    def __height(self, node: "TreeNode") -> int:
        if node is None:
            return 0  
        
        left_height = self.__height(node.left_child)  
        right_height = self.__height(node.right_child) 

        if left_height > right_height:
            return 1 + left_height
        else:
            return 1 + right_height 
         
    def print(self) -> None:
        result: List[str] = self.__print(self.node, [])
        rst: str = ''.join(result)
        print(rst)
        
    def __print(self, current_elem: Union["TreeNode", None], rst: List) -> List:
        if current_elem is not None:
            self.__print(current_elem.left_child, rst)
            rst.append(f'{current_elem.key} {current_elem.data},')
            self.__print(current_elem.right_child, rst)

        return rst


        


class TreeNode:
    def __init__(self, key: int, data: Any):
        self.key = key
        self.data = data
        self.left_child = None
        self.right_child = None


def main():
    bst: BST = BST()
    elems: Dict[int, str] = {50:'A', 15:'B', 62:'C', 5:'D', 20:'E', 58:'F', 91:'G', 3:'H', 8:'I', 37:'J', 60:'K', 24:'L'}
    for key, value in elems.items():
        bst.insert(key, value)

    bst.print_tree()
    print(bst.search(100))
    bst.print()
    print(bst.search(24))
    bst.insert(20, 'AA')
    bst.insert(6, 'M')
    bst.delete(62)
    bst.insert(59, 'N')
    bst.insert(100, 'P')
    bst.delete(8)
    bst.delete(15)
    bst.insert(55, 'R')
    bst.delete(50)
    bst.delete(5)
    bst.delete(24)
    print(bst.height())
    bst.print()
    bst.print_tree()


if __name__ == "__main__":
    main()
    