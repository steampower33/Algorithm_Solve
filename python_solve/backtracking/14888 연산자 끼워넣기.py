def calculate(use):
    global nums
    result = nums[0]
    for i in range(len(use)):
        if use[i] == '+':
            result += nums[i+1]
        elif use[i] == '-':
            result -= nums[i+1]
        elif use[i] == '*':
            result *= nums[i+1]
        elif use[i] == '//':
            if result < 0:
                result = abs(result) // nums[i+1]
                result = -result
            else:
                result //= nums[i+1]

    return result

def dfs(depth):
    global n, nums, Operators, visited, result
    if depth == (n-1):
        result.append(calculate(useOperator))
        return
    for i in range(len(Operators)):
        if not visited[i]:
            visited[i] = True
            if Operators[i] == '+':
                useOperator.append('+')
            elif Operators[i] == '-':
                useOperator.append('-')
            elif Operators[i] == '*':
                useOperator.append('*')
            elif Operators[i] == '//':
                useOperator.append('//')
            dfs(depth+1)
            visited[i] = False
            useOperator.pop()

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    OperatorNum = list(map(int, input().split()))
    Operators = list()
    useOperator = list()

    for i in range(4):
        for j in range(OperatorNum[i]):
            if i == 0:
                Operators.append('+')
            elif i == 1:
                Operators.append('-')
            elif i == 2:
                Operators.append('*')
            elif i == 3:
                Operators.append('//')

    visited = [False] * len(Operators)
    result = list()
    dfs(0)

    print(max(result))
    print(min(result))
