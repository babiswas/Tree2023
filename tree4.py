import sys
class Node:
    max_d=-sys.maxsize+1
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

    def mdiameter(self):
        h1=0
        h2=0
        if not self:
            return 0
        else:
            if self.left:
                h1=self.left.mdiameter()
            if self.right:
                h2=self.right.mdiameter()
            Node.max_d=max(Node.max_d,1+h1+h2)
            return 1+max(h1,h2)

    def height(self):
        h1,h2=0,0
        if not self:
            return 0
        else:
            if self.left:
                h1=self.left.height()
            if self.right:
                h2=self.right.height()
            return max(h1,h2)+1
            
    def diameter(self):
        h1,h2=0,0
        d1,d2=0,0
        if not self:
            return 0
        else:
            if self.left:
                h1=self.left.height()
            if self.right:
                h2=self.right.height()
            if self.left:
                d1=self.left.diameter()
            if self.right:
                d2=self.right.diameter()
            return max(max(d1,d2),1+h1+h2)


    def insert(self,value):
        if self.value>value:
            if self.left:
                self.left.insert(value)
            else:
                self.left=Node(value)
        elif self.value<value:
            if self.right:
                self.right.insert(value)
            else:
                self.right=Node(value)
        else:
            print("Duplication not allowed:")
    
    def inorder(self):
        if self:
            if self.left:
                self.left.inorder()
            print(self.value)
            if self.right:
                self.right.inorder()

if __name__=="__main__":
    print("===========================")
    node=Node(12)
    node.insert(6)
    node.insert(2)
    node.insert(10)
    node.insert(1)
    node.insert(0)
    node.insert(24)
    node.insert(18)
    node.insert(30)
    node.insert(25)
    node.insert(36)
    print("================================")
    print("The inorder traversal of the tree is:")
    node.inorder()
    print(f"The height of the binary tree is: {node.height()}")
    print("===================================")
    print("Diameter of a binary tree is:")
    print(f"The diameter of the binary tree is {node.diameter()}")
    print("=======================================")
    print("Optimised diameter of binary tree is:")
    node.mdiameter()
    print(f"The diameter is {node.max_d}")
    print("========================================")



