class Node:

    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

    def inorder(self):
        if self:
            if self.left:
                self.left.inorder()
            print(self.value)
            if self.right:
                self.right.inorder()

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

    def btree_list(self):
        mylist=None
        stack=list()
        temp=self
        prev=None
        while True:
            if temp:
                stack.append(temp)
                temp=temp.left
            elif stack:
                temp=stack.pop()
                if not mylist:
                    mylist=temp
                    prev=temp
                else:
                    if temp.left==prev:
                        prev.right=temp
                        prev=temp
                    elif prev.right==temp:
                        temp.left=prev
                        prev=temp
                    elif temp.left!=prev and prev.right!=temp:
                        prev.right=temp
                        temp.left=prev
                        prev=temp
                temp=temp.right
            else:
                break
        return mylist

def traverse(node):
    temp=node
    while temp!=None:
        print(temp.value)
        temp=temp.right
    return
if __name__=="__main__":
    print("==============================")
    print("The binary tree to doubly linked list:")
    node=Node(12)
    node.insert(6)
    node.insert(4)
    node.insert(8)
    node.insert(2)
    node.insert(24)
    node.insert(15)
    node.insert(30)
    node.insert(34)
    node.insert(28)
    print("================================")
    print("The inorder traversal of the tree is:")
    node.inorder()
    print("===================================")
    nd=node.btree_list()
    traverse(nd)




