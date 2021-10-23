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
            

    
    



#### 이진탐색 트리 remove까지 풀구현(insert만 넣은 부분 위에 살아있음)
class Node:

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

    def insert(self, key, data):
        if key < self.key:
            if self.left:
                return self.left.insert(key, data)
            else:
                self.left = Node(key, data)
        elif key > self.key:
            if self.right:
                return self.right.insert(key, data)
            else:
                self.right = Node(key, data) 
        else:
            raise KeyError('Key %s already exists.' % key)

    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self)
        if self.right:
            traversal += self.right.inorder()
        return traversal
    
    # NEW1. lookup
    def lookup(self, key, parent=None):
        if key < self.key:
            if self.left:
                return self.left.lookup(key, self) # self = left subtree의 부모 Node
            else:
                return None, None
        elif key > self.key:
            if self.right:
                return self.right.lookup(key, self) # self = left subtree의 부모 Node
            else:
                return None, None
        else:
            return self, parent
        
    # NEW2. countChildren : 삭제시, 자식의 갯수에 따라 경우가 3가지로 달라짐.
    def countChildren(self):
        count = 0
        if self.left:
            count+=1
        if self.right:
            count+=1
        return count
            
    # insert처럼, remove도 node에서는 없고 Tree에만 있다.
    # countChildren는 node에만 있다.
    # inorder, lookup은 node, Tree 둘다 있다.

class BinSearchTree:

    def __init__(self):
        self.root = None

    def insert(self, key, data):
        if self.root:
            self.root.insert(key, data)
        else:
            self.root = Node(key, data)


    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []
        
    # NEW3. 
    def lookup(self,key):
        if self.root:
            return self.root.lookup(key)
        else:
            return None, None
        
    # NEW4. remove는 어려워서 그런지, 기본적인 주석을 참고해서 만든다.
    def remove(self, key):
        # 1. 일단 Tree lookup -> node lookup의 node, 부모node를 return 받는다.
        node, parent = self.lookup(key)
        # 2. 찾는 node가 있을때만 삭제가 가능하다. 없으면 return False
        if node:
            # 3. 찾은 node에서, node.countChildren로 그놈의 자식갯수를 파악하고 , 그 경우의수를 나눈다.
            nChildren = node.countChildren()
            # The simplest case of no children
            # 4. 자식이 없는 경우
            if nChildren == 0:
                # 만약 parent 가 있으면
                # node 가 왼쪽 자식인지 오른쪽 자식인지 판단하여
                # parent.left 또는 parent.right 를 None 으로 하여
                # leaf node 였던 자식을 트리에서 끊어내어 없앱니다.
                # 4-1. 삭제하는 노드가 루트노드인지 확인한다.
                if parent:
                    # 4-2. 루트노드가 아니면 == 부모가 있으면, 부모의 왼쪽인지/ 오른쪽인지 확인하여, 
                    #      삭제된다 = 부모의 해당쪽 tree가 사라진다.(자식이 없으므로 딸려올라오는 것도 없다.)
                    #      원래 자식이 있으면, 자식를 챙겨놓고, 그 자식을 parent의 link에 대입해줘야함.
                    if node == parent.left:
                        parent.left = None
                    else:
                        parent.right = None
                        
                # 만약 parent 가 없으면 (node 는 root 인 경우)
                # self.root 를 None 으로 하여 빈 트리로 만듭니다.
                # 4-3. 삭제하려는놈이 부모가 없다 == root node이다.
                else:
                    self.root = None
                    #4-4. tree를 비워주는 self.root = None을 시행해준다.
                    
            # When the node has only one child
            elif nChildren == 1:
                # 하나 있는 자식이 왼쪽인지 오른쪽인지를 판단하여
                # 그 자식을 어떤 변수가 가리키도록 합니다.
                #5. 자식이 1개인 경우, 자식이 그대로, 삭제된node의 자리로 가서, 삭제된node의 parent의 해당link에 딸려올라가기 때문에, 
                #   자식tree를  childNonde라는 변수에 미리 챙겨둔다.
                if node.left:
                    childNode = node.left
                else:
                    childNode = node.right
                    
                # 만약 parent 가 있으면
                # node 가 왼쪽 자식인지 오른쪽 자식인지 판단하여
                # 위에서 가리킨 자식을 대신 node 의 자리에 넣습니다.
#               # 6. 자식이 없는 경우 부모를 먼저 챙겼지만, 자식있는 경우 자식챙기고 -> 부모의 어느쪽 제거인지 확인 -> None대신 자식을 넣어주면 된다.
                if parent:
                    if node == parent.left:
                        parent.left = childNode
                    else:
                        parent.right = childNode
                # 만약 parent 가 없으면 (node 는 root 인 경우)
                # self.root 에 위에서 가리킨 자식을 대신 넣습니다.
                #7. 부모가 없는 경우 == root node인 경우, 자식을 root에 줌.
                else:
                    self.root = childNode
            # When the node has both left and right children
            else:
                #8. 자식이 양쪽으로 다있는 경우, 특이하다
                # 1) 삭제대상보다 key가 한칸 더 큰 노드를 바로 오른쪽 subtree로 이동 -> 제일 작은 값을 찾기 위해 왼쪽subtree만 타기  ->  찾는다.
                # 2) 그놈을 S, 그놈의 부모를 P라고 챙겨놓고,  S --> 삭제자리에 배치한다. 이제 기존 S만 삭제하면 된다.
                # 3) P의 자식을 삭제하는 것이므로 P의 자식링크에 None을 넣으면 된다. 하지만, 문제가 p == 삭제대상인 경우도 있다.
                #   X = P
                #  / \
                # a   S (X에서 한칸 오른쪽 갔는데, 더이상 갈 곳이 없다.)
                # 자식이 2개인 X지만,, X == P가 되는 상황이 있음.
                #   S = P 
                #  / \
                # a   S  :  P의 자식링크에 None을 넣는 것을 이 경우에만 p.right 에다가 None을 넣고, 그 외에서는 P.left에다가 None을 넣어 기존 S를 삭제한다.
                
                #8-1, S와 P를 챙긴다. : key 한칸 증가한 것 = 오른쪽으로 한칸 간 것 = S와 , 그것의 부모는 /\ 가기 전 node가 되므로 S와 P를 챙긴다.
                parent = node
                successor = node.right
                # parent 는 node 를 가리키고 있고,
                # successor 는 node 의 오른쪽 자식을 가리키고 있으므로
                # successor 로부터 왼쪽 자식의 링크를 반복하여 따라감으로써
                # 순환문이 종료할 때 successor 는 바로 다음 키를 가진 노드를,
                # 그리고 parent 는 그 노드의 부모 노드를 가리키도록 찾아냅니다.
                #8-2. 이제 S를 왼쪽으로 갈 수 있는 가야한다.
                # - 왼쪽으로 간다. == 직전node.left를  node로 업데이트 시키는데, < 왼쪽이 존재하는 동안 계속 > while 
                while successor.left:
                    parent, successor = successor, successor.left
                # 삭제하려는 노드인 node 에 successor 의 key 와 data 를 대입합니다.
                #8-3. 갈수있는만큼 다 갔으면, S의 < key와 data값 대입함으로써 > --> < S를 삭제할 X 자리로 옮김 >을 시행한다.
                node.key = successor.key
                node.data = successor.data
                # 이제, successor 가 parent 의 왼쪽 자식인지 오른쪽 자식인지를 판단하여
                # 그에 따라 parent.left 또는 parent.right 를
                # successor 가 가지고 있던 (없을 수도 있지만) 자식을 가리키도록 합니다.
                # 8-4. 이제 기존S만 삭제하면 된다.
                # - 보통은 S가 P의 left에 있으므로 p.left에 s의 자식들을 끌어올리면 되지만, 
                # - X = P가 되는 경우도 있으니, S가 p.right가 될때만, p.right에 s의 자식들을 끌올린다.
                if successor == parent.left:
                    # 8-5. 이 때, successor.right는 <왼쪽의 극한이기 때문에 .left는 존재안하며> <있을 수도, 없을 수도 있으며, 있다면 반드시 right에만 있을 S의 자식>을 끌어올려 할당해주자.
                    #   P
                    #  /
                    # S  or
                    #     P
                    #    /
                    #   S
                    #    \
                    #     a
                    parent.left = successor.right
                else:
                    parent.right = successor.right

            return True

        else:
            return False


def solution(x):
    return 0