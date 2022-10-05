# Node class
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


class BinaryTree:
    test = Node(2)
    first = True
    def __init__(self, key):
        self.__root = None
        

    def insert(self, key):
 
        if self.__root is None:
            self.__root = Node(key)
            return

        temp = self.__root
        prev = None

    # This loop loops through the tree and finds the suitable place for the new value 
        while (temp != None):
            if temp.key > key:
                prev = temp
                temp = temp.left
            elif temp.key < key:
                prev = temp
                temp = temp.right
            elif temp.key == key:
                print("Duplicates are not allowed")
    
    # Assign the value
        if prev.key > key:
            prev.left = Node(key)
        elif prev.key < key:
            prev.right = Node(key)


    def traverse_inOrder_starter(self):
        self.traverse_inOrder()
        self.first = True

    def traverse_inOrder(self, root = None):
        if root is None and self.first:
            self.first = False
            root = self.__root
        elif root is None:
            return
        if root:
            self.traverse_inOrder(root.left)
            print(root.key)
            self.traverse_inOrder(root.right)
        


tree = BinaryTree(50)
tree.insert(25)
tree.insert(2)
tree.insert(59)
tree.traverse_inOrder_starter()

#######_________________________________________________________________________________________________

