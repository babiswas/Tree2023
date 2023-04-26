class Node:

    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

    def tree_height(self):
        queue=list()
        queue.append(self)
        count=0
        while queue:
            m=len(queue)
            if m!=0:
                count+=1
            while m!=0:
                temp=queue.pop(0)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
                m-=1
        return count
        


    def height(self):
        h1,h2=0,0
        if not self:
            return 0
        else:
            if self.left:
                h1=self.left.height()
            if self.right:
                h2=self.right.height()
            return 1+h1 if h1>h2 else 1+h2

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
    print("Second implementation:")
    print(f"The height of the tree is {node.tree_height()}")



