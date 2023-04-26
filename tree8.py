class Node:
    max_sum=0
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

    def max_path_sum(self):
        s1,s2=0,0
        if not self:
            return 0
        else:
            if self.left:
                s1=self.left.max_path_sum()
            if self.right:
                s2=self.right.max_path_sum()
            Node.max_sum=max(max(max(s1,s2)+self.value,s1+s2+self.value),Node.max_sum)
            return max(s1,s2)+self.value
        
if __name__=="__main__":
    print("=========================")
    print("Finding the maximum path sum:")
    node=Node(12)
    node.insert(6)
    node.insert(3)
    node.insert(10)
    node.insert(1)
    node.insert(4)
    node.insert(24)
    node.insert(30)
    node.insert(34)
    node.insert(18)
    print("============================")
    print("The maximum path sum is:")
    node.max_path_sum()
    print(Node.max_sum)
    print("==============================")
    print("Building second tree:")
    Node.max_sum=0
    node1=Node(-10)
    node1.left=Node(9)
    node1.right=Node(20)
    node1.right.right=Node(7)
    node1.right.left=Node(15)
    print("The maximum path sum is:")
    node1.max_path_sum()
    print(Node.max_sum)
    print("================================")



    