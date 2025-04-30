import heapq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(3)
node1 = TreeNode(5)
node2 = TreeNode(1)
node3 = TreeNode(6)
node4 = TreeNode(2)
node5 = TreeNode(0)
node6 = TreeNode(8)
node7 = TreeNode(7)
node8 = TreeNode(4)

root.left = node1
root.right = node2

node1.left = node3
node1.right = node4

node4.left = node7
node4.right = node8

node2.left = node5
node2.right = node6


def traverse(node, mapping, depth):
    if node.left is None and node.right is None:
        mapping[depth] = mapping.get(depth, []) + [node.val]

        return mapping
    
    mapping[depth] = mapping.get(depth, []) + [node.val]

    depth += 1

    traverse(node.left, mapping, depth)
    traverse(node.right, mapping, depth)

    return mapping

nodes = traverse(root, dict(), 0)

deepest = max(nodes.keys())

print(nodes)

print('a' + 'b')