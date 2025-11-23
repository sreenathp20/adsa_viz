class BST:

    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def insert(self, root, key):
        if root is None:
            return BST(key)
        else:
            if key < root.key:
                root.left = BST.insert(root.left, key)
            else:
                root.right = BST.insert(root.right, key)
        return root
    
    def inorder_traversal(self, root):
        if root:
            BST.inorder_traversal(BST, root.left)
            print(root.key, end=' ')
            BST.inorder_traversal(BST, root.right)

    def search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return BST.search(root.left, key)
        return BST.search(root.right, key)
    
    def optimal_bst(self, keys, freq):
        n = len(keys)
        cost = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            cost[i][i] = freq[i]
        for L in range(2, n + 1):
            for i in range(n - L + 1):
                j = i + L - 1
                cost[i][j] = float('inf')
                for r in range(i, j + 1):
                    c = (cost[i][r - 1] if r > i else 0) + (cost[r + 1][j] if r < j else 0) + sum(freq[i:j + 1])
                    if c < cost[i][j]:
                        cost[i][j] = c
        return cost[0][n - 1]
    
    def build_optimal_bst(self, keys, freq):
        n = len(keys)
        cost = [[0 for _ in range(n)] for _ in range(n)]
        root = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            cost[i][i] = freq[i]
            root[i][i] = i
        for L in range(2, n + 1):
            for i in range(n - L + 1):
                j = i + L - 1
                cost[i][j] = float('inf')
                for r in range(i, j + 1):
                    c = (cost[i][r - 1] if r > i else 0) + (cost[r + 1][j] if r < j else 0) + sum(freq[i:j + 1])
                    if c < cost[i][j]:
                        cost[i][j] = c
                        root[i][j] = r
        return self._build_tree(keys, root, 0, n - 1)

    def _build_tree(self, keys, root, i, j):
        if i > j:
            return None
        r = root[i][j]
        node = BST(keys[r])
        node.left = self._build_tree(keys, root, i, r - 1)
        node.right = self._build_tree(keys, root, r + 1, j)
        return node
    
    def optimal_bst2(self, keys, freq):
        n = len(keys) + 1
        dp = [[[0, None] for _ in range(n)] for _ in range(n)]
        for i in range(n - 1):
            dp[i][i + 1] = [freq[i], i + 1]
        for L in range(2, n):
            for i in range(n - L):
                j = i + L
                dp[i][j] = [float('inf'), None]
                sm = sum(freq[i:j])
                for r in range(i + 1, j + 1):
                    left = dp[i][r - 1][0]
                    right = dp[r][j][0]
                    c = left + right + sm
                    if c < dp[i][j][0]:
                        dp[i][j] = [c, r]
        return dp
    
    def build_optimal_bst2(self, dp, keys):

        def build_tree(i, j):
            if i >= j:
                return None
            r = dp[i][j][1]
            node = BST(keys[r - 1])
            node.left = build_tree(i, r - 1)
            node.right = build_tree(r, j)
            return node

        return build_tree(0, len(dp) - 1)

    
if __name__ == "__main__":
    keys = [10, 12, 20]
    freq = [34, 8, 50]
    keys = [10, 20, 30, 40]
    freq = [4, 2, 6, 3]
    bst = BST(None)
    optimal_cost = bst.optimal_bst(keys, freq)
    optimal_dp = bst.optimal_bst2(keys, freq)
    tree = bst.build_optimal_bst2(optimal_dp, keys)
    print(f"Optimal cost of BST is: {optimal_dp[0][len(keys)][0]}")
    optimal_bst_root = bst.build_optimal_bst(keys, freq)
    print("Inorder traversal of the constructed Optimal BST:")
    bst.inorder_traversal(tree)
    
