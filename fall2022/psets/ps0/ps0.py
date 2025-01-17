#################
#               #
# Problem Set 0 #
#               #
#################


#
# Setup
#
class BinaryTree:
    def __init__(self, root):
        self.root: BTvertex = root
 
class BTvertex:
    def __init__(self, key):
        self.parent: BTvertex = None
        self.left: BTvertex = None
        self.right: BTvertex = None
        self.key: int = key
        self.size: int = None

#
# Problem 1a
#

# Input: BTvertex v, the root of a BinaryTree of size n
# Output: Up to you
# Side effect: sets the size of each vertex n in the
# ... tree rooted at vertex v to the size of that subtree
# Runtime: O(n)
def calculate_sizes(v):
    v.size = 1
    if v.left != None:
        v.size += calculate_sizes(v.left)
    if v.right != None:
        v.size += calculate_sizes(v.right)
    return v.size

#
# Problem 1c
#

# Input: BTvertex r, the root of a size-augmented BinaryTree T
# ... of size n and height h
# Output: A BTvertex that, if removed from the tree, would result
# ... in disjoint trees that all have at most n/2 vertices
# Runtime: O(h)
def find_vertex(r):
    numNodes = r.size

    # If the tree is trivial or nearly trivial, the root node suffices
    if r.size == 1 or r.size == 2:
        return r

    def vertex_threshold(v):
        # Leaf nodes will never satisfy the condition for non-trivial trees, but are included for the sake of error handling
        if v.left == None and v.right == None:
            raise Exception("Leaf Node is Impossible")
        elif v.left != None and v.right == None:
            # If the parent exists and a size is assigned to it
            if v.parent != None and v.parent.size != None:
                # Test both child tree and parent tree
                if v.left.size <= numNodes / 2 and v.parent.size - v.size <= numNodes / 2:
                    return v
            elif v.left.size <= numNodes / 2:
                return v
            nextVertex = v.left
        elif v.left == None and v.right != None:
            # If the parent exists and a size is assigned to it
            if v.parent != None and v.parent.size != None:
                # Test both child tree and parent tree
                if v.right.size <= numNodes / 2 and v.parent.size - v.size <= numNodes / 2:
                    return v
            elif v.right.size <= numNodes / 2:
                return v
            nextVertex = v.right
        else:
            # If the parent exists and a size is assigned to it
            if v.parent != None and v.parent.size != None:
                # Test both child tree and parent tree
                if v.left.size <= numNodes / 2 and v.right.size <= numNodes / 2 and v.parent.size - v.size <= numNodes / 2:
                    return v
            elif v.left.size <= numNodes / 2 and v.right.size <= numNodes / 2:
                return v
            # For next level, choose the node with a larger size to decrease size
            if v.left.size > v.right.size:
                nextVertex = v.left
            else:
                nextVertex = v.right
        return vertex_threshold(nextVertex)
            
    return vertex_threshold(r)
