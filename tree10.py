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
            print("Duplication not allowed:")
    
    def spiral(self):
        stack1=list()
        stack2=list()
        stack1.append(self)
        while len(stack1)!=0 or len(stack2)!=0:
            while stack1:
                m=stack1.pop()
                print(m.value)
                if m.left:
                    stack2.append(m.left)
                if m.right:
                    stack2.append(m.right)
            while stack2:
                n=stack2.pop()
                print(n.value)
                if n.right:
                    stack1.append(n.right)
                if n.left:
                    stack1.append(n.left)

if __name__=="__main__":
    print("================================")
    node=Node(12)
    node.insert(6)
    node.insert(4)
    node.insert(10)
    node.insert(3)
    node.insert(5)
    node.insert(24)
    node.insert(18)
    node.insert(30)
    node.insert(34)
    node.insert(28)
    print("Spiral order traversal:")
    node.spiral()
    print("====================================")


    