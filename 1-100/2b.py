def count2And5(n):
    twos = 0
    fives = 0
    t = n
    while t % 2 == 0:
        t //= 2
        twos += 1
    f = n
    while f % 5 == 0:
        f //= 5
        fives += 1
    return twos, fives


def solution():
    n = int(input())
    matrix = [[] for i in range(n)]
    for i in range(n):
        matrix[i] = list(map(int, input().split()))
    twos, fives = count2And5(matrix[0][0])


if __name__ == "__main__":
    solution()
