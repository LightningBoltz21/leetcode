from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return f"TreeNode(val={self.val})"
    
    def __repr__(self):
        return self.__str__()

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def traverse(root):
        
            if not root:
                nodes.append(None)
                return
            traverse(root.left)
            nodes.append(root.val) 
            traverse(root.right)
            return nodes
        
        nodes = []
        p_list = traverse(p)
        nodes = []
        q_list = traverse(q)
        
        print(p_list)
        print(q_list)
        return p_list == q_list

if __name__ == "__main__":
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(3)
    
    tree2 = TreeNode(1)
    tree2.left = TreeNode(2)
    tree2.right = TreeNode(3)
    
    solution = Solution()
    result = solution.isSameTree(tree1, tree2)
    print(f"Are the trees the same? {result}")
  