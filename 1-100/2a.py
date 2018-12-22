def solution():
    n = int(input())
    progress = []
    while n:
        name, score = input().split()
        score = int(score)
        progress.append((name, score))
        n -= 1

    results = {}
    for player in progress:
        name, score = player
        results[name] = results.get(name, 0) + score

    max_key = max(results, key=results.get)
    max_score = results[max_key]

    final = {}
    for player in progress:
        name, score = player
        final[name] = final.get(name, 0) + score
        if final[name] >= max_score and results[name] == max_score:
            max_key = name
            break
    print(max_key)


if __name__ == "__main__":
    solution()
