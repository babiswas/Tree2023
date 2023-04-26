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

    def lvl_trav(self):
        queue=list()
        queue.append(self)
        while queue:
            m=len(queue)
            print([obj.value for obj in queue])
            while m!=0:
                nd=queue.pop(0)
                if nd.left:
                    queue.append(nd.left)
                if nd.right:
                    queue.append(nd.right)
                m-=1

    def rev_lev_trav(self):
        queue=list()
        stack=list()
        mymap=dict()
        queue.append(self)
        count=0
        while queue:
            ln=len(queue)
            count+=1
            mymap.update({count:ln})
            while ln:
                m=queue.pop(0)
                stack.append(m)
                if m.right:
                    queue.append(m.right)
                if m.left:
                    queue.append(m.left)
                ln-=1
        print(f"The number of levels is {count}")
        while stack:
            mytemp=list()
            for i in range(mymap[count]):
                mytemp.append(stack.pop())
            print([obj.value for obj in mytemp])
            count-=1
            mytemp.clear()


if __name__=="__main__":
    print("==========================")
    node=Node(12)
    node.insert(6)
    node.insert(8)
    node.insert(4)
    node.insert(5)
    node.insert(1)
    node.insert(24)
    node.insert(30)
    node.insert(18)
    node.insert(28)
    node.insert(34)
    print("The level order traversal of the tree is:")
    node.lvl_trav()
    print("The reverse level order traversal of the tree is:")
    node.rev_lev_trav()
    print("================================")
            

            