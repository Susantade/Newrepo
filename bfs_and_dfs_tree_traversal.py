# Breadth First Tree Traversal

class Node:

    '''
        This class is used to create a node.
    '''
    
    def __init__(self, data=None):
        self.left = None
        self.val = data
        self.right = None

class Tree:

    '''
        This class implements BFS and DFS traversal methods.
    '''
    
    def bfs_tree_traversal(self, root: Node):

        '''
            This method traverse a tree using Breadth First Search(BFS) algorithm.
        '''
        
        queue = []
        queue.append(root)
        
        while len(queue) > 0:
            
            node = queue.pop(0)
            print(node.val, end = '-')
               
            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

    def dfs_tree_traversal(self, root: Node):

        '''
            This method traverse a tree using Depth First Search(DFS) algorithm. 
        '''
        
        stack = []
        stack.append(root)
        
        while len(stack) > 0:
            
            node = stack.pop()
            print(node.val, end = '-')

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

def main(root):

    '''
        This function creates tree object and calls its methods.
    '''

    # Raises AssertionError when a tree's root node is None.
    assert root.val is not None, 'Tree Is Empty.'

    tree = Tree()

    print('BFS Tree Traversal: ', end = '')
    tree.bfs_tree_traversal(root)

    print('\nDFS Tree Traversal: ', end = '')
    tree.dfs_tree_traversal(root)

# Driver code

if __name__ == '__main__':

    '''
              a
            /  \
            b   c
           / \  /\
           d  e h i
          /    \
          f     g
    '''

    root = Node('a')
    
    root.left = Node('b')
    root.right = Node('c')
    
    root.left.left = Node('d')
    root.left.right = Node('e')
    
    root.left.left.left = Node('f')
    root.left.right.right = Node('g')
    
    root.right.left = Node('h')
    root.right.right = Node('i')

    main(root)
    
    
        
