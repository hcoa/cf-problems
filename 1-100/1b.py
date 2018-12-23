def convert(coord):
    n = coord
    res = []

    while n > 0:
        rem = n % 26
        if rem == 0:
            res.append('Z')
            n -= 26
        else:
            res.append(chr(64 + rem))
            n -= rem
        n //= 26
    return ''.join(res[::-1])


def to_int(letters):
    result = 0
    alphLen = 26
    st = ord('A')
    for letter in letters:
        result = alphLen * result + (ord(letter) - st + 1)
    return result


def isNum(s):
    return ord(s) >= 48 and ord(s) <= 57


def isCoordinates(row):
    if not row.startswith('R'):
        return False
    i = 1
    while i < len(row):
        if isNum(row[i-1]) and row[i] == 'C':
            return True
        i += 1
    return False

    
def main():
    cnt = int(input())
    while(cnt > 0):
        line = input()
        if isCoordinates(line):
            idx = line.find('C')
            col = int(line[idx+1:])
            row = line[1:idx]
            print(convert(col), row, sep='')
        else:
            i = 0
            while i < len(line):
                if isNum(line[i]):
                    break
                i += 1
            print('R', line[i:], 'C', to_int(line[:i]), sep='')
        cnt -= 1

main()
