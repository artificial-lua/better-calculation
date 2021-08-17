# 0부터 임의의 자연수 a까지의 짝수의 합

a가 양의 정수라 가정할 때, 0부터 a까지의 짝수의 합은 보통 아래와 같이 작성된다.
``` python
def solution_A(a):
    sum = 0
    for i in range(a + 1):
        if i % 2 == 0:
            sum += i
    return sum
```
```
2550
```
0부터 a까지 반복하며, 짝수일 경우에만 sum에 합하여 값을 도출해내는 코드이다.  
반복문과 조건문이 들어가 있으므로 실행시간이 상당히 복잡해 진다.

# 등차급수와 이의 적용
고등학교 과정에서는 등차수열을 나타낼 때 시그마를 사용하여 나타낼 수 있다.  
1부터 100까지의 합은 시그마를 사용해 나타내면 아래와 같다.  
<center><img src="https://latex.codecogs.com/png.latex?%5Clarge%20%7B%5Ccolor%7BWhite%7D%20%5Csum_%7Bk%3D1%7D%5E%7B100%7Dk%3D5050%7D"></center>  

<!-- $$\sum_{k=1}^{100}k=5050$$ -->
시그마 아래의 k=1은 수열이 1부터 시작함을 나타낸다.  
시그마 위의 100은 수열 100번째 항까지 더함을 의미한다.  
이를 미지수 n으로 나타내면 아래와 같다.
<center><img src="https://latex.codecogs.com/png.latex?%5Clarge%20%7B%5Ccolor%7BWhite%7D%5Csum_%7Bk%3D1%7D%5E%7Bn%7Dk%7D"></center>  

<!-- $$\sum_{k=1}^{n}k$$ -->
1부터 n까지의 합을 구함을 나타낸다. 또한 위 식은 아래와 같이 변형될 수 있다.
<center><img src="https://latex.codecogs.com/png.latex?%5Clarge%20%7B%5Ccolor%7BWhite%7D%5Csum_%7Bk%3D1%7D%5E%7Bn%7Dk%3D%7Bn%5Ccdot%28n&plus;1%29%5Cover2%7D%7D"></center>  

<!-- $$\sum_{k=1}^{n}k={n\cdot(n+1)\over2}$$ -->
이를 다시 위 100까지의 합을 적용하면 아래와 같다.
<center><img src="https://latex.codecogs.com/png.latex?%5Clarge%20%7B%5Ccolor%7BWhite%7D%5Csum_%7Bk%3D1%7D%5E%7B100%7Dk%3D%7B100%5Ccdot%28100&plus;1%29%5Cover2%7D%7D"></center>  

<!-- $$\sum_{k=1}^{100}k={100\cdot(100+1)\over2}$$ -->  
<em>이 식의 구현은 <strong>[자연수 1\~100의 합](../000)</strong>에서 이미 소개되었다.</em>  

## 처음으로 돌아가서
우리가 원하는 값인 0부터 n까지 짝수의 합을 나타내려 시도하면 아래처럼 생각할 수 있다.
<center><img src="https://latex.codecogs.com/png.latex?%5Clarge%20%7B%5Ccolor%7BWhite%7D%5Csum_%7Bk%3D1%7D%5E%7Bn%7D2k%7D"></center>  

<!-- $$\sum_{k=1}^{n}2k$$ -->  
<em>첫째 항이 0일 때, 의미 없으므로 1로 정한다.</em>  
다만 문제가 있는 식이다. 중요한것은 시그마 위의 n이 n까지가 아닌, n번째 항이라는 것에 주의해야 한다. 위 식을 사용하기 위해서는 실제로 n은 우리가 원하는 자연수 a를 2로 나눈 값이어야 한다.
<center><img src="https://latex.codecogs.com/png.latex?%5Clarge%20%7B%5Ccolor%7BWhite%7Dn%3D%5B%7Ba%5Cover2%7D%5D%2C%5Cquad%5Csum_%7Bk%3D1%7D%5E%7Bn%7D2k%3D2%5Ccdot%7Bn%5Ccdot%28n&plus;1%29%5Cover2%7D%3Dn%5Ccdot%28n&plus;1%29%7D"></center>  

<!-- $$n=[{a\over2}],\quad\sum_{k=1}^{n}2k=2\cdot{n\cdot(n+1)\over2}=n\cdot(n+1)$$ -->  
결과적으로, 우리가 원하는 자연수 a에 대한 0부터의 합의 식은 아래와 같다.
<center><img src="https://latex.codecogs.com/png.latex?%5Clarge%20%7B%5Ccolor%7BWhite%7D%28%7Ba%5Cover2%7D%29%5E2&plus;%7Ba%5Cover2%7D%7D"></center>  

<!-- $$({a\over2})^2+{a\over2}$$ -->  
이 식을 코드로 작성하면 아래와 같다.
``` python
def solution_B(a):
    a = a // 2
    sum = a ** 2 + a
    return sum
```
이와 같이 수열의 합을 사용하면 단순한 조건이 붙은 계산을 반복문 없이 구할 수 있다.

# 비교용 코드
``` python
import time

loop = 100000

def solution_A(a):
    sum = 0
    for i in range(a + 1):
        if i % 2 == 0:
            sum += i
    return sum

def solution_B(a):
    a = a // 2
    sum = a**2 + a
    return sum


if __name__ == "__main__":
    solution = []
    duration = []
    result = []

    # 임의의 양의 정수 a
    a = 100

    solution.append(solution_A)
    solution.append(solution_B)

    for i in range(len(solution)):
        result.append(None)
        start = time.time()
        for j in range(loop):
            result[i] = solution[i](a)
        duration.append(time.time() - start)

    print(duration)
    print(result)
```