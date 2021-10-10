#### 이진트리 Node + BinaryTree 구현
# 연산: size, depth, inorder, preorder, postorder 구현
class Node:
    def __init__(self, item):
        self.data = item
        self.left = None  # tree는 재귀적으로 풀어지며, 각 node마다 [재귀적 root node가 되므로] subtree로 가는 링크가 존재한다.
        self.right = None 

    def size(self):
        l = self.left.size() if self.left else 0 # 재귀의 base로서 else 0 + subtree.size()를 호출하면 알아서 자신의 root node.size()를 호출 할 예정임.
        r = self.left.size() if self.left else 0 
        return l+r+1 

    def depth(self):
        # depth는 각각의 subtree depth 중 큰 것 + root depth 1
        l = self.left.depth() if self.left else 0
        r = self.right.depth() if self.right else 0
        return max(l, r) + 1

    # 순회시작---
    # 중위순회
    def inorder(self):
        traversal = [] 
        if self.left:
            traversal += self.left.inorder() # 서브트리에서 재귀적으로 list를 반환해서 갖다줄것임. 그것을 한 곳에 이어 붙인다.
        # root node (=자기자신)의 데이터 1개는 append <-> subtree의 여러데이터(list)는 += 괄떼이어붙이기
        traversal.append(self.data)
        if self.right:
            traversal += self.right.inorder() 
        return traversal # node가 list를 return하면, node.inorder()를 주문한 해당 tree가 list를 받게되는 구조.
     # 전위순회
    def preorder(self):
        traversal = []
        
        traversal.append(self.data)
        if self.left:
            traversal += self.left.preorder()
        if self.right:
            traversal += self.right.preorder()
        return traversal
    # 후위순회
    def postorder(self):
        traversal = []
        
        if self.left:
            traversal += self.left.postorder()
        if self.right:
            traversal += self.right.postorder()
        traversal.append(self.data)
        return traversal

        
class BinaryTree:
    # tree는 self.r에 root노드를 받아 저장해놓고 있음. 그것외에는 없다?!
    def __init__(self, r):
        self.root = r

    # tree는, 나의 root node가 존재할 경우 node가 수행할 함수들을 호출만하도록 정의해놓음. tree = root + left + right이며..  재귀적으로 호출될려면 그렇게 구성되어야한다.
    # **부분문제로서의 tree는 root_node가 존재 안할수도 있나보다. 그래서 부분문제로서 base를 가져야하므로 0 or [] 빈리스트를 돌려주도록 짠다.**
    def size(self):
        if self.root:
            return self.root.size()
        else:
            0 

    def depth(self):
        return self.root.depth() if self.root else 0

    def inorder(self):
        return self.root.inorder() if self.root else [] # 여기서부터는 subtree-부분문제의 base case로서  0이 아니라 [] 빈 리스트 반환.
    
    def preorder(self):
        return self.root.preorder() if self.root else [] # 여기서부터는 subtree-부분문제의 base case로서  0이 아니라 [] 빈 리스트 반환.
    
    def postorder(self):
        return self.root.postorder() if self.root else [] # 여기서부터는 subtree-부분문제의 base case로서  0이 아니라 [] 빈 리스트 반환.
    

    



    

