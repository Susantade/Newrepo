# pre-order tree traversal

class Node:
    
    '''
        This class is used to create node. 
    '''
    
    def __init__(self, data = None):
        self.left = None
        self.val = data
        self.right = None

class TreeTraversal:
    
    '''
        This class implements tree traversal methods.
    '''
    
    def preorder_traversal(self, root: Node):
        
        if root.left is None or root.right is None:
            return root.val
        
        else:
            print(root.val, end = '-')
            print(self.preorder_traversal(root.left), end = '-')
            print(self.preorder_traversal(root.right), end = '-')
        

    def postorder_traversal(self, root: Node):
        
        if root.left is None or root.right is None:
            return root.val
        else:
            print(self.postorder_traversal(root.left), end='-')
            print(self.postorder_traversal(root.right), end='-')
            print(root.val, end='-')

    def inorder_traversal(self, root: Node):
        
        if root.left is None or root.right is None:
            return root.val
        else:
            print(self.inorder_traversal(root.left), end = '-')
            print(root.val, end = '-')
            print(self.inorder_traversal(root.right), end = '-')

def main(root: Node):

    '''
        This is the main function that wraps the tree traversal methods.
    '''
    
    assert root.val is not None, 'Root is empty.'
    
    tree = TreeTraversal()
    
    print('Pre-order Traversal:')
    tree.preorder_traversal(root) # Calling the preorder_traversal method
    
    print("\nPost-order Traversal:") # Calling the postorder_traversal method
    tree.postorder_traversal(root)
    
    print("\nIn-order Traversal:") # Calling the inorder_traversal method
    tree.inorder_traversal(root)


# driver code

if __name__ == '__main__':
    
    root = Node(10)
    root.left = Node(3)
    root.right = Node(7)
    root.left.left = Node(5)
    root.left.right = Node(6)
    root.right.left = Node(8)
    root.left.left.left = Node(55)
    root.left.left.right = Node(50)

    # main() function callings
    main(root)
            
