### 알고리즘 레포지토리
 📂 01_codeup : 기초 100제 중 마지막 배열문제들(6092~6098)
 📂 02_boj : 백준 단계별로 문제 풀기 中 다시 생각해볼 것들(bronze~)
 📜 concept1~6 : 프로그래머스 & 코드잇 기준 개념 정리
 📜 practice1~6 : 프로그래머스 & 코드잇 기준 Lv 1~3 문제들 정리
 
 ![image-20210909211235458](https://raw.githubusercontent.com/is3js/screenshots/main/image-20210909211235458.png)
 
 - 처음 계획은 6가지 알고리즘 패러다임 및 기타 분류별로 정리한 예제를 노트북에 풀어놓는 것입니다.
     1. `정렬과 탐색` : 선형/이진탐색 + 선택/삽입정렬 
     2. `Brute Force` : 전체 다 살펴보는 방식의 문제
     3. `Divide and Conquer` : 재귀 등 부분문제가 있는 살펴보기
     4. `Dynamic Programming` : 부분문제 + 중복되는 문제를 memo(dict, 부분문제 없이 넣고 저장) or tabulation(list, base index 넣어놓고 처음부터, 부분문제가 list[k-1] 등)로 해결하기
     5. `Greedy Algorithm` : 부분문제 + 각 부분이 최대값을 선택했을 때가 정답
     6. `기타` 등 구현 : 기초 개념 및 한번에 생각하기 어려웠운, 배경지식이 필요한 개념.
        - 소수 판별(isPrime2) / 소수 카운팅(에라토스테네스의 체) countPrimes2, findPrimes / 소인수분해 factorize2, 중복제거 소인수 모음 findFactors / 


 - 문제마다 문제설명을 생략하면 재활용이 불가능하다고 판단했기 때문에 `jupyter notebook`형태로 문제 + 풀이 및 `풀이 주석`으로 학습한 것을 정리하고 있습니다.

### Big-O of n 알고리즘 (나올때마다 기록해두기)
 - 이진탐색 : log(n)
    - n의 start or end가 절반씩 줄거나 or 반복문의 index i *= 2 2배로 커지거나 or  n//2 로 절반씩 줌.
    - `str()` log(n)이지만, 자리수d로 표기하면 O(d)
 - 선형탐색 : n
    - x `in` sequence
    - slice
    - `max`, `min`
    - list의 append 제외 `insert, del, index, reverse`
        - append : O(1) - 안움직이고 맨 뒤에 추가만 하면 되므로.
        - slicing([a:b]) : O(b-a) 
        - sort, sorted의 정렬 : nlogn
 - sort, sorted : n log(n)
    - for i  내부에 while j*=2  or  for i  while  i//2 j+=1
 - 합병정렬, 퀵정렬 : n log(n)
 - 재귀 : (재귀인자 포함)재귀내부복잡도 \* 재귀1개당몇번호출(n-1이면 n번, n//2면 log(n)번) \*\*(함수내 재귀호출갯수)
    - 10씩 줄어든다면? log10(n)보다는 자리수d로 O(d)로 나타냄. 10//n ex> 자리수합
    - slicing으로도 재귀호출이 가능하다. ex> 리스트 뒤집기, 이진탐색 by 재귀

 - [그외 정리 블로그](https://wayhome25.github.io/python/2017/06/14/time-complexity/)(초보몽키)




### 알고리즘 패러다임 푸는 요령

```
0 [sort]시 직전애들과 비교하는, 삽입정렬 같은 경우, 0~i-1까지는 이미 정렬된 상태인 것을 생각하자.
 -> 삽입정렬: 각 i번째 값에 대하여 -> i=j와 j-1을 j번째값 기준으로 하나씩 비교해 shift를 끝낸 뒤, i번째값 value의 위치를 정한다.
 ->-> 즉 정렬된 묶음에서 하나를 삽입시키길, 오른쪽에서부터 shift 시켜서 끼워넣는 작전.
 ->-> shift를 for i를 고정시킨 상태에서, j=i + while j-1를 이용한 shift 조건 + j-=1 등으로 왼쪽으로 나아가는 알고리즘.


1. [BruteForce]로 해결되는지 확인한다.
 -> 전체를 다 보는 경우가 많으며, for문이 다돌고 출력해야함. -> for문 끝나고 return하는 방식
 -> 찾는 점이 어딘지 몰라 다 돌면서 매번  확인 + 업데이트 해야한다면? for문 속에서 업데이트 후 -> 최종 업데이트 변수 return(print) -> for문위에 저장할 초기항 변수 : flag  or count or update -> for문위 변수 해석 : 초기항을 넣는 직전까지의 ~한 값(들) -> for문속 해석 : 직전까지의 ~ -> 업데이트 -> 현재까지~ -> for문이 다 끝나면? 최종 ~
 -> 업데이트시 최소값을 구한다치면, 1차원이면 min(,) -> 2차원으로서 1개 변수가 아닌 튜플 or 리스트면, for문마다 min()내장함수처럼 거리구하는 공식을 함수로 만들어서 for문속에서 반복적으로 업데이트 -> 만약, 최소값을 만족시키는 data 2개(이상)를 원한다면, 리스트에 0번 1번으로 가지고 있으면서 업데이트시켜준다!(튜플은 안변하며, 업데이트되면서 변한 것을 넣어줘야하므로 그다음인 list를 자료형으로 가지면서 할당만 다른 값으로 바꿔주자.)
 -> 풀이과정에서 중복만 검사하면 된다면, dict의 memoization고려
 -> 직전까지의 최대/최소값은 for i에서 (활용후) 업뎃해줘야한다.(return 최종업뎃값)
 -> ex> min_so_far = default -> for i -> (활용 후) 업뎃  : min_so_far = min( min_so_far, [i]항=마지막항과 비교하여 업뎃 ) or 업뎃만한 뒤, 바깥에서 return  최종업뎃값
 -> list에서 순서를 가진 2개의 변수가 돌아야한다면! 2중for문 이외에 -> 뒤에것을 기준(for i 고정)해야 앞에것의 최대/최소를 동시에(그 과정에서) 챙겨놓을 수 있다. 
 -> 정렬된list라면, <<이진탐색>>을 먼저 생각하고 / 다른방법으로 <<양끝을 동시에 탐색>>하는데 while (index) low < high low+=1 high-=1 으로 붙이면서 탐색한다.
 -> for i에서 양쪽으로 최대값은 max( array[:i] or array[i:])의 슬라이싱을 활용할 수 있지만, 더 효율적이려면 시복n->공간으로 옮기는 개념이다.
    * 각 i번째마다 left_max, right_max를 저장할  [default 값(0) ]* n 의 빈 리스트를 2개 미리 생성해놓고(왼쪽용, 오른쪽용) 각 i번째마다 0제외 1~(i-1)까지에서의 최대값들 업데이트 / n제외(i+1)~(n-1) 중 최대값 업데이트 list를 각각 2개를 채워서 미리 구해놓는다고 생각한다. <-생각하기 어려움.
    * max(list[:i]) replace : i에서 1~(i-1)까지 중 최대 건물 높이 ->
      for가 돌고 있으니, for문 위 변수(시작항대입[0], 직전(i-1)까지)의 최대 건물높이 저장 -> 현재항(i) 비교없이 그대로 사용
    * max(right [:i]) replace : 문제는 (i+1)~(n-1)까지 중 최대 건물 높이 ->
      for문위변수(시작항대입[-1], 직전까지오면서) + for range(n-2,,-1)을 활용해서 끝(n-2)부터 ->n-3->...-> 시작(-1)까지 오면서 직전항이 i+1로 생각하면서 최대값을 비교하여 업데이트 해나간다.
 -> max(상수,) or min(상수,)로 최소값을 지정한 max값(누적합시 최소값 0) / 최대값을 지정한 최소값을 활용한다. ex> max(0, 음수가 나올지도 모르는 계산) 값을 누적합에 더해줘야할 경우.

2. input에 대한 [부분 문제]가 있는지 [Divide anc conquer]로 살펴본다 
 -> [input을 Divide and Conquer의 재귀]로 해결할 수 있다. **식을 짤 땐, 함수(n-1)을 풀었다고 가정**하고 부분문제들을 conquer한다.
 -> 부분 문제는  input 마지막 경우 = 조건별 부분1 + 부분2 or max(부분1, 부분2) 등으로 **배반**으로 나누어져 풀어진다면 최적의 부분문제다.(부분문제의 조합 = 원래문제 답)
 -> input n을 `n-1, n-2`의 조합 뿐만 아니라 `n//2`의 mid 활용,  `n미포함 n-1부분문제 + n항포함 n-1변형문제`의 정답가정+ n-1부분문제활용n포함문제해결 등 여러가지 경우의 수를 생각한다.
 -> 재귀 : base case 가장 먼저 + (divide) + recursive by 가정+부분 문제조합
 -> value의 중복검사는 if해당범위<= and <= count+= 한 뒤, 범위구간 = 갯수시 중복X , 이진탐색으로 줄여나간다.
 -> 부분문제로 나눌시 탐색범위가 끝만 조정되는게 아니라, 앞뒤가 조정되는 경우, start, end 둘다 받는다.

3. [최적의 부분문제]를 구성한 배반의 부분문제들이 내려가면서 중복되는지 확인한다. -> Dynamic(Memo or Tabul or Tabul공간최적화)
 -> n-1 + n-2등으로 풀리는 부부문제의 경우는 거의 중복된다.
 -> tabulation(부분문제를 list[k-1], list[k-2]로 품)으로 풀거면, base case를 list의 0, 1에 미리 채워놓고, n단계에서 뽑아서 부분해결한 상태로 가정해서 conquer해주면 된다.
 -> memoization(부분문제가 없음)은 default값 없이 시작 + for  if key에있으면 return 없으면 =True 넣기. if에서 해결로직이 완성되었다.
 -> 자료형의 index탐색이 아닌, value값의 범위를 탐색할 때도, start,end의 인자가 필요하다. 특히 이진탐색의 mid활용시 부분문제conquer시 활용을 위해 원래함수에 인자로 존재해야함. 
    - <value탐색>은 이진의 절반 탐색이라도... index가 아니므로  <모든 요소를 돌면서> if 범위로 판단한다. ex> count=0 <모든 요소 for돌면서> if절반범위 count+=1
    - 또한, <value탐색>은 list는 그대로 두고, value의 범위만 바뀐체 탐색을 이어나간다. ex> 중복검사 자체를 list전체돌기 + value만의 범위만 바꿔서 탐색하기 때문에 
 -> 이진 탐색으로 푸는 부분문제는 if 발견시 return왼쪽 / 아니면 return오른쪽 으로 해결한다.

4. 조건별 부분1 + 2 + 3으로 나눈 것 중 배반문제가 아니라 [최대/최소 등 특정조건 1개 선택]이 답인지 확인한다. 조건 중에 최대값을 선택 + 그때의 부분문제가 원래 문제의 답인지 [Greedy algorithm]을 판단해서 푼다.
 -> - greedy는 재귀의 base/recursive는 사라지고 sorted( , reverse=True) or max(부분1, 부분2)로  부분문제 조건최대 택1의 일반 문제다. 직전까지의변수+for+현재항으로변수없뎃
 -> 직전이 있어야하므로, 값에 [0]값을 넣고 시작은 range(1,)부터 하는 sense


6. 기타 기본 알고리즘에 대해서
 -> 소수판단(isPrime2)은 <약수는 짝을 이루니 절반만 탐색>으로 시간을 줄이거나
 -> 2~n까지의 소수 카운팅(찾기) (countPrimes, findPrimes)는  <매번 isPrime2로 찾지말고, 새로운 tabulation방식 + 초기항은 해당하는 것을 주고서 이용하여 탐색범위를 팍팍 줄임(while등장) >로 해결하거나
 -> 소인수분해(factorize2)는 소인수 후보들(2~n-1)을 하나 하나 다뽑아서 돌려서 확인하지말고, < 초기항 2부터 +1씩 확인해나가면서 i의 탐색범위를 루트(n)으로 탐색범위를 줄여서 순차적으로 나가는 것>이 더 빠르다.  n을 //i로 줄여나가니 sieve처럼 배수를 제끼는 것은 factorize1과는 동일하다. 요약 = 소수를 미리 구해놓고 도는 시간 >>> +1씩 증가하더라도 탐색범위를 좁히는 것이 더 빠르다. + 주의사항으로 맨 마지막 n이 1이 아니면 (= 다음 i ~ 루트(n)까지도 안나누어지면, 그냥 그것을 소수로 판단하고 factors에 추가함.)
 -> if문을 썼는데, 재귀처럼 반복된다면 -> while [if재귀문]을 올리고 -> 해석 : [계속 ~ 할때까지] 작성하고 / 그 [더이상 ~ 않는다면, ~가 끝났다면] 으로 해석하면서 while문 끝난 밑으로 내려온다.
   - 이 때, if 문안에서 `한 factor에 대해 n이 줄면서 업데이트 되는 과정`이 있기 때문에 가능한 듯 싶다. 줄면서 업데이트되는 n = 재귀, 부분문제와 상관되는데, while로 해결할 수 있다.
 -> `not in 모으는 곳`을 통해 **없으면 넣어라(append)**를 활용할 수 있음. 사실상 `중복 제거 모으기`라면 set을 써도 되지만...
```


## 문제 소스
 - 프로그래머스, Codeit, inflearn에서 제공되는 기초 및 level 1 ~ level 3 연습문제를 풀이해보겠습니다.

 - 저작권은 해당 사이트에 있습니다.



## 참고
 - master -> main으로 branch 변경
    - local에서 git init했다면, `git checkout -b main`부터 하고 시작.
 - test.py에 문제설명 속 python코드를 가져와 구현해보는 방법을 사용함.