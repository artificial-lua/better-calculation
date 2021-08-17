# better-calculation

1부터 100까지 더하는 파이썬 코드는 보통 아래와 같이 작성된다.
``` python
# solution A
sum = 0
for i in range(1, 101):
    sum += i

print(sum)
```
```
5050
```
1부터 100까지 순서대로 합하는 간단한 코드이다.

아래는 위 코드의 반복문을 생략하고 작성한 코드이다
``` python
# solution B
sum = (1 + 100) * 100 / 2
print(sum)
```
```
5050.0
```
1과 100을 더하여 한 쌍을 만들고, 100만큼 반복한 뒤, 두 수가 한 쌍이므로 2로 나누는 식이다.
반복문 없이 단순 계산으로 1부터 100까지의 합을 얻었으며, 실행 속도 역시 100배 정도의 차이를 보인다.

반복문을 사용한 단순 계산은 일반적으로 프로그래밍을 학습할 떄 반복문에 익숙해지기 위해 사용하는 코드이지만, 프로그래밍에 익숙해진 다음은 단순계산에 대해 수학적 사고가 필요하다.  

<strong>[#000](000)</strong> : 자연수 1~100의 합  
<strong>[#001](001)</strong> : 자연수 a~b의 합
