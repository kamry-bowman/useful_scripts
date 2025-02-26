import unittest
from collections import deque

class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Codec:
    """
        Encodes a tree to a single string. Encoding is as a comma separated level-order traversal,
        with "N" included for leaf node children, so deserialization can determine structure. Trailing
        Ns for leaf nodes are trimmed however.

        The tree:
                     (  2  )
                    /      \
                  (1)       (6)
                 /         /
              (0)        (4)
                         / \
                       (3)  (5)
        Would be encoded as:
        2,1,6,0,N,4,N,N,N,3,5
    """
    def serialize(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        q = deque([root])
        count = 1
        while q:
            for _ in range(len(q)):
                node = q.pop()
                count += 2
                if node:
                    q.appendleft(node.left)
                    q.appendleft(node.right)
        inorder_array = []
        q = deque([root])
        while q:
            for _ in range(len(q)):
                node = q.pop()
                inorder_array.append(node.val if node else None)
                if node is None:
                    continue
                q.appendleft(node.left)
                q.appendleft(node.right)
        last_not_none_index = len(inorder_array) - 1
        for i in reversed(range(len(inorder_array))):
            char = inorder_array[i]
            if char is not None:
                last_not_none_index = i
                break
        inorder_array_trimmed = inorder_array[:last_not_none_index + 1]
        return ",".join([str(char) if char is not None else "N" for char in inorder_array_trimmed])
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        char_array = data.split(",")
        char_array_indexes_for_last_level = [0]
        stopped_at = 1
        char_array_index_to_node = {}
        char_array_index_to_node[0] = TreeNode(int(char_array[0]))
        while stopped_at < len(char_array):
            char_array_indexes_for_current_level = []
            index_in_char_array_indexes_for_current_level = 0
            char_array_i = stopped_at
            stop = min(stopped_at + len(char_array_indexes_for_last_level) * 2, len(char_array))
            while char_array_i < stop:
                char = char_array[char_array_i]
                # we skip through i's until we find a parent node from the last node needing to be filled
                if char_array_i >= char_array_indexes_for_last_level[index_in_char_array_indexes_for_current_level]:
                    if char == "N":
                        node = None
                    else:
                        node = TreeNode(int(char))
                        char_array_index_to_node[char_array_i] = node
                        char_array_indexes_for_current_level.append(char_array_i)
                    parent_node = char_array_index_to_node[char_array_indexes_for_last_level[index_in_char_array_indexes_for_current_level]]
                    if char_array_i % 2 == 1:
                        parent_node.left = node
                    else:
                        parent_node.right = node
                        # we have filled in the right child of this parent, so we can move to the next
                        index_in_char_array_indexes_for_current_level += 1
                char_array_i += 1
            stopped_at = char_array_i
            char_array_indexes_for_last_level = char_array_indexes_for_current_level
        return char_array_index_to_node[0]

class Solution(unittest.TestCase):
    def test_serialization_1(self):
        input = [1,2,3,None,None,4,5]
        input_str = ",".join([str(char) if char is not None else "N" for char in input])
        codec = Codec()
        deserialized_tree = codec.deserialize(input_str)
        serialized_tree = codec.serialize(deserialized_tree)
        self.assertEqual(serialized_tree, input_str)
        deserialized_tree = codec.deserialize(serialized_tree)
        serialized_tree_2 = codec.serialize(deserialized_tree)
        self.assertEqual(serialized_tree_2, serialized_tree)

    def test_serialization_2(self):
        input = [4,-7,-3,None,None,-9,-3,9,-7,-4,None,6,None,-6,-6,None,None,0,6,5,None,9,None,None,-1,-4,None,None,None,-2]
        input_str = ",".join([str(char) if char is not None else "N" for char in input])
        codec = Codec()
        deserialized_tree = codec.deserialize(input_str)
        serialized_tree = codec.serialize(deserialized_tree)
        self.assertEqual(serialized_tree, input_str)
        deserialized_tree = codec.deserialize(serialized_tree)
        serialized_tree_2 = codec.serialize(deserialized_tree)
        self.assertEqual(serialized_tree_2, serialized_tree)

    def test_serialization_pydoc_example(self):
        #             (  2  )
        #            /      \
        #          (1)       (6)
        #         /         /
        #      (0)        (4)
        #                 / \
        #               (3)  (5)
        root = TreeNode(2)
        node_1 = TreeNode(1)
        root.left = node_1
        node_0 = TreeNode(0)
        node_1.left = node_0
        node_6 = TreeNode(6)
        root.right = node_6
        node_4 = TreeNode(4)
        node_6.left = node_4
        node_3 = TreeNode(3)
        node_5 = TreeNode(5)
        node_4.left = node_3
        node_4.right = node_5

        codec = Codec()
        serialized_tree = codec.serialize(root)
        expected = "2,1,6,0,N,4,N,N,N,3,5"
        self.assertEqual(serialized_tree, expected)