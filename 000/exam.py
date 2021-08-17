import time

loop = 1000000

def solution_A():
    sum = 0
    for i in range(101):
        sum += i
    return sum

def solution_B():
    return (1 + 100) * 100 / 2


if __name__ == "__main__":
    solution = []
    duration = []
    result = []

    solution.append(solution_A)
    solution.append(solution_B)

    for i in range(len(solution)):
        result.append(None)
        start = time.time()
        for j in range(loop):
            result[i] = solution[i]()
        duration.append(time.time() - start)

    print(duration)
    print(result)