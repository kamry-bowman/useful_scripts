# Serialize and Deserialize Binary Tree as Level Order Traversal

This utility uses level order traversal to serialize a Python binary tree (as are used on Leet Code)

Encodes a tree to a single string. Encoding is as a comma separated level-order traversal,
with "N" included for leaf node children, so deserialization can determine structure. Trailing
Ns for leaf nodes are trimmed however.

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
"2,1,6,0,N,4,N,N,N,3,5"
```

To make use of the code:

```
codec = Codec()
example_tree = TreeNode(1, left=TreeNode(0))
serialized = codec.serialize(example_tree)
deserialized = codec.deserialize(serialized)
```
