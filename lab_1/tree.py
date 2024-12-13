class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.children = []  # Lista dzieci (węzły potomne)
        self.edges = {}     # Krawędzie, przypisane do dzieci

    def add_child(self, child, edge_value=None):
        """Dodaj węzeł dziecka i opcjonalną wartość krawędzi."""
        self.children.append(child)
        self.edges[child] = edge_value

    def __str__(self, level=0):
        """Rekurencyjna reprezentacja węzła i jego dzieci."""
        ret = " " * (level * 4) + f"Node(value={self.value})\n"
        for child in self.children:
            edge_value = self.edges[child]
            ret += " " * (level * 4 + 4) + f"Edge(value={edge_value})\n"
            ret += child.__str__(level + 1)
        return ret


class Tree:
    def __init__(self):
        self.root = None

    def set_root(self, value):
        """Ustaw korzeń drzewa."""
        self.root = TreeNode(value)

    def traverse(self, node=None):
        """Przejdź przez drzewo w sposób DFS i zwróć wartości węzłów."""
        if node is None:
            node = self.root
        if node is None:
            return []  # Puste drzewo
        result = [node.value]
        for child in node.children:
            result.extend(self.traverse(child))
        return result

    def __str__(self):
        """Zwróć reprezentację tekstową drzewa."""
        if self.root is None:
            return "Empty Tree"
        return str(self.root)
