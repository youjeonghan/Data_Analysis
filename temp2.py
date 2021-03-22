n = int(input())
numbers = list(map(int, input().split()))
operations = list(map(int, input().split()))
opIdx = ["+", "-", "*", "/"]
min_vvv = []
max_vvv = []


def calculate(a, op, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    else:
        return a // b


def dfs(depth):
    if depth == n - 1:
        if not min_vvv:
            min_vvv.append(numbers[n - 1])
            max_vvv.append(numbers[n - 1])
        else:
            min_vvv = [1]
            max_vvv = [2]
        return

    for i in range(4):
        if operations[i] != 0:
            operations[i] -= 1
            origin = numbers[i + 1]
            numbers[i + 1] = calculate(numbers[i], opIdx[i], numbers[i + 1])
            dfs(depth + 1)
            operations[i] += 1
            numbers[i + 1] = origin


dfs(0)
print(min_vvv, max_vvv)