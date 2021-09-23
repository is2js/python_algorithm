############## 양방향 연결 리스트
class Node:
    def __init__(self, item):
        self.data = item 
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        # list생성시에는  외부data없이, count,head,tail 만 생성
        self.nodeCount = 0

        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail 
        self.tail.prev = self.head
        self.tail.next = None 

    def __repr__(self):
        # 출력시... 비었다면? 비었다고 메세지후 종료
        if self.nodeCount == 0:
            return 'LinkedList: empty'

        # 안비어있다면, head부터 쭉쭉 다다음것이있을때 다음것작전으로
        # - 1개씩 이동하면서 data를 string으로 뽑아 저장해준다.
        s = ''
        curr = self.head # i=0 -> i+=1이 아니라,    curr = self.head -> curr.next로 업데이트한다. 기약없이 조건동안 돌때 while
        while curr.next.next:
            curr=curr.next  # head부터 시작이라.. 일단 업뎃하고나서 데이터 수집함. (왜냐면 head에는 뽑아낼 값x  0같은 시작점에 불과하다.)
            s += repr(curr.data) # 출력시 나오는 string을 변수로 잡을 때는 repr() 내장함수를 이용한다.
            # 업데이트 된놈을 모으고나서  [ 그 [다다음] 것까지 있으면 ] -> 화살표도 추가
            # - 단방향 : tail의 dummy node 없으니, 다음 것 존재? 실Node존재 -> 화살표 추가
            # - 양방향 : tail의 dummy node가 if .next 검사시 True로 나와버림.(가짜노든데)
            # -- 양방향에 추가된 tail node때문에, (마지막Node가정) 다음(tail)에 그 다음(None)을 검사해서 None이 아니다 -> 다음은 dummynode아니고 실node다. -> 화살표 추가.
            # -- my) 양방향시 다음Node로 검사하면 tailNode가 실Node로 객체가 존재해버린다. 
            # **항상 다다음이 있는지를 확인해서 **`다다음이 있어야 다음이 있다.`**의 개념을 활용한다.
            if curr.next.next is not None:
                # 다다음이 None이 아니다 == 다음이 있다.
                s += ' -> '
        return s 

    def getLength(self):
        return self.nodeCount
    
    # 어차피 1~n번Node를 다 순회해야하는 것은 그냥 처음부터 돈다?
    # - getAt시에만.. 역 후진... 을 사용하고, 순회/역순회는 그냥 첨부터 가는길에 담아놓는다.
    # - reverse 가 따로 존재한다. 이놈들
    def traverse(self):
        result = []
        curr = self.head 
        # 다다음이 있다 = 다음이 실Node로 존재함.
        while curr.next.next:
            curr = curr.next  # 여기서도 먼저 업데이트하고 뽑아낸다. 왜냐면 head에는 뽑아낼 값x
            result.append(curr.data) # node가 아니라 현재node의 데이터를 추출
        return result

    def reverse(self):
        result = []
        curr = self.tail 
        # 전전이 있다 = 전이 실Node로 존재함.
        while curr.prev.prev:
            curr = curr.prev
            result.append(curr.data)
        return result

    # 참고)
    # - getAt(pos)는 0의 head까지는 가져올 수 있다? (tail은 X)
    # - insertAt(pos, newNode)는  getAt(pos-1)로 prev를 얻으니 
    # -> 1~n을 다루는 insertAt(pos)을 위해서라도, getAt(pos-1)은 0을 다룰 수 있어야한다.
    # -> n+1은 다룰일이 없나보다..
    def getAt(self, pos):
        # getAt은 insertAt(pos-1)시 0도 들어간다. -> 0은 처리할 수 있어야한다.
        if pos < 0 and pos > self.nodeCount:
            return 
        
        # getAt은 양방향부터 개선되어, 절반보다 큰 pos의 Node를 얻는다면 뒤에서 온다.
        # - 뒤에서 오는 것은 tail부터 어디까지??? => 횟수를 가지고 후진시켜 찾아간다.
        # - 0부터 몇번 반복(전진or후진)하는지를 i=0 while < N  i+=1으로 반복한다.
        # ** -> 특정지점까지 가려고하는데, 시작을 모른다면, i=0으로 시작하자. 그게 설사 뒤에서부터라도 **
        if pos > (self.nodeCount // 2) :
            
            curr = self.tail 
            # while에 if조건 + i업데이틀 걸어야한다.
            # 서로 포함이면 자기index에서 바로뺀 만큼 전진 / 0부터 시작이면, 바로뺀+1번 전진이다.
            # (self.nodeCount - pos)  +1번 전진하려면???  
            # i=0부터 < N 시 N번 반복..이니까
            # i=0부터 < [self.nodeCount - pos + 1]

            # 더 쉽게 tail을 self.nodeCount+1로 보고, 서로포함하여 빼서 (n+1 - pos ) 를 전진횟수로 보자.
            
            # i = 0 # 찾아가기위한 횟수를 위해 작성: i=0  while < N  i+=1
            # while (self.nodeCount -  pos  +1):
            #     i+=1
            i = 0 
            # N번 prev후진을 반복해서, 원하는 위치의 node까지 찾아옴.
            while i < self.nodeCount -  pos  +1 :
                curr = curr.prev
                i+=1
        else:
            curr = self.head
            i=0
            while i < (pos-0):
                curr = curr.next
                i+=1
        return curr 

        
    # insertAt(pos) -> getAt(pos-1) -> prev를 받은 상태다.
    # - 양방향에서는 next도 필요하다.
    # - prev에는 newNode로 인해 next가 되어버린 놈을 가리키고 있다.
    def insertAfter(self, prev, newNode):
        # (prev) \(NewNode) /(next가 필요한 상황)
        next = prev.next
        
        # newNode에서 나가는 방향의 화살표들( 할당당하는놈이 newNode.xxxx = )을 채워준다.
        newNode.prev = prev 
        newNode.next = next 
            # (기존 연결을 끊어서) newNode로 들어가는 화살표들을 채워준다.
            # 뒤에서 들어가는
        prev.next = newNode
            # 앞에서 뒤로가는 화살표
        next.prev = newNode

        # 다 완료되면 count+1 + True반환
        self.nodeCount+=1

        return True 

    def insertAt(self, pos, newNode):
        if pos < 1 and pos > self.nodeCount :
            return False
        # 양방향에서는 self.tail에서 바로뽑기의 예외를 버리고, getAt에서 알아서 뽑아오라고 통일시켰다.
        # - prev만 찾으면 insertAfter에서 prev-newNode-next로 처리하게 한다.
        prev = self.getAt(pos-1)
        return self.insertAfter(prev, newNode)

    # 쓸일이 있으려나 모르겠지만, insertBefore(next, )는 insertAfter(prev, )와 대칭적으로 작성한다.
    def insertBefore(self, next, newNode):
        prev = next.prev 
        newNode.prev = prev 
        newNode.next = prev.next
        prev.next = newNode 
        next.prev = newNode 
        self.nodeCount += 1 
        return True


    # insert처럼 prev를 받아오며, 외부에서 받아온 newNode를 두고 next를 찾았던 것과 달리
    # - prev에서 (사라질) curr과 next를 동시에 찾는다.
    def popAfter(self, prev):
        # 삭제시에는 prev에서 2개를 다 구함. curr과 next 순차적으로.
        curr = prev.next
        next = curr.next
        # 삭제시에는 연결끊기 전, 뒤(prev)에서 가는 화살표를 , 앞(next)에서 뒤로 가는 화살표를 바꿔준다.
        # 데이터 교환시 딱히 curr이 필요하지 않다.
        prev.next = next
        next.prev = prev
        self.nodeCount -= 1
        # 하지만, 삭제끝난뒤 그 데이터를 반환해주는 데서 curr이 필요하다.
        return curr.data

    # 삭제는 newNode없이 pos만들어오며, prev를 뽑아 넘기는 것이 똑같다.
    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError('Index out of range')

        prev = self.getAt(pos - 1)
        return self.popAfter(prev)

    # 쓸일이 있으려나 모르겠지만, popAfter와 대칭적으로 작성해준다.
    def popBefore(self, next):
        curr = next.prev
        prev = curr.prev
        prev.next = next
        next.prev = prev
        self.nodeCount -=1
        return curr.data


    def concat(self, L):
        # 시작은 head or tail에서 할 수 있다.
        # 1.
        # 앞쪽 tail(dummy)직전의 실Node가 바라보는 화살표를  
        # 뒤쪽 head.next의 실Node를 바라보게한다. (그게 뒤쪽 빈list의 tail dummy node이어도 상관없다??)
        # - 단방향일 땐, 뒤쪽의 head.next가 [ 빈 리스트라면 None이며, tail도 Node을 가리키므로 ] if L.tail 로 실Node를 바라봐서 list가 빈게 아닐때만 붙혀줌..
        # - 양방향일 땐, L.tail로 끊을 가봤자 dummynode로 존재하는 것처럼됨. -> if L.tail검사 의미없어짐.
        #              뒤쪽L이 비어서(None-head-tail-None) tail dummy node여도 그냥 대입하자.
        #              **왜냐면,, 마지막실Node는 concat하기전에도 tail dummy node를 가리키고 있었기 때문**
        # **앞쪽(self) 맨마지막실Node(tail.prev)와,  뒤쪽(L) 맨앞의 실Node(head.next)의 화살표 교환식이라 생각하자.**
        self.tail.prev.next = L.head.next
        L.head.next.prev = self.tail.prev

        # 붙혀졌다고 가정하고, 꼬리는 덮어쓴다. 같은 tail로서 dummynode는 고정일텐데, 그냥 dummy 덮어쓰기
        self.tail = L.tail
        #  갯수, 그만큼+
        self.nodeCount += L.nodeCount


    
############## Stack 2개
class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size(self) == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]



class LinkedListStack:

    def __init__(self):
        self.data = DoublyLinkedList()

    def size(self):
        return self.data.getLength()

    def isEmpty(self):
        return self.size() == 0 

    def push(self, item):
        # array(list)의 append()와 달리, 
        # 1) 노드 속에 넣은 뒤 2) insertAt n+1자리
        node = Node(item)
        self.data.insertAt( self.size()+1, node)

    def pop(self):
        return self.data.popAt(self.size())

    # dll의 popAt -> popAfter -> curr(node).data까지 가서 return한다.
    # 하지만 getAt -> 다른데서 prev node얻을려는 메서드로서 -> curr의 node까지 만 return하니, 실제데이터 보려면 .data까지
    def peek(self):
        return self.data.getAt(self.size()).data



    


    
        