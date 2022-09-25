#################
#               #
# Problem Set 0 #
#               #
#################


#
# Setup
#

class BTvertex:
    # parent: BTvertex (or None in the case of the root)
    # left : BTvertex
    # right : BTvertex
    # key : string
    # temp : int
    def __init__(self, key):
        self.parent = None
        self.left = None
        self.right = None
        self.key = key
        self.size = None

class BinaryTree:
    #root: BTvertex
    def __init__(self, root):
        self.root = root


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
    numNodes = r.size + 1
    # If the tree is nearly trivial, the root node suffices
    if r.size == 1 or r.size == 2:
        return r

    def vertex_threshold(v):
        # Leaf nodes will never satisfy the condition for non-trivial trees, but are included for the sake of error handling
        if v.left == None and v.right == None:
            raise Exception("Leaf Node is Impossible")
        elif v.left != None and v.right == None:
            if v.left.size < numNodes / 2:
                return v
            nextVertex = v.left
        elif v.left == None and v.right != None:
            if v.right.size < numNodes / 2:
                return v
            nextVertex = v.right
        else:
            if v.left.size < numNodes / 2 and v.right.size < numNodes / 2:
                return v
            # For next level, choose the node with a smaller size
            if v.left.size > v.right.size:
                nextVertex = v.left
                console.log('hi')
            else:
                nextVertex = v.right
        return vertex_threshold(nextVertex)
            
# match...case code for equivalent logic as above (compatible w Python 3.10)
#
#         match (v.left, v.right):
#             case (None, None):
#                 raise Exception
#             case (left, None):
#                 if left.size < numNodes / 2:
#                     return v
#                 nextVertex = v
#             case (None, right):
#                 if right.size < numNodes / 2:
#                     return v
#                 nextVertex = v
#             case (left, right):
#                 if left.size < numNodes / 2 and right.size < numNodes / 2:
#                     return v
#                 if left.size < right.size:
#                     nextVertex = left
#                 else:
#                     nextVertex = right
#         return vertex_threshold(nextVertex)

    return vertex_threshold(r)
