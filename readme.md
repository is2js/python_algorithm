## 알고리즘 레포지토리
 ![image-20210828121626358](https://raw.githubusercontent.com/is3js/screenshots/main/image-20210828121626358.png)
 - 처음 계획은 4가지 알고리즘 패러다임 및 기타 분류별로 정리한 예제를 노트북에 풀어놓는 것입니다.
     1. `정렬과 탐색` : 선택정렬, 이진탐색 등 관련 문제
     2. `Brute Force` : 전체 다 살펴보는 방식의 문제
     3. `Divide and Conquer` : 재귀 등 부분문제가 있는 살펴보기
     4. `Dynamic Programming` : 부분문제 + 중복되는 문제를 memo(dict) or tabulation(list)로 해결하기
     5. `Greedy Algorithm` : 부분문제 + 각 부분이 최대값을 선택했을 때가 정답
     6. 기타 `자료 구조` 등 : 자료구조에 집중된 문제들 해결하기


 - 문제마다 문제설명을 생략하면 재활용이 불가능하다고 판단했기 때문에 `jupyter notebook`형태로 문제 + 풀이 및 `풀이 주석`으로 학습한 것을 정리하고 있습니다.

### 알고리즘 패러다임 푸는 요령

```
1. [BruteForce]로 해결되는지 확인한다. -> 모르겠다.
2. input에 대한 [부분 문제]가 있는지 [Divide anc conquer]로 살펴본다 
 -> [input을 Divide and Conquer의 재귀]로 해결할 수 있다.
 -> 부분 문제는  input 마지막 경우 = 조건별 부분1 + 부분2 + 부분3  등으로 **배반**으로 나누어진다면 최적의 부분문제다.(부분문제의 조합 = 원래문제 답)
   
4. [최적의 부분문제]를 구성한 배반의 부분문제들이 내려가면서 중복되는지 확인한다. -> Dynamic(Memo or Tabul or Tabul공간최적화)
  
5. 조건별 부분1 + 2 + 3으로 나눈 것 중 배반문제가 아니라 [최대/최소 등 특정조건 1개 선택]이 답인지 확인한다. 조건 중에 최대값을 선택 + 그때의 부분문제가 원래 문제의 답인지 [Greedy algorithm]을 판단해서 푼다.
 -> 부분문제는 없어지고, sorted(, reverse=True) 등을 이용해서 재귀가 아닌 일반문제로 풀어낸다.
```


## 문제 소스
 - 프로그래머스, Codeit 에서 제공되는 기초 및 level 1 ~ level 3 연습문제를 풀이해보겠습니다.
 - 저작권은 해당 사이트에 있습니다.



## 참고
 - master -> main으로 branch 변경