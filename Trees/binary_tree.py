class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self):
        self.head = None

    def insert_node(self, val, parent_node=None):

        if parent_node is None:
            parent_node = self.head

        if parent_node is None:
            self.head = Node(val)
            return

        if parent_node.val > val:
            if parent_node.left is None:
                parent_node.left = Node(val)
                return
            parent_node = parent_node.left
            self.insert_node(val, parent_node)
            return

        if parent_node.val < val:
            if parent_node.right is None:
                parent_node.right = Node(val)
                return
            parent_node = parent_node.right
            self.insert_node(val, parent_node)
            return

    def traverse(self, result, parent_node=None):


        if parent_node is None:
            parent_node = self.head

        if parent_node.left is None:
            result.append(parent_node.val)

        # check left first
        if parent_node.left is not None:
            self.traverse(result, parent_node.left)
            result.append(parent_node.val)

        if parent_node.right is not None:
            self.traverse(result, parent_node.right)
            return



if __name__ == "__main__":
    tree = BinaryTree()

    tree.insert_node(50)
    tree.insert_node(30)
    tree.insert_node(40)
    tree.insert_node(41)
    tree.insert_node(42)
    tree.insert_node(43)
    tree.insert_node(15)
    tree.insert_node(20)
    tree.insert_node(18)
    tree.insert_node(17)
    tree.insert_node(19)
    tree.insert_node(10)
    tree.insert_node(9)
    tree.insert_node(8)
    tree.insert_node(3)
    tree.insert_node(5)
    tree.insert_node(6)
    tree.insert_node(7)
    tree.insert_node(2)
    tree.insert_node(60)
    tree.insert_node(52)
    tree.insert_node(64)

    res = []
    tree.traverse(res)
    print(res)
