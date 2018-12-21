def round_winner(progress):
    name = list(progress.keys())[0]
    score = progress.pop(name)
    for n, s in progress.items():
        if s > score:
            name = n
            score = s
    return name, score


def solution():
    n = int(input())
    first_winner = None
    progress = {}
    while n:
        name, score = input().split()
        score = int(score)
        first_winner = round_winner(progress)
        progress[name] = progress.get(name, 0) + score
    return first_winner


def main():
    solution()

if __name__ == "__main__":
    main()
