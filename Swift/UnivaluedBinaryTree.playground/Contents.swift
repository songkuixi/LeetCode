public class TreeNode {
    public var val: Int
    public var left: TreeNode?
    public var right: TreeNode?
    public init() { self.val = 0; self.left = nil; self.right = nil; }
    public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }
    public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
        self.val = val
        self.left = left
        self.right = right
    }
}

class Solution {
    func isUnivalTree(_ root: TreeNode?) -> Bool {
        guard let root = root else {
            return false
        }
        return traverse(root, root.val)
    }
    
    func traverse(_ root: TreeNode?, _ val: Int) -> Bool {
        guard let root = root else {
            return true
        }
        if root.val != val {
            return false
        }
        return traverse(root.left, val) && traverse(root.right, val)
    }
}
