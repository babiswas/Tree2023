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

    def bottom_view(self):
        '''bottom view of the binary tree'''
        queue=list()
        visited=dict()
        queue.append((self,0))
        while queue:
            item=queue.pop(0)
            visited.update({item[1]:item[0].value})
            if item[0].left:
                queue.append((item[0].left,item[1]-1))
            if item[0].right:
                queue.append((item[0].right,item[1]+1))
        for key in sorted(visited.keys()):
            print(visited.get(key))
            
    
    def top_view(self):
        '''Top view of the binary tree'''
        queue=list()
        visited=dict()
        queue.append((self,0))
        while queue:
            item=queue.pop(0)
            if item[1] not in visited:
                visited.update({item[1]:item[0].value})
            if item[0].left:
                queue.append((item[0].left,item[1]-1))
            if item[0].right:
                queue.append((item[0].right,item[1]+1))
        for key in sorted(visited.keys()):
            print(visited.get(key))

if __name__=="__main__":
    print("===============================")
    print("Bottom view of a binary tree:")
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
    print("=====================================")
    print("The top view of the binary tree is:")
    node.top_view()
    print("========================================")
    print("The bottom view of the binary tree is:")
    node.bottom_view()
    print("=======================================")

            
