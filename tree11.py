class Node:

    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

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
            print("Duplication not allowed")
    
    def is_balanced(self):
        h1,h2=0,0
        if not self:
            return 0
        else:
            if self.left:
                h1=self.left.is_balanced()
            if self.right:
                h2=self.right.is_balanced()
            if h1==-1 or h2==-1:
                return -1
            if abs(h1-h2)>1:
                return -1
            return 1+max(h1,h2)

if __name__=="__main__":
    print("===================================")
    node=Node(12)
    node.insert(6)
    node.insert(10)
    node.insert(4)
    node.insert(5)
    node.insert(1)
    node.insert(24)
    node.insert(30)
    node.insert(34)
    print("Checking if tree is height balanced:")
    num=node.is_balanced()
    if num==-1:
        print("The tree is not balanced:")
    else:
        print("The tree is balanced")

            
