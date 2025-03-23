# Przykład 1: Implementacja drzewa binarnego
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None  # Lewe dziecko
        self.right = None  # Prawe dziecko

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

# Testowanie drzewa binarnego
tree = BinaryTree()
values = [5, 3, 7, 1, 4, 6, 8]
for value in values:
    tree.insert(value)
print("Przechodzenie inorder:", tree.inorder_traversal())  # Wyświetla [1, 3, 4, 5, 6, 7, 8]

# Przykład 2: Proste drzewo binarne z ręcznym budowaniem
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Funkcja do przechodzenia inorder
def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.value, end=" ")
        inorder(node.right)

print("Ręczne drzewo – inorder:", end=" ")
inorder(root)  # Wyświetla 4 2 5 1 3