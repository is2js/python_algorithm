![alt text](https://img.shields.io/badge/Python-3.8-red.svg)
![alt text](https://img.shields.io/badge/BOJ-Algorithm-blue.svg)

### 레포지토리 생성 목적
 - cf) 기업 interview: 비슷한 알고리즘 본 적 있나요??의 질문을 받은 뒤, 대기업 코딩테스트 수준까지 역량을 끌어올리기 위해 공부 기록을 정리함.
    - 21.09.08 : 03_silver_1316_그룹단어체커(interview)(sorted의 데이터 변환_find_연속된단어)에서 string.find를 이용하여 튀는 index를 찾는 경우?
    - 21.09.22 : doublylinkedlist의 __repr__ 작성시 "->" 챙기는 로직(단)다음것, 양) 다다음 것이 있을때 s+="->" )로 화살표를 출력하는 것 cf) 나는 그냥 '->'.join()으로 사이사이마다 연결함.
    - 21.10.07 : stack문제) 가장 큰 수 - 원본순서기억하면서 넣되, 직전or최근값과 비교(LIFO)해서 나보다 작으면 pop으로 날리기. pop횟수 제한. -> 순서대로 먹는 약을 앞에것과 중복되면pop으로 날리면서 순서대로 unique하게 기억하면서 push하기.
    
 - 작업환경 : `wsl2`, `vscode`
    ![image-20210924073210862](https://raw.githubusercontent.com/is3js/screenshots/main/image-20210924073210862.png)


### 알고리즘 레포지토리 📂(folder/)  📜 (.ipynb)   🐍(.py)
 - 📂 00_algorithm_paradigm
   - 📜 concept01\~06 : 예제를 통한 알고리즘 분류별 개념정리(Codeit, Leetcode, 주니온TV)
   - 📜 practice01\~06 : 예제를 통한 알고리즘 분류별 Lv1~3 문제풀이( Codeit, Leetcode)
   - 🐍 concept6-3-1~7: concept06의 코드만 정리(주니온TV)
 - 📂 01_codeup: 🐍 Codeup기초 100제 중 마지막 배열문제들(6092\~6098)
 - 📂 02_boj_step_to_12: 🐍 백준 단계별 문제풀기 12단계까지 문제 중 시간초과 or 틀린 문제 풀이 및 고찰
 - 📂 03_Datastructure: 🐍 자료구조를 python Class로 구현한 code
 - **📂 04_problems_by_class: 🐍 알고리즘 분류별로 회고(느낀점)을 기록하면서 풀이(~ing)**



### 00레포의 알고리즘 패러다임 푸는 요령
1. `정렬과 탐색` : 선형/이진탐색 + 선택/삽입정렬 
2. `Brute Force` : 전체 다 살펴보는 방식의 문제
3. `Divide and Conquer` : 재귀 등 부분문제가 있는 살펴보기
4. `Dynamic Programming` : 부분문제 + 중복되는 문제를 memo(dict, 부분문제 없이 넣고 저장) or tabulation(list, base index 넣어놓고 처음부터, 부분문제가 list[k-1] 등)로 해결하기
5. `Greedy Algorithm` : 부분문제 + 각 부분이 최대값을 선택했을 때가 정답
6. `기타` 등 구현 : 배경지식이 필요한 기초 구현 문제(주니온TV)
   - 소수 판별(isPrime2) / 소수 카운팅(에라토스테네스의 체) countPrimes2, findPrimes / 소인수분해 factorize2, 중복제거 소인수 모음 findFactors / 공통 소인수 commonFactors -> gcd2 공통소인수들의 누적곱/ math.gcd와 최소공배수 lcm, lcmFromTo / 달력만들기 - 윤년판단(for2월일수) leapyear, 이번달의 일수 daysOfMonth, 해당월 1일의 요일=시작요일 dayOfTheWeek, 전체달력출력 printCalendar / 
7. `추가 기타` 구현 : 콜라츠의 추측 collatz(n) / 로마숫자를 아라비아 숫자로 toArabicNumber, 아라비아숫자를 로마숫자로 toRomanNumber / 스무고개 binary_guess, binary_guess_count/ 홀수 마방진 검사 checkMagic(square), NxN 홀수 마방진 만들기 makeMagicSquare(n) / i부터 끝까지의 배열의 합(재귀) sumOfArray(array, i)

```
0 [sort]시 직전애들과 비교하는, 삽입정렬 같은 경우, 0~i-1까지는 이미 정렬된 상태인 것을 생각하자.
 -> 정렬에서 i번째? i-1까지는 이미 정렬된 상태이다! 직전까지는 정렬된 상태에서  i번재 요소를 가지고 합류시켜 묶어서 정렬하는 삽입정렬.
 -> 삽입정렬: 각 i번째 값에 대하여 -> i=j와 j-1을 j번째값 기준으로 하나씩 비교해 shift를 끝낸 뒤, i번째값 value의 위치를 끼워넣어주는 전략을 쓴다.
 ->-> shift는 for i를 고정(i번째 shift의 기준 value만 고정)시킨 상태에서, j=i + while j-1를 이용한 shift 조건 + j-=1 등으로 왼쪽으로 나아가는 알고리즘.
 -> 합벙정렬: list를 절반으로 나눈뒤, 각 부분문제로 정복했다는 가정하에, list1과 list2를 인덱스i,j를 동시에 while에서 돌면서 작은 순대로 뽑아 정렬
 --> i와 j를 동시에 <비교해가며if>돈다면, fori forj가 아니라 while로 같이 돌리며 + if 각 조건에 맞게 if i+=1  else j+=1 or i+=1, j+=1작전을 쓴다. 이러한 수법은 GCD by 소인수분해 시에도 등장한다.
 --> 증가하는 index에 대하여 while < N and <M 은 둘 중에 하나라도 먼저 끝나면 while문도 종료된다. -> 다돈 것이므로 나머지가 있는 것도 챙겨주자.
 --> while i < and j < 를 동시에 돌면서 조건도 동시에 있다면, 둘 중에 하나가 끝나면 끝인경우다 -> 뭐가 먼저 끝나는지 다돌고 판단해주는 sense
 --> if담에 무조건 else만 생각X 추가적으로 다른 경우의수도 있다면 elif 조건만 주자. else는 모든 배반의 경우라서.. 찝찝.
 -> 퀵정렬 : list가 함수내부에서도 접근되는 것을 이용하여 return이 없는 재귀문제가 됨. list의 맨마지막 값을 기준(pivot)으로 설정하여 그보다 작은 그룹 + pivot + 큰그룹으로 나눠서 divide를 함수내부에서 해주고, small그룹과 big그룹을 각각 분할정복함. 가운데 pivot은 가운데서 유지되며 index를 반환해주는데, 그 index를 기준으로 부분문제들 input이 됨.
 --> index를 input로하는 부분문제들은, base case를 정렬해야될 갯수(end-start+1)가 1개 이하면 정렬안해도된다. 자기자신을 반환하거나 아무것도 안하거나.
 -> 퀵정렬 : input이 index이며 부분 문제에서는 줄어든 값이 들어가야한다. def func(default=상수, 상수가 아니면 default=None주고 함수내부에서 확인)패턴을 사용해서, `default값은 있어서 안줘도 되는데(호출시 입력X), 혹시라도 값을 줄거면(내부에서 재귀적으로 부분문제 풀면서 입력) 그걸로 대체`하도록 하게 하자.

1. [BruteForce]로 해결되는지 확인한다.
 -> 전체를 다 보는 경우가 많으며, for문이 다돌고 출력해야함. -> for문 끝나고 return하는 방식
 -> 찾는 점이 어딘지 몰라 다 돌면서 매번  확인 + 업데이트 해야한다면? for문 속에서 업데이트 후 -> 최종 업데이트 변수 return(print) -> for문위에 저장할 초기항 변수 : flag  or count or update -> for문위 변수 해석 : 초기항을 넣는 직전까지의 ~한 값(들) -> for문속 해석 : 직전까지의 ~ -> 업데이트 -> 현재까지~ -> for문이 다 끝나면? 최종 ~
 -> 업데이트시 최소값을 구한다치면, 1차원이면 min(,) -> 2차원으로서 1개 변수가 아닌 튜플 or 리스트면, for문마다 min()내장함수처럼 거리구하는 공식을 함수로 만들어서 for문속에서 반복적으로 업데이트 -> 만약, 최소값을 만족시키는 data 2개(이상)를 원한다면, 리스트에 0번 1번으로 가지고 있으면서 업데이트시켜준다!(튜플은 안변하며, 업데이트되면서 변한 것을 넣어줘야하므로 그다음인 list를 자료형으로 가지면서 할당만 다른 값으로 바꿔주자.)
 -> 풀이과정에서 1개의 iter를 중복여부만 검사하면 된다면, dict의 key에 T/F로만 확인하는 memoization고려
 -> 직전까지의 최대/최소값은 for i에서 (활용후) 업뎃해줘야한다.(return 최종업뎃값)
 -> ex> min_so_far = default -> for i -> (활용 후) 업뎃  : min_so_far = min( min_so_far, [i]항=마지막항과 비교하여 업뎃 ) or 업뎃만한 뒤, 바깥에서 return  최종업뎃값
 -> list에서 순서를 가진 2개의 변수가 돌아야한다면! 2중for문 이외에 -> 뒤에것을 기준(for i 고정)해야 앞에것의 최대/최소를 동시에(그 과정에서) 챙겨놓을 수 있다. 
 -> 정렬된list라면, <<이진탐색>>을 먼저 생각하고 / 다른방법으로 <<양끝을 동시에 탐색>>하는데 while (index) low < high low+=1 high-=1 으로 붙이면서 탐색한다.
 --> 즉, 이정배(이미정렬된배열)에서의 탐색은, 이진탐색 or < 투포인터 활용 탐색 > 도 고려한다.
 -> for i에서 양쪽으로 최대값은 max( array[:i] or array[i:])의 슬라이싱을 활용할 수 있지만, 더 효율적이려면 시복(슬라이싱, O(n))->공간(변수)으로 옮기는 개념이다.
 --> i번째마다 매번 slicing하여, 직전까지의?(X) << i번재까지 >> 쌓인 << 여태까지의 >> min or max값을 구해왔었다.
 ---> 직전까지의 -> for문위 변수로 업데이트해서 가져다님, 
 ---> 각 i입장에서 직전까지의 -> for문위 변수로 업데이트할때마다, 길이가 정해진 배열에 기록(중요한 것은 각 i상태(입장)에서 <여태까지의>의 minmax등 값을 저장해야함.)
 --> for문위변수 + update를 이용하면, 매번 직전까지의 + 현재까지의 min,max 등의 값을 update할 수 있다. update값을 쟁여놓을 정해진길이의 배열이 있다면, 그 update되는 당시의 min, max값을 저장해놓을 수 있다. 당시의 min,max들을 저장해놓으면, 매번 슬라이싱한 max(list[:i]) 등의 직전까지중 최대값을 slicing없이 쉽게 구할 수 있다.
 ---> 본 문제에서의 각 i가 갖다 쓸 수 있게, <각i입장에서 직전까지의 max>를 미리 만들어놓는다.
    * 각 i번째마다 left_max, right_max를 저장할  [default 값(0) ]* n 의 빈 리스트를 2개 미리 생성해놓고(왼쪽용, 오른쪽용) 각 i번째마다 0제외 1~(i-1)까지에서의 최대값들 업데이트 / n제외(i+1)~(n-1) 중 최대값 업데이트 list를 각각 2개를 채워서 미리 구해놓는다고 생각한다. <-생각하기 어려움.
    * max(list[:i]) replace : i에서 1~(i-1)까지 중 최대 건물 높이 ->
      for가 돌고 있으니, for문 위 변수(시작항대입[0], 직전(i-1)까지)의 최대 건물높이 저장 -> 현재항(i) 비교없이 그대로 사용
    * max(right [:i]) replace : 문제는 (i+1)~(n-1)까지 중 최대 건물 높이 ->
      for문위변수(시작항대입[-1], 직전까지오면서) + for range(n-2,,-1)을 활용해서 끝(n-2)부터 ->n-3->...-> 시작(-1)까지 오면서 직전항이 i+1로 생각하면서 최대값을 비교하여 업데이트 해나간다.
 -> max(상수,) or min(상수,)로 최소값을 지정한 max값(누적합시 최소값 0) / 최대값을 지정한 최소값을 활용한다. ex> max(0, 음수가 나올지도 모르는 계산) 값을 누적합에 더해줘야할 경우.
 -> 조건을 만족시키는 가장 작은 수는? - 무한루프로 1(초기항)부터 시작하며, +1씩 나가면서, 조건을 만족할 때 바로 return(break)해버리면 `가장 작은 수`다.
 --> 조건을 만족하는 두(n)번째 수는? 작은수부터 출발 -> [count변수를 추가]하여, 조건 만족할때마다 +1하면서, 해당 n에서 return(break)한다.
 -> for문을 돌면서 curr(현재까지 -> for문안에서 직전까지)를 update해줄 때, 그 max 상황에서의 (순서모르고 value만 챙기기 가 아닌) index 등의 정보를 다 챙기려면, curr(현재까지의) = max( curr(직전까지의), i번째값)가 아니라 [if문으로 비교 + 값 업데이트 + index변수 추가하여 챙기기] 등 변수추가 + if문으로 교체하여 풀어서 해결해야한다.

2. input에 대한 [부분 문제]가 있는지 [Divide anc conquer]로 살펴본다 
 -> [input을 Divide and Conquer의 재귀]로 해결할 수 있다. **식을 짤 땐, 함수(n-1)을 풀었다고 가정**하고 부분문제들을 conquer한다.
 -> 부분 문제는  input 마지막 경우 = 조건별 부분1 + 부분2 or max(부분1, 부분2) 등으로 **배반**으로 나누어져 풀어진다면 최적의 부분문제다.(부분문제의 조합 = 원래문제 답)
 -> input n을 `n-1, n-2`의 조합 뿐만 아니라 `n//2`의 mid 활용,  `n미포함 n-1부분문제 + n항포함 n-1변형문제`의 정답가정+ n-1부분문제활용n포함문제해결 등 여러가지 경우의 수를 생각한다.
 -> 재귀 : base case 가장 먼저 + (divide) + recursive by 가정+부분 문제조합
 -> value의 중복검사는 if해당범위<= and <= count+= 한 뒤, 범위구간 = 갯수시 중복X , 이진탐색으로 줄여나간다.
 -> 부분문제로 나눌시 탐색범위가 끝만 조정되는게 아니라, 앞뒤가 조정되는 경우, start, end 둘다 받는다.

3. [최적의 부분문제]를 구성한 배반의 [부분문제들이 내려가면서 중복]되는지 확인한다. -> Dynamic(Memo or Tabul or Tabul공간최적화)
 -> n-1 + n-2등으로 풀리는 부분문제의 경우는 거의 중복된다. 참고로 n//2 의 mid활용, merge_sort 등에서 input의 길이로 부분문제를 만드는 경우에는 중복이 없을 수도 있다.
 --> n-1, n-2등의 촘촘한, 다 알아야하는 것은 tabulation -> 공간최적화
 --> tabulation: 1) n과 index를 일치시킨 table(list)에 초기항을 넣어둔다. 2) for문 1개로  초기항이후~n까지 돌면서  부분문제들 & append로 n번째 index의 table을 채운다. 3) table[n]을 반환한다
 --> tabulation의 문제들(최소동전거슬, 계단올라가기)는 (N번째, [단위리스트])의 2가지 인자를 받는 것 같다.
 ----> tabul시, 부분문제의 갯수(3개) > 알 수 있는 초기항(2개) 라면? 초반 문제 풀어나갈 때 n-3 정도에서 음수가 나온다. -> table[음수index]를 방지하기 위해 tabul2) 부분문제로 append전에 table[n]=0초기화 이후, if 필터링해서 +=로 값을 추가한다.
 my) append할 때 필터링이 필요하다면, table.append(0)등으로 초기화해놓고 if필터링: +=를 활용한다.
 ---> table ---> 공간 optimized: 1) 재귀식을 구성하는 부분문제의 갯수만큼 변수를 for문에서 생성 및 업데이트를 유지해야하므로, 초기항 변수도 그만큼 둔다.(n-1도, n-2도 다 <다음항으로 update> 되어야함.) 주로, prev[func(n-2)], curr[func(n-1)]형식이며, 그 중 curr(뒤쪽)값이 반복문을 다 돌고 return할 n번째항이 된다.  2) table처럼 for로 n을 찾아가는 것은 똑같으나, 초기항을보고 curr기준으로 반복문을 다 나왔을 시 n이 되록 전진(for문위변수 update)횟수를 민감하게 잘 판단한다. 3) 반복문동안 n으로 update된 curr변수를 return한다.
 ----> 공간optimized의 기준이 변수a,b중 a(prev)다? == [n=1일 때 a에 맞춰진다] -> a가 input n의 기준이므로 return a
 
 --> n//2, k와 n-k의 부분문제 -> cache를 쓰는 memoization
 -> tabulation(부분문제를 list[k-1], list[k-2]로 품)으로 풀거면, base case를 list의 0, 1에 미리 채워놓고, n단계에서 뽑아서 부분해결한 상태로 가정해서 conquer해주면 된다. 문제는.. n번째 구할떄.. 첨부터 n까지 채워야함 -> 공간 최적화해야함. -> 초기항 확인후, 몇번반복해야할지 초기항~n항으로 판단.
 -> memoization(부분문제가 없음)은 재귀함수가 cache(dict)를 인자로 받으며, recursive case에서는 cache에 있는경우부터 먼저 확인하여 있으면 return하고 당시 함수를 종료시켜야함. 없는경우 나눠서 계산한다. default값 없이 시작 + for  if key에있으면 return 없으면 =True 넣기. if에서 해결로직이 완성되었다. 
 --> base에서도 cache사용, recursive에서 나누기전에 cache확인, 없으면 부분문제 해결후, cache저장후 종료.
 -> 자료형의 index탐색이 아닌, value값의 범위를 탐색할 때도, start,end의 인자가 필요하다. 특히 이진탐색의 mid활용시 부분문제conquer시 활용을 위해 원래함수에 인자로 존재해야함. 
    - <value탐색>은 이진의 절반 탐색이라도... index가 아니므로  <모든 요소를 돌면서> if 범위로 판단한다. ex> count=0 <모든 요소 for돌면서> if절반범위 count+=1
    - 또한, <value탐색>은 list는 그대로 두고, value의 범위만 바뀐체 탐색을 이어나간다. ex> 중복검사 자체를 list전체돌기 + value만의 범위만 바꿔서 탐색하기 때문에 
 -> 이진 탐색으로 푸는 부분문제는 if 발견시 start==end될때까지 돌려야하니 줄어든 절반범위로 찾도록 return 중복찾은쪽의 부분문제 else return 중복못찾은쪽의 부분문제
 --> 이진탐색은, 결국 start == end로 1개 값을 찾을 때까지, 2개 범위(index를 절반 or value범위를 절반) 중 찾은 범위에서 다시 부분문제를 계속 돌리는 구조다.

4. 조건별 부분1 + 2 + 3으로 나눈 것 중 배반문제가 아니라 [최대/최소 등 특정조건 1개 선택]이 답인지 확인한다. 조건 중에 최대값을 선택 + 그때의 부분문제가 원래 문제의 답인지 [Greedy algorithm]을 판단해서 푼다.
 -> greedy는 부분문제(직전항의 정답이용)와의 규칙(택1의 규칙)이 발견되면, for로 <<첨부터 1번에 다>> 돌면서 현재까지 max값을 update하도록 설계되는 것 같다. 규칙만 발견되면 부분문제는 아예 함수내에서 사라짐.
 --> forfor(BF, n**2), for+n//2(DC, nlgn) 등에서 ---> 택1의 규칙만 발견되면 for문1개로 max update(Greedy, n)으로 시간복잡도가 크게 줄어든다.
 --> greedy 등 [직전항과의 규칙 발견]시, <<직전까지의 정답>>뿐만 아니라, <<직전까지의 계산>>도 변수로 받아놓고 update시켜 활용가능함. <<현재의 정답 >> by <<현재의 계산>>을 완성하자.
 --> greedy는 문제에서 주어지는 것이 memo나 tabul과 비슷하게 (N,[단위리스트])형태지만, N이 범주형(N번째 등)가 아니라 숫자형(value)일 수 있으며, (value, [단위리스트])가 부분문제로 안나눠질 수 있다. 그럴 땐 탐욕적 속성이 풀리도록 update해서 풀어버린다. update과정에서 value가 unit_list(역순정렬, greedy)에 의해 기하급수적으로 쪼개진다.
 -> - greedy는 재귀의 base/recursive는 사라지고 sorted( , reverse=True) or max(부분1, 부분2)로  부분문제 조건최대 택1의 일반 문제다. 직전까지의변수+for+현재항으로변수없뎃으로 첨부터 끝까지 해결한다.
 -> 직전이 있어야하므로, 값에 [0]값을 넣고 시작은 range(1,)부터 하는 sense


6. 기타 기본 알고리즘에 대해서
 -> 소수판단(isPrime2)은 <약수는 짝을 이루니 절반만 탐색>으로 시간을 줄이거나
 -> 2~n까지의 소수 카운팅(찾기) (countPrimes, findPrimes)는  <매번 isPrime2로 찾지말고, 새로운 tabulation방식 + 초기항은 해당하는 것을 주고서 이용하여 탐색범위를 팍팍 줄임(while등장) >로 해결하거나
 -> 소인수분해(factorize2)는 소인수 후보들(2~n-1)을 하나 하나 다뽑아서 돌려서 확인하지말고, < 초기항 2부터 +1씩 확인해나가면서 i의 탐색범위를 루트(n)으로 탐색범위를 줄여서 순차적으로 나가는 것>이 더 빠르다.  n을 //i로 줄여나가니 sieve처럼 배수를 제끼는 것은 factorize1과는 동일하다. 요약 = 소수를 미리 구해놓고 도는 시간 >>> +1씩 증가하더라도 탐색범위를 좁히는 것이 더 빠르다. + 주의사항으로 맨 마지막 n이 1이 아니면 (= 다음 i ~ 루트(n)까지도 안나누어지면, 그냥 그것을 소수로 판단하고 factors에 추가함.)
 -> if문을 썼는데, 재귀처럼 반복된다면 -> while [if재귀문]을 올리고 -> 해석 : [계속 ~ 할때까지] 작성하고 / 그 [더이상 ~ 않는다면, ~가 끝났다면] 으로 해석하면서 while문 끝난 밑으로 내려온다.
   - 이 때, if 문안에서 `한 factor에 대해 n이 줄면서 업데이트 되는 과정`이 있기 때문에 가능한 듯 싶다. 줄면서 업데이트되는 n = 재귀, 부분문제와 상관되는데, while로 해결할 수 있다.
 -> `not in 모으는 곳`을 통해 **없으면 넣어라(append)**를 활용할 수 있음. 사실상 `중복 제거 모으기`라면 set을 써도 되지만...
 -> 직전까지 업데이트 변수 or 누적합, 누적곱처럼 누적lcm도 [for문 위 updated될 변수 or 누적변수 = 직전까지의 lcm  + for + 현재lcm으로 업데이트 후 누적 ]을 반복한다.
 -> 두 list에서 공통인 것은 1번만 챙겨야할 경우, if 같으면 챙긴다+둘다 index증가 elif 다른데, i가 작은경우 -> 작은경우를 챙기고 키워준다. 키웠을 때 같아질 수 있으니.! 같아진다면 또 한번만 챙겨야한다! -> else 다른데, j가 작은 경우-> 작은쪽이 100% 홀로남겨지는 놈이니 이놈을 챙기고 키워준다.
 


```
### Big-O of n 알고리즘 (나올때마다 기록해두기)
 - 이진탐색 : log(n)
    - n의 start or end가 절반씩 줄거나 or 반복문의 index i *= 2 2배로 커지거나 or  n//2 로 절반씩 줌.
    - `str()` log(n)이지만, 자리수d로 표기하면 O(d)
 - 선형탐색 : O(n)
    - x `in` sequence
    - slice
    - `max`, `min`
    - list의 append 제외 `insert, del, index, reverse`
        - append : O(1) - 안움직이고 맨 뒤에 추가만 하면 되므로.
        - slicing([a:b]) : O(b-a) 
        - sort, sorted의 정렬 : nlogn
 - sort, sorted : n log(n)
    - for i  내부에 while j*=2  or  for i  while  i//2 j+=1
 - 합병정렬, 퀵정렬 : O(n log(n))
    - 삽입정렬, 거품정렬 : O(n^2)
 - 재귀 : (재귀인자 포함)재귀내부복잡도 \* 재귀1개당몇번호출(n-1이면 n번, n//2면 log(n)번) \*\*(함수내 재귀호출갯수)
    - 10씩 줄어든다면? log10(n)보다는 자리수d로 O(d)로 나타냄. 10//n ex> 자리수합
    - slicing으로도 재귀호출이 가능하다. ex> 리스트 뒤집기, 이진탐색 by 재귀

 - [그외 정리 블로그](https://wayhome25.github.io/python/2017/06/14/time-complexity/)(초보몽키)


### 정렬 종류별 사용법
1. 선택정렬 : 간단한 아이디어지만 O(N^2)으로 안쓴다.
2. 삽입정렬 : 데이터가 정렬된 상태라면, 빠르게 작동할 수도 있다. O(N^2)
3. **퀵정렬 : 대부분의 경우에 적합하고 빠르다. O(NlgN)**
4. **계수정렬 : input이 중복되면서&너무많이 들어올 때, `범위가 제한되어 index로 표기가능`할 때, input을 index로 간주하고 counting만 해준다. O(N+K) 매우 빨라짐.**
    - 음수도 k+음수범위로 올려서 사용가능하다.(또다른 배열에 나열시킬 때, -1 곱할시 순서 바뀜 주의)
    - 나는 enumerate로 idx와 val을 받은 뒤, idx의 갯수를 살릴 때 [idx] * val로 2차원이 되지만, 그 갯수를 살리려고 list화 시켜서 통계학으로 사용함.


### stack과 queue 구현시 자료구조
- stack : list로 충분함(push, pop, peek이 **중간에 삽입/삭제가 없음. -> 하나씩 밀거나 당길일 없음.**)
- **queue** : dequeue시 맨앞삭제시 한칸씩 앞으로 다 이동해야해서 -> linkedList로 제거후 link뗐다 붙혔다가 빠름.
- 환형큐 : list로 충분함. 중간에 삽입/삭제도 **front,rear index가 움직이면서 알아서 처리함 -> 하나씩 밀거나 당길일 없음.**.
- 우선순위큐 :  일반큐(dequeue로 인한 한칸씩밀어주기로 -> 양방향 연결리스트를 선호)와 enqueue만 다르다. 
  - **enqueue**시에도 양방향 연결리스트로  정해진 우선순위 자리를 찾아가, 중간 삽입을 해준다.
  - **그외 메소드들은 queue 와 동일하다.**


### 문제 소스
 - 프로그래머스, CodeUp, Codeit, inflearn에서 제공되는 기초 및 level 1 ~ level 3 연습문제를 풀이해보겠습니다.
     - codeup : while조건 속에서 우선시되는 조건은 if elif else 의 위쪽우선순위로 올려놓으면 알아서 다음루프에서 우선순위부터 처리가 된다. 다만, 탈출조건은 가장 먼저 
 - 저작권은 해당 사이트에 있습니다.



### 참고
 - master -> main으로 branch 변경
    - local에서 git init했다면, `git checkout -b main`부터 하고 시작.
 - test.py에 문제설명 속 python코드를 가져와 구현해보는 방법을 사용함.
