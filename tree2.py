from __future__ import annotations
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

    def insert(self,value:int)->None:
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

    def is_present(self,node1:Node)->bool:
        test1,test2=False,False
        if node1==self:
            return True
        else:
            if self.left:
                test1=self.left.is_present(node1)
            if self.right:
                test2=self.right.is_present(node1)
            return test1 or test2
            

    def find_node(self,value):
        test1=None
        if self.value==value:
            return self
        else:
            if self.right:
                test1=self.right.find_node(value)
                if test1:
                    return test1
            if self.left:
                test1=self.left.find_node(value)
                if test1:
                    return test1
            
    def lca(self,node1:Node,node2:Node)->Node:
        test1,test2=None,None
        if not self:
            return None
        else:
            if self.is_present(node1) and self.is_present(node2):
                if self.value==node1.value or self.value==node2.value:
                    return self
                else:
                    if self.left:
                        test1=self.left.lca(node1,node2)
                    if self.right:
                        test2=self.right.lca(node1,node2)
                    if test1!=None:
                        return test1
                    elif test2!=None:
                        return test2
                    else:
                        return self
                    
                    

if __name__=="__main__":
    print("===============================")
    node=Node(12)
    node.insert(24)
    node.insert(30)
    node.insert(18)
    node.insert(14)
    node.insert(20)
    node.insert(26)
    node.insert(34)
    node.insert(6)
    node.insert(3)
    node.insert(10)
    node.insert(9)
    print("============================")
    print("Inorder traversal of the tree:")
    node.inorder()
    print("Lowest common ancestor:")
    node1=node.find_node(18)
    node2=node.find_node(26)
    print("===================================")
    print(node1.value)
    print(node2.value)
    print("======================================")
    print("The lowest common ancestor is:")
    temp=node.lca(node1,node2)
    if temp!=None:
        print(temp.value)
    



                    
                


