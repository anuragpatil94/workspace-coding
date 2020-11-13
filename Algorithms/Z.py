def createZArray(text):
    zArr = [0] * len(text)
    left = right = 0
    current = 1
    while current < len(text):
        # When working outside the Z window
        if current > right:
            # since current is greater than right, we already finised the last
            # search and starting the new search. Hence we move left and right
            # to current and start new window
            left = right = current
            while right < len(text) and text[right] == text[right - current]:
                right += 1
            zArr[current] = right - left
            right -= 1
        # Working Inside the Z Window
        else:
            # We are taking the previously calculated Z Indexes to check if we
            # have a new match that goes beyond the right index. This confirms
            # that next 'n' characters are a match and we would compare after
            # these `n` characters since they don't have to be compared again
            # which helps reducing number of comparisons.
            # example:
            # L----C----R => Cindex + Zindex[C-L]
            # Why Zindex[C-L]? This will give xth letter index from pattern
            # which is appended before text.
            if zArr[current - left] + current - 1 < right:
                zArr[current] = zArr[current - left]
            else:
                # Since we already have compared some indexes from current to
                # right we don't have to compare again.
                # ZWindow starts at C and we check right if it is match.
                left = current
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
