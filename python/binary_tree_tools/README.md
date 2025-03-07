# Serialize and Deserialize Binary Tree as Level Order Traversal

This utility uses level order traversal to serialize a Python binary tree (as are used on Leet Code)

Encodes a tree to a single string. Encoding is as a comma separated level-order traversal,
with "null" included for leaf node children, so deserialization can determine structure. Trailing
nulls for leaf nodes are trimmed however.

```
The tree:
                (  2  )
            /      \
            (1)       (6)
            /         /
        (0)        (4)
                    / \
                (3)  (5)
Would be encoded as:
"2,1,6,0,null,4,null,null,null,3,5"
```

To make use of the code:

```
from binary_tree_tools import serialize_tree, deserialize_tree, TreeNode
example_tree = TreeNode(1, left=TreeNode(0))
serialized = serialize_tree(example_tree)
deserialized = deserialize_tree(serialized)
```

Make sure binary_tree_tools is on PYTHONPATH

# Print binary tree structure

To print out a binary tree structure as follows:

```
  └──2
     ├──6
     │  └──4
     │     ├──5
     │     └──3
     └──1
        └──0

```

You can make use of the print_tree method from binary_tools:

```
from binary_tools import print_tree, TreeNode

tree = TreeNode(1, left=TreeNode(0), right=TreeNode(2))
print_tree(tree)
```

Make sure binary_tree_tools is on PYTHONPATH
