#### 이진트리 Node + BinaryTree 구현
# 연산: size, depth, inorder, preorder, postorder 구현
# **node에서는 left/right tree무조건 호출 -> tree에서 root가 있나/없나 확인**
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

    # node의 순회시작---
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

# **node에서는 left/right tree무조건 호출 -> tree에서 root가 있나/없나 확인**
class BinaryTree:
    # tree는 self.r에 root노드를 받아 저장해놓고 있음. 그것외에는 없다?!
    def __init__(self, r):
        self.root = r

    # tree는, 나의 root node가 존재할 경우, node가 수행할 함수들을 호출만하도록 정의해놓음. tree = root + left + right이며..  재귀적으로 호출될려면 그렇게 구성되어야한다.
    # **부분문제로서의 tree는 root_node가 존재 안할수도 있나보다. 그래서 부분문제로서 base를 가져야하므로 0 or [] 빈리스트를 돌려주도록 짠다.**
    # -> tree는 부분의 sub, right tree로, node에서 self.left, self.right로  무적권 일단 호출되므로
    # --> 무적권 호출에 대한 return size,dept=0, 순회=[] 의 basecase를 tree가 없어 끝인 경우, 함수종료를 정의해줘야한다.
    # **node에서는 left/right tree무조건 호출 -> tree에서 root가 있나/없나 확인**
    def size(self):
        if self.root:
            return self.root.size()
        else:
            return 0 

    def depth(self):
        return self.root.depth() if self.root else 0

    def inorder(self):
        return self.root.inorder() if self.root else [] # 여기서부터는 subtree-부분문제의 base case로서  0이 아니라 [] 빈 리스트 반환.
    
    def preorder(self):
        return self.root.preorder() if self.root else [] # 여기서부터는 subtree-부분문제의 base case로서  0이 아니라 [] 빈 리스트 반환.
    
    def postorder(self):
        return self.root.postorder() if self.root else [] # 여기서부터는 subtree-부분문제의 base case로서  0이 아니라 [] 빈 리스트 반환.
    

    

# 이진탐색트리
class Node:
    # 탐색트리부터는 Node가 key+data로 구성된다.
    def __init__(self, key, data):
        self.key = key
        self.data = data 
        self.left = None 
        self.right = None
    
    def insert(self, key, data):
        # data이전에, 일단 들어오는 key  vs  root_node로서 나의 key를 비교한다.
        if key < self.key:
            # 해당 tree가 있으면, 그 tree에서 insert를 새롭게 주문한다.
            if self.left:
                self.left.insert(key, data)
            # 들어가야할 왼쪽에 tree가 없으면?, [Insere상황에서] Node를 생성 -> new Node를 tree자리에 넣어서 단다.
            # * 빈자리에 Node를 단다 -> 빈 sub Tree자리에 new Node를 넣어서 끝낸다.
            else:
                self.left = Node(key, data)
        elif key > self.key:
            if self.right:
                self.right.insert(key, data)
            else:
                self.right = Node(key, data)
        else: 
            # * 이진 탐색 트리에서는 key 중복을 허용하지 않음. 같은 key값이 들어오면 에러를 낸다.
            raise KeyError('중복된 노드 존재')
    
    # * 이진탐색 트리에서는, data가 아니라 T[ node, node] 의 Node list를 모아서 반환한다.
    def inorder(self):
        traversal = []
        # sub tree가 있으면 재귀적 Tree.inorder()를 주면하면 된다. []값으로 return되니 += list extend로 붙혀준다.
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self)
        if self.right:
            traversal += self.right.inorder()

        return traversal

class BinSearchTree:
    # *이진탐색 트리는 root_node를 인자로 안받고, 비어있는 트리(root=None)으로 일단 생성한다.
    # -> 이진탐색 트리는 insert시 빈tree에 Node를 할당해서 트리를 만들었다.
    # --> 해당tree insert시 비었으면, insert해서 self.root(node)를 .insert()해서 채운다?
    def __init__(self):
        # 이탐 tree는 root노드가 없을 수 있다.
        self.root = None

    def insert(self, key, data):
        if self.root:
            self.root.insert(key, data)
        # 이탐 tree가 루트노드가 없을 수 도 있다.-> insert아니라면 말단으로 온상황이다.
        #  -> insert라면 node를 root_node에 넣어서 만들어준다.
        else:
            self.root = Node(key, data)
        
    
    def inorder(self):
        if self.root:
            self.root.inorder()
        # 이탐 tree가 루트노드가 없을 수 도 있다.-> insert아니라면 말단으로 온상황이다.
        #  -> inorder라면, 말단에서 빈 list를 반환해주자. 
        #  -> 부모tree에서는  node_list += 로 extend를 할 준비를 하고 있을 테니
        else:
            return []
            

    
    



