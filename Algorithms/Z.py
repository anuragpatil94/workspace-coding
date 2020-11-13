def createZArray(text):
    zArr = [0] * len(text)
    left = right = 0
    current = 1
    while current < len(text):
        if current > right:
            left = right = current
            while right < len(text) and text[right] == text[right - current]:
                right += 1
            zArr[current] = right - left
            right -= 1
        else:
            if zArr[current - left] + current - 1 < right:
                zArr[current] = zArr[current - left]
            else:
                left = right = current
                while right < len(text) and text[right] == text[right - current]:
                    right += 1
                zArr[current] = right - left
                right -= 1
        current += 1
    return zArr


def Z(text, pattern):
    arr = createZArray(pattern + "$" + text)
    result = []
    for index, num in enumerate(arr):
        if num == len(pattern):
            result.append(index - len(pattern) - 1)
    return result


tests = [
    ["abxabcabcabyabxabcabcaby", "abcaby", [6, 18]],
    ["abyabcabyabcaby", "abyabcaby", [0, 6]],
]

for test in tests:
    assert Z(test[0], test[1]) == test[2]
