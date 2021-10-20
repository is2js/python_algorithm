############## 양방향 연결 리스트
class Node:
    # Node는 item과, 화살표 2개(link)를 가진다.
    def __init__(self, item):
        self.data = item 
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        # list생성시에는  외부data없이, count, head Node ,tail Node 만 생성
        self.nodeCount = 0

        self.head=Node(None)
        self.tail=Node(None)
        
        self.head.next = self.tail
        self.head.prev = None
        
        self.tail.next = None
        self.tail.prev = self.head


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
        if pos < 1 and pos > self.nodeCount +1 :
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
        # get 0~n, insert 1~n+1, pop 1~n
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

        # 1) 즉, 앞의 마지막실Node와 뒤 맨앞실Node를 서로 바라보게 연결함.
        self.tail.prev.next = L.head.next
        L.head.next.prev = self.tail.prev
        
        #  2) 꼬리 덮어씀.
        # 붙혀졌다고 가정하고, 꼬리는 덮어쓴다. 같은 tail로서 dummynode는 고정일텐데, 그냥 dummy 덮어쓰기
        # .tail 자체가.. 화살표..역할..
        self.tail = L.tail
        # 3)  갯수, 그만큼+
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



    


    
        


#### ArrayStack 1-1: 괄호 유효성 검사
#expr = "([ㅋㅋㅋㅇㄹ{ㄴㅇㄹ}ㄴㅁㅇㄹ]ㅁㄴㅇ)"
def 괄호_유효성_검사(expr):
    match = {
        ')' : '(',
        '}' : '{',
        ']' : '[',
    }

    S = ArrayStack()

    for c in expr:
        if c in '({[':
            S.push(c)

        elif c in match:
            if S.isEmpty():
                return False
            else:
                t = S.pop()
                if t != match.get(c):
                    return False
                    
    return S.isEmpty()


#### ArrayStack 1-2: 중위->후위표기식 변환
# S='A*(B+C)'
def 중위_To_후위(S):
    prec = {
        '*':3,'/':3,
        '+':2, '-':2,
        '(':1, 
    }


    opStack = ArrayStack()

    answer = ''


    for s in S:
        # 1. 여는괄호만나기
        if s == '(':
            opStack.push(s)
        # 2. 그외 연산자 만나기
        elif s in prec:
            if opStack.isEmpty():
                opStack.push(s)
            else:
                # stack에 연산자가 차있는 상황이라면, 계속 비교판단해야한다.
                # 그게.. 경우에 따라, 
                # 1) 우선순위 높은놈이 peek push되있다? pop&출력 후 -> **그 다음 peek과 비교하는 if루프반복 ->while**
                while not opStack.isEmpty():
                    if prec[opStack.peek()]  >= prec[s]:
                        answer += opStack.pop() 
                # 2) 우선순위 낮은놈이 peek push되있다? 빌때까지?ㄴㄴ break로 빠져나와서, 날 peek으로 push해주면 됨. (내가 수식마지막이라서 pop&출력검사는 맨 나중에 한번 더 함.)
                    else: break
                opStack.push(s)
        # 3. 닫는 괄호만나기
        elif s == ')':
            # peek로 여는 괄호가 나올때까지 모두 pop()~ 없애주도록 update
            while opStack.peek() != '(':
                answer+=opStack.pop() 
            # while특성상 현재 peek ( 여는 괄호 상태다.-> 괄호는 pop으로 날린다.
            opStack.pop()
        # 4. 이제 나머지 피연산자들(숫자 혹은 ABCD)
        # -> 나올때마다 출력만.
        else:
            answer+=s


    # 5. 스택(연산자push)에 남아있는 것은 없는지 확인해서 다 pop & 출력
    while not opStack.isEmpty():
        answer += opStack.pop()

    return answer


#### ArrayStack 1-3: 중위--splitTokens--> 토큰리스트 --ArrayStack->후위표기식(토큰리스트) 변환 후--ArrayStack-->후위표기식 계산
# def solution(expr):
#     tokens = splitTokens(expr)
#     postfix = infixToPostfix(tokens)
#     val = postfixEval(postfix)
#     return val

def splitTokens(exprStr):
    tokens = []

    val = 0 # 직전까지 문자열->10진수 변환값. by <<누적되면서 update변환됨>> 
    valProcessing = False # update시작->끝을 알려주는 변수 # 직전까지의 숫자update여부 (매번 업데이트해줌)

    for c in exprStr:
        # 스페이스는 무시(건너띄기)하기위해 , 맨위쪽에 if continue처리
        if c == ' ':
            continue
        if c in '1234567890':
            # 숫자를 만난 순간부터, 다음것과 연계하여 업데이트된다. 문자열숫자를 10진수 int로 update하는 과정이다.
            # 일단 flag부터 켜준다. 다음이 숫자가 아닐 때, [update끝내고 마무리 ]알려줘야한다.
            valProcessing=True  # 해당과정일 땐, 항상 True를 넣어준다. 아닐때 False로 한번 바뀐다.
            # 직전까지의 -> 현재까지의 수로 update
            val = val*10 + int(c)
        
        else:
            # [숫자가 아닌 곳에 왔을 때,]
            # << 직전까지의 숫자update여부(flag) >> 를 확인해서.. , [숫자계산을 마무리해준다.]
            if valProcessing:
                # 직전까지 숫자였구나.. 이제 아니란다. 마무리하자. # 숫자는 update과정이 끝나고나서야.. append해준다.
                tokens.append(val)
                val=0
            valProcessing=False # 언제바뀔지모르니, 매번 업데이트해준다.  숫자가 아니라면, 아니라고 매번 적어줘야한다.

            tokens.append(c) # 숫자update가 아닐 경우, 바로바로 토큰으로 넣어준다.

    # [숫자가 아닌곳이 아닌.. 바로 끝나는 경우]
    if valProcessing:
        # 숫자update로 끝났다? (후위식은 안그럴듯?) -> 마무리를 따로해주자.
        tokens.append(val)
        # val = 0초기화해줄필요는 없다.
    return tokens


def infixToPostfix(tokenList):
    # 우선순위: 여는 괄호는, 닫힌괄호만날때까지 stack에 있을 수 있게 우선순위를 연산자들에 비해 제일 낮게 준다.
    # -> 대신 만나는 순간, [비교없이] 바로 들어가도록 if문을 제일 위에 선언해준다.
    # 닫는 괄호는 딱히 연산자로서 취급안한다. 만나는 순간 다 빼오는 특이한놈이다.
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    postfixList = []

    opStack = ArrayStack()

    for s in tokenList:
        if s == '(':
            opStack.push(s)
        
        # 우선순위가 있는 연산자들이 들어올 경우, stack에 담거나 비교가 필요함.
        elif s in prec:
            if opStack.isEmpty():
                opStack.push(s)

            else:
                while not opStack.isEmpty():
                    if prec[opStack.peek()] >= prec[s]:
                        postfixList.append(opStack.pop())
                    else: break 

                opStack.push(s) # 높은걸만나서 다 빠지고 맨마지막에 push or 내가 높아서 바로 push
            
        elif s == ')':
            while opStack.peek() != '(':
                postfixList.append(opStack.pop())
            # 열린괄호를 peek에 가져서 while을 빠져나온 상태에서 -> 열린괄호 날리기
            opStack.pop()

        else:
            postfixList.append(s)

    # tokenList를 다돌앗는데, stack에 먼가(연산자가) 남아있따면.. 빼서 넣어주기
    # - 비어서 push된체로 끝났거나 or 비교후 push된 상태로 끝
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return postfixList


# new : 후위 표기식(토큰리스트)을 Arraystack으로 계산하기
# - 연산자들, 여는괄호를 push(중위to후위)하는게 아니라, 피연산자들을 push하면서 연산자 등장시 계산함.
# **계산에 있어서는, 연산자들의 서로간 우선순위보다는, <<피연산자들의 들어간 순서 및 들어간 순서대로 최근 2개 (계산후에도 피연산자취급하여 push된) >> 가 중요하다. **
def postfixEval(postfix_tokenList):
    Stack = ArrayStack()

    for token in postfix_tokenList:
        # 숫자 = 피연산자 -> 일단 push
        if type(token) is int:
            Stack.push(token)

        # 숫자가 아닌 연산자들 -> 종류에 맞게 연산 with pop1,pop2 하여 결과물을 다시 피연산자로서 push
        else:
            b = Stack.pop()
            a = Stack.pop()

            if token == '+':
                Stack.push(a + b)
            elif token == '-':
                Stack.push(a - b)
            elif token == '*':
                Stack.push(a * b)
            elif token == '/':
                Stack.push(a / b)

    # 결국엔 연산하여 결과물 1개값만 남게됨.
    return Stack.pop()

def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val



#### 비추
#### ArrayQueue : dequeue연산 때문에 array(list)로 만든 queue는 비추
class ArrayQueue:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmtpy(self):
        return self.size() == 0 

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0] 

#### 추천
#### LinkedListQueue : dequeue시 pop(0)이 아닌 popAt(1)로서, 각 원소들이 한칸씩 이동할 필요없음.
class LinkedListQueue:

    def __init__(self):
        self.data = DoublyLinkedList()

    def size(self):
        return self.data.getLength()

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        node = Node(item)
        self.data.insertAt(self.size() + 1, node)

    def dequeue(self):
        # queue는 선입선출로 맨첫번째것(queue는 1부터)부터 뺀다.
        # 알아서 popAt내부에서 node -> data까지 반환함.
        return self.data.popAt(1)

    def peek(self):
        # getAt은 popAt과 달리, node내부 item까지 반환하진 않는다. prev node반환용 함수였다..
        # -> 직접  data까지 반환
        return self.data.getAt(1).data 


#### 일반 queue은 dequeue땜시 DLL로 구현
#### 원형 큐는 n수만 정해지면 선형을 연결해서 구현. dequeue시 밀어넣기 필요없어짐.
#    직접 index(포인터)를 이동시키면서 처리함. -> dequeue시 front가 , enqueue시 rear가 -1부터 전진함.
#    정해진 갯수를 가지므로 원형으로 돌아갈 때, 삽입시 확인을 위한 isFull()연산이 추가됨.
class CircularQueue:

    def __init__(self, n):
        self.maxCount = n 
        self.data = [None] * n
        self.count = 0
        self.front = -1
        self.rear = -1 


    def size(self):
        return self.count
    
    def isEmpty(self):
        return self.size() ==0 
        #return self.count ==0 

    # CircularQueue는 갯수제한이 있어, 가득찼는지 확인하고 넣어야한다.
    def isFull(self):
        return self.size() == self.maxCount
        #return self.count == self.maxCount

    def enqueue(self, x):
        if self.isFull():
            raise IndexError("Queue full")
        # 1. rear부터 이동
        # 삽입시에는 마지막index를 +1해주는 동시에, 전체길이 넘어갈 수 있으므로 나머지처리로 인한 초기화
        self.rear = (self.rear+1) % self.maxCount
        # 2. 이동한 rear자리에 데이터 삽입
        self.data[self.rear] = x 
        self.count += 1

    def dequeue(self):
        if self.isEmpty:
            raise IndexError("Queue empty")
        # front index도 rear처럼 사건발생시 전진만 하며 & 환형으로 돌려줘야한다.
        # - 삭제된 값 자리로 뒤에것들이 한칸씩 당기는 것이 아니라, 다음삭제때가 시작되면, 다음 삭제될 value자리의 index로 오른족으로 한칸 옮겨줌. 나머지들이 안움직여도 알아서 삭제됨.
        # [front][첫값][2번재값] ... 상태로 유지되었다가 움직임.
        self.front = (self.front+1) % self.maxCount
        x = self.data[self.front] # 값을 참조만하고 실제 지우진 않음(나중에 덮어쓰기함.)
        self.count -= 1
        return x 

    # 빼는 것과 비슷한데, front를 실제 +1 옮기진 않고 +1가서 값만 꺼내본다.
    def peek(self):
        if self.isEmpty():
            raise IndexError("Queue empty")
        return self.data[ (self.front +1) % self.maxCount ]


#### 우선순위큐 : 삭제 혹은 중간에 삽입(정렬유지enqueue)도 해야하므로 DLL로 구현하는게 좋다.
class PriorityQueue:

    def __init__(self):
        self.queue = DoublyLinkedList()

    def size(self):
        return self.queue.getLength()

    def isEmpty(self):
        return self.size() == 0

    # 우선순위큐의 특징은 삽입시 정렬을 유지한체 해당 자리에만 삽입한다.
    # - 대신 뺄때는 편하게 정렬된 마지막만 빼면 된다.
    def enqueue(self, x):
        newNode = Node(x)

        curr = self.queue.head # 직전까지의 node이며 업데이트 됨.
        # 1) 실Node내에서 2) 데이터x가 curr(직전).next(현재) node와 비교해서, 작다?==우선순위높다?==더 오른쪽으로 건너가야한다.
        while curr.next.data != None and curr.next.data > x:
            curr = curr.next 
        # 지금은 1) 실Node 내에서 현재항(curr.next)보다는 커서..(크거나같아서)  현재항의 자리에 삽입되어야함.
        #       -> 삽입은 insertAt(pos) -> prev등 Node를 얻은 상태에서 삽입은? insertAfter()
        # curr.next 현재항자리에 삽입해야하는데, prev가 필요하므로 curr가 prev다
        # 2) 실Node가 끝난 마지막 상황이라면? curr가 마지막 node다... 
        #    n+1자리에 삽입하는 것이고, curr이 n항이자 prev다.
        # 1), 2)경우 모두 insertAfter(curr, newNode)로 해결된다.
        self.queue.insertAfter(curr, newNode)

    def dequeue(self):
        # 현재 우선순위높을수록(작을수록), 오른쪽에 오도록 정렬해놨으니... 젤 오른쪽꺼 빼면된다.
        return self.queue.popAt(self.queue.getLength())
    
    def peek(self):
        # 데이터를 볼때도 가장 오른쪽 데이터가 나올예정이니 그것으 데이터 보여주면 됨.
        return self.queue.popAt(self.queue.getLength()).data


    










