# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        current=root;
        if(current== None):
            return ;
        while(current.left != None):
            pos=current;
            while(pos !=None):
                pos.left.next=pos.right;
                if(pos.next!=None):
                    pos.right.next=pos.next.left;
                pos=pos.next;
            current=current.left;