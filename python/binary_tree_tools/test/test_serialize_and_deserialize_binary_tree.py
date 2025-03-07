import unittest
from binary_tree_tools import deserialize_tree, serialize_tree, TreeNode


class Solution(unittest.TestCase):
    def test_serialization_1(self):
        input = [1, 2, 3, None, None, 4, 5]
        input_str = ",".join(
            [str(char) if char is not None else "N" for char in input])
        deserialized_tree = deserialize_tree(input_str)
        serialized_tree = serialize_tree(deserialized_tree)
        self.assertEqual(serialized_tree, input_str)
        deserialized_tree = deserialize_tree(serialized_tree)
        serialized_tree_2 = serialize_tree(deserialized_tree)
        self.assertEqual(serialized_tree_2, serialized_tree)

    def test_serialization_2(self):
        input = [4, -7, -3, None, None, -9, -3, 9, -7, -4, None, 6, None, -6, -6,
                 None, None, 0, 6, 5, None, 9, None, None, -1, -4, None, None, None, -2]
        input_str = ",".join(
            [str(char) if char is not None else "N" for char in input])
        deserialized_tree = deserialize_tree(input_str)
        serialized_tree = serialize_tree(deserialized_tree)
        self.assertEqual(serialized_tree, input_str)
        deserialized_tree = deserialize_tree(serialized_tree)
        serialized_tree_2 = serialize_tree(deserialized_tree)
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

        serialized_tree = serialize_tree(root)
        expected = "2,1,6,0,N,4,N,N,N,3,5"
        self.assertEqual(serialized_tree, expected)


if __name__ == "__main__":
    unittest.main()
