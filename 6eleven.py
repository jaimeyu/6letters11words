def findSubWordsIn(word):
    #print "Attempting to find subwords for " + word.strip() + "."
    qSubWords = []
    words = open("list.txt", "r") #readonly
    for candidate in words:
        candidate = candidate.strip()
        #print "Checking if " + candidate + " is a substring of " + word
        if -1 != word.find(candidate,0,len(word)):
            if candidate != word:
                #print "Found candidate: " + candidate
                qSubWords.append(candidate)
    return qSubWords


words = open("list.txt", "r") #readonly

qWords = []

for word in words:
    word = word.strip()

    #optimization.
    if len(word) < 6:
        continue
    subWords = []
    subWords = findSubWordsIn(word)
    #subWords = findSubWordsIn("abbas")
    if ( len(subWords) > 10):
        collection = []
        collection.append(word)
        collection.append(subWords)
        qWords.append(collection)

print "Results: Words that have been found to have 11 or more subwords within it."
for item in qWords:
    print "*************************************"
    print "'" + item[0] +"' has the following subwords:"
    print item[1]


