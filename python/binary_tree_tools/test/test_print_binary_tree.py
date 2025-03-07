import unittest
from unittest.mock import patch
import io
from binary_tree_tools import print_tree, TreeNode


class PrintBinaryTreeTest(unittest.TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_tree(self, stdout_mock):
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
        expected = """└──2
   ├──6
   │  └──4
   │     ├──5
   │     └──3
   └──1
      └──0
"""
        print_tree(root)
        self.assertEqual(stdout_mock.getvalue(), expected)


if __name__ == "__main__":
    unittest.main()
