import time

loop = 1000000

def solution_A():
    for i in range(loop):
        sum = 0
        for i in range(101):
            sum += i
    return sum

def solution_B():
    for i in range(loop):
        sum = 0
        sum = (1 + 100) * 100 / 2
    return sum


if __name__ == "__main__":
    solution = []
    duration = []
    result = []

    solution.append(solution_A)
    solution.append(solution_B)

    for i in range(len(solution)):
        start = time.time()
        result.append(solution[i]())
        duration.append(time.time() - start)

    print(duration)
    print(result)