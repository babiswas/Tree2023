class Node:
    def __init__(self,value):

        '''Node in a tree'''
        
        self.value=value
        self.left=None
        self.right=None

    def insert(self,value):

        '''Insert method in tree'''

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

    def postorder(self):

        '''Postorder traversal of the tree.'''

        stack=list()
        temp=self
        while True:
            if temp:
                stack.append(temp)
                temp=temp.left
            else:
                if not stack:
                    break
                if stack[-1].right==None:
                    temp=stack.pop()
                    print(temp.value)
                    while stack[-1].right==temp:
                        temp=stack.pop()
                        print(temp.value)
                        if not stack:
                            break
                if stack:
                    temp=stack[-1].right
                else:
                    break

    def preorder(self):

        '''Postorder traversal of the tree:'''

        stack=list()
        temp=self
        stack.append(temp)
        while stack:
            m=stack.pop()
            print(m.value)
            if m.left:
                stack.append(m.left)
            if m.right:
                stack.append(m.right)


    def inorder(self):

        '''Inorder traversal of a tree:'''

        stack=list()
        temp=self
        while True:
            if temp:
                stack.append(temp)
                temp=temp.left
            elif stack:
                temp=stack.pop()
                print(temp.value)
                temp=temp.right
            else:
                break

if __name__=="__main__":
    print("=============================")
    print("Building the tree:")
    node=Node(12)
    node.insert(24)
    node.insert(18)
    node.insert(30)
    node.insert(38)
    node.insert(28)
    node.insert(6)
    node.insert(4)
    node.insert(10)
    node.insert(3)
    node.insert(1)
    print("=====================================")
    print("The inorder traversal of the tree is:")
    node.inorder()
    print("======================================")
    print("The preorder traversal of the tree is:")
    node.preorder()
    print("The postorder traversal of the tree is:")
    print("=======================================")
    node.postorder()