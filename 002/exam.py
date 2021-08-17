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