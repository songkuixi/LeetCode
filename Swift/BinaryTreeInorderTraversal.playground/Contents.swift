public class TreeNode {
    public var val: Int
    public var left: TreeNode?
    public var right: TreeNode?
    public init(_ val: Int) {
        self.val = val
        self.left = nil
        self.right = nil
    }
}

class Solution {
    func inorderTraversal(_ root: TreeNode?) -> [Int] {
        guard root != nil else {
            return []
        }
        var res: [Int] = []
        traverse(root, &res)
        return res
    }
    
    func traverse(_ node: TreeNode?, _ arr: inout [Int]) {
        if let node = node {
            traverse(node.left, &arr)
            arr.append(node.val)
            traverse(node.right, &arr)
        }
    }
}
