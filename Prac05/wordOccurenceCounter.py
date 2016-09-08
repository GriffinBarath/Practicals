def main():
    WORD_OCCURENCES = {}
    userSentence = str(input("Please enter a sentence containing at least 10 words:"))
    userSentence = str.lower(userSentence)
    seperatedSentence = str.split(userSentence)
    seperatedSentence.sort()
    for word in seperatedSentence:
        if word not in WORD_OCCURENCES:
            WORD_OCCURENCES[word] = 1
        else:
            WORD_OCCURENCES[word] += 1
    longestWordLength = 0
    for entry in WORD_OCCURENCES:
        entryLength = len(entry)
        if entryLength > longestWordLength:
            longestWordLength = len(entry)
    for entry in WORD_OCCURENCES:
        print("{:{}} : {}".format(entry, longestWordLength, WORD_OCCURENCES[entry]))


main()
