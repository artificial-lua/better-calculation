# a부터 b까지의 합

항상 b는 a보다 크다 가정할 때,
``` python
import time

loop = 1000000

def solution_A(a, b):
    sum = 0
    for i in range(a, b+1):
        sum += i
    return sum

def solution_B(a, b):
    return (a + b) * (b - a + 1) / 2


if __name__ == "__main__":
    solution = []
    duration = []
    result = []

    # b 는 a보다 크다는 전제 하에 원하는 수로 바꿀 수 있다.
    a = 1
    b = 100

    solution.append(solution_A)
    solution.append(solution_B)

    for i in range(len(solution)):
        result.append(None)
        start = time.time()
        for j in range(loop):
            result[i] = solution[i](a, b)
        duration.append(time.time() - start)

    print(duration)
    print(result)
```