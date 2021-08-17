import time

loop = 1000000

def solution_A(a, b):
    for i in range(loop):
        sum = 0
        for i in range(a, b+1):
            sum += i
    return sum

def solution_B(a, b):
    for i in range(loop):
        sum = 0
        sum = (a + b) * (a - b + 1) / 2
    return sum


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
        start = time.time()
        result.append(solution[i](a, b))
        duration.append(time.time() - start)

    print(duration)
    print(result)