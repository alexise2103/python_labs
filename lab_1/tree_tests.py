import unittest
from tree import Tree, TreeNode

class TestTree(unittest.TestCase):
    def test_create_tree(self):
        """Test tworzenia drzewa i ustawiania wartości."""
        tree = Tree()
        tree.set_root("root")
        self.assertEqual(tree.root.value, "root")
        self.assertEqual(tree.traverse(), ["root"])

    def test_add_children(self):
        """Test dodawania dzieci i krawędzi."""
        tree = Tree()
        tree.set_root("root")

        child1 = TreeNode("child1")
        child2 = TreeNode("child2")
        tree.root.add_child(child1, edge_value=5)
        tree.root.add_child(child2, edge_value=10)

        self.assertEqual(tree.traverse(), ["root", "child1", "child2"])
        self.assertEqual(tree.root.edges[child1], 5)
        self.assertEqual(tree.root.edges[child2], 10)

    def test_nested_children(self):
        """Test dodawania dzieci wielopoziomowych."""
        tree = Tree()
        tree.set_root("root")

        child1 = TreeNode("child1")
        child2 = TreeNode("child2")
        child3 = TreeNode("child3")
        child1.add_child(child3, edge_value=2)
        tree.root.add_child(child1, edge_value=5)
        tree.root.add_child(child2, edge_value=10)

        self.assertEqual(tree.traverse(), ["root", "child1", "child3", "child2"])
        self.assertEqual(tree.root.edges[child1], 5)
        self.assertEqual(tree.root.edges[child2], 10)
        self.assertEqual(child1.edges[child3], 2)

    def test_str_representation(self):
        """Test reprezentacji tekstowej drzewa."""
        tree = Tree()
        tree.set_root("root")
        child1 = TreeNode("child1")
        child2 = TreeNode("child2")
        tree.root.add_child(child1, edge_value=5)
        tree.root.add_child(child2, edge_value=10)

        expected_output = (
            "Node(value=root)\n"
            "    Edge(value=5)\n"
            "    Node(value=child1)\n"
            "    Edge(value=10)\n"
            "    Node(value=child2)\n"
        )
        self.assertEqual(str(tree), expected_output)


if __name__ == "__main__":
    unittest.main()
