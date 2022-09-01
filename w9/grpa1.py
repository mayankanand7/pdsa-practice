def constructWord(word, wordList):
    if len(word) == 0:
        l = []
        l.append([])
        return l
    if len(wordList) == 0:
        return wordList

    w = wordList[0]

    if isinstance(w, list):
        return wordList

    wordList.remove(w)

    if word.startswith(w):        
        rw = word[len(w):len(word)]
        if rw in wordList:
            wordList.remove(rw)
            wordList.append([w, rw])

    return constructWord(word, wordList)




word = 'apple'
wordList = ['ap', 'pple', 'app', 'apl', 'appl', 'le', 'ple']
# word = 'constantinople'
# wordList = ['const', 'an', 'tan']
print(constructWord(word, wordList))