def read_file():

    result = []
    file = open("input_2.txt", "r").readlines()
    for line in file:
        result.append([int(x) for x in line.split()])

    return result

def is_increasing(tab: list) -> bool:

    for i in range(len(tab) - 1):
        if tab[i] >= tab[i + 1] or abs(tab[i] - tab[i + 1]) > 3:
            return False
        
    return True

def is_decreasing(tab: list) -> bool:

    for i in range(len(tab) - 1):
        if tab[i] <= tab[i + 1] or abs(tab[i] - tab[i + 1]) > 3:
            return False
        
    return True

def safe_unsafe(tab: list) -> int:

    result = 0
    for i in tab:
        if is_increasing(i) or is_decreasing(i):
            result += 1

    return result

print(safe_unsafe(read_file()))

def safe_unsafe_dampener(tab: list) -> int:

    result = 0
    for i in tab:
        if is_increasing(i) or is_decreasing(i):
            result += 1
        else:
            for j in range(len(i)):
                tmp = i[:j] + i[j + 1:]
                if is_increasing(tmp) or is_decreasing(tmp):
                    result += 1
                    break

    return result

print(safe_unsafe_dampener(read_file()))