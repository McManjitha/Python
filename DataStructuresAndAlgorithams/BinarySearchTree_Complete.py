class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

    def __str__(self):
        return f"User(username:{self.username}, name:{self.name}, email:{self.email})"

    def __repr__(self):
        return f"User(username:{self.username}, name:{self.name}, email:{self.email})"
###########################################################################################################


class BSTNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return "BinaryTree <{}>".format(to_tuple(self))

    def __repr__(self):
        return "BinaryTree <{}>".format(to_tuple(self))
######################################################################################


def insert(node, key, value):
    if node is None:
        node = BSTNode(key, value)
    elif node.key > key:
        node.left = insert(node.left, key, value)
        node.left.parent = node
    elif node.key < key:
        node.right = insert(node.right, key, value)
        node.right.parent = node
    return node


def find(node, key):
    if node is None:
        return None
    elif node.key == key:
        return node
    elif node.key < key:
        return find(node.right, key)
    elif node.key > key:
        return find(node.left, key)


# update a vlaue in the tree
def update(node, key, value):
    target = node.find(node, key)
    if target is not None:
        target.value = value


# convert binary tree to a tuple
def to_tuple(node):
    if node is None:
        return None
    if node.left is None and node.right is None:
        return node.key
    return to_tuple(node.left),  node.key, to_tuple(node.right)


# Display the entire binary tree
def display_key_structure(node, space='\t', level=0):
    # If the node is empty
    if node is None:
        print(space*level + '∅')
        return

    # If the node is a leaf
    if node.left is None and node.right is None:
        print(space*level + str(node.key))
        return

    # If the node has children
    display_key_structure(node.right, space, level+1)
    print(space*level + str(node.key))
    display_key_structure(node.left,space, level+1)


# Height of a binary tree
def tree_height(node):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))


def list_all_keys(node):
    if node is None:
        return []
    return list_all_keys(node.left) + [node.key] + list_all_keys(node.right)

def list_all(node):
    if node is None:
        return []
    return list_all(node.left) + [(node.keys, node.value)] + list_all(node.right)


#      check whether the tree is balanced or not
#   1. Ensure that the left subtree is balanced.
#   2. Ensure that the right subtree is balanced.
#   3. Ensure that the difference between heights of left subtree and right subtree is not more than 1.
def balanced_unbalanced(node):
    if node is None:
        return True
    leftBalanced = balanced_unbalanced(node.left)
    rightBalanced = balanced_unbalanced(node.right)
    balanced = leftBalanced and rightBalanced and (abs(tree_height(node.left) - tree_height(node.right)) <= 1)
    return balanced


# Make a balanced Binary Search Tree
def make_balanced_bst(data, low=0, high=None, parent=None):
    if high is None:
        high = len(data) - 1
    elif low > high:
        return None

    mid = (high + low) // 2
    key, value = data[mid]
    node = BSTNode(key, value)
    node.parent = parent
    node.left = make_balanced_bst(data, low, mid-1, node)
    node.right = make_balanced_bst(data, mid+1, high, node)

    return node


def traverse_inOrder(node):
    if node is None:
        return []

    return traverse_inOrder(node.left) + [(node.key, node.value)] + traverse_inOrder(node.right)
###################################################################################################################


class TreeMap:
    def __init__(self):
        self.root = None

    def __setitem__(self, key, value):
        node = find(self.root, key)
        if node is not None:
            update(key, value)
        else:
            self.root = insert(self.root, key, value)
            self.root = make_balanced_bst(traverse_inOrder(self.root))

    def __getitem__(self, key):
        node = find(self.root, key)
        if node is not None:
            return node.value
        else:
            return None

    def __iter__(self):
        return (x for x in list_all(self.root))

    def __len__(self):
        return len(list_all_keys(self.root))

    def display(self):
        display_key_structure(self.root)


aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')

users = [aakash, biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]
#rootNode = BSTNode(aakash.username, aakash)
tree = TreeMap()
for x in users:
    tree[x.username] = x
print(len(tree))


