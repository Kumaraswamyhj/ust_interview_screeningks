
def frequency_word(input):

    words = input.split()
    words.sort()
    frequency = {}
    for item in words:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency.items()
