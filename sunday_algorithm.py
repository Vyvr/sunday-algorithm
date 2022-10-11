
# ----Finds if pattern matches text, starting from index----#
def matchesAt(text, index, pattern):
    if len(text) < len(pattern):
        return False
    for i in range(0, len(pattern)):
        if text[index + i] != pattern[i]:
            return False
    return True

# ----Adds to array indexes where pattern matches text----#
def reportSuccess(index, matchedIndexes):
    matchedIndexes.append(index)

#----Creates dictionary of last indexes of letters----#
def createPatternLettersDictionary(pattern, patternChars):
    for index, letter in enumerate(reversed(pattern)):
        if letter not in patternChars:
            patternChars[letter] = str(index + 1)
    return patternChars

#----Preprocesses text and patern, returns shift number, if letter not in dictionary return number longer than pattern----#
def preprocess(patternChars, letter, pattern):
    if letter not in patternChars:
        return len(pattern) + 1
    return int(patternChars[letter])


def main():
    text = 'acbabadababbdbabac'
    pattern = 'babac'
    # text = 'ABABBCAACCAWACACAWCCA'
    # pattern = 'BCAACCA'
    # text = 'abbababbabababb'
    # pattern =    'abb'
    patternChars = {}
    startingPos = 0
    matchedIndexes = []

    createPatternLettersDictionary(pattern, patternChars)

    while startingPos < len(text) - len(pattern) + 1:
        if matchesAt(text, startingPos, pattern):
            reportSuccess(startingPos, matchedIndexes)

        if (len(pattern) + startingPos) >= len(text):
            break
        startingPos += preprocess(patternChars,
                                  text[len(pattern) + startingPos], pattern)

    print(matchedIndexes)


if __name__ == "__main__":
    main()
