test = ["MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX"]

f = open("input_4.txt", "r").read().splitlines()

def hor_xmas(l: list) -> int:
    result = 0
    for i in range(len(l)):
        for j in range(len(l[i]) - 3):
            if l[i][j:j + 4] == "XMAS" or l[i][j:j + 4] == "SAMX":
                result += 1
    return result

def ver_xmas(l: list) -> int:
    result = 0
    for i in range(len(l) - 3):
        for j in range(len(l[i])):
            word = l[i][j] + l[i + 1][j] +l[i + 2][j] + l[i + 3][j]
            if word == "XMAS" or word == "SAMX":
                result += 1
    return result

def diag_xmas(l: list) -> int:
    result = 0
    for i in range(len(l) - 3):
        for j in range(len(l[i]) - 3):
            word1 = l[i][j] + l[i + 1][j + 1] + l[i + 2][j + 2] + l[i + 3][j + 3]
            word2 = l[i + 3][j] + l[i + 2][j + 1] + l[i + 1][j + 2] + l[i][j + 3]
            if word1 == "XMAS" or word1 == "SAMX":
                result += 1
            if word2 == "XMAS" or word2 == "SAMX":
                result += 1
    return result

print(hor_xmas(f) + ver_xmas(f) + diag_xmas(f))

def cross_xmas(l: list) -> int:
    result = 0
    for i in range(len(l) - 2):
        for j in range(len(l) - 2):
            word1 = l[i][j] + l[i + 1][j + 1] + l[i + 2][j + 2]
            word2 = l[i + 2][j] + l[i + 1][j + 1] + l[i][j + 2]
            if (word1 == "MAS" or word1 == "SAM") and (word2 == "MAS" or word2 == "SAM"):
                result += 1
    return result

print(cross_xmas(f))