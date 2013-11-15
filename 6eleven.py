import thread

def findSubWordsIn(word,lwords):
    print "Attempting to find subwords for " + word.strip() + "."
    qSubWords = []
    for candidate in lwords:
        candidate = candidate.strip()
        # For now, only use words of 2 or more letters.
        if len(candidate) < len(word) and len(candidate) > 1:
            #print "Checking if " + candidate + " is a substring of " + word
            if -1 != word.find(candidate,0,len(word)):
                if candidate != word:
                    #print "Found candidate: " + candidate
                    qSubWords.append(candidate)
    return qSubWords

words = open("list.txt", "r") #readonly

lwords = []
for word in words:
    lwords.append(word)

qWords = []

for word in lwords:
    word = word.strip()

    #optimization.
    if len(word) != 6:
        continue
    subWords = []
    subWords = findSubWordsIn(word,lwords)
    #subWords = findSubWordsIn("abbas")
    if ( len(subWords) > 10):
        print "Found a wordk with 11+ sub words:"
        print subWords
        collection = []
        collection.append(word)
        collection.append(subWords)
        qWords.append(collection)

print "Results: Words that have been found to have 11 or more subwords within it."
for item in qWords:
    print "*************************************"
    print "'" + item[0] +"' has the following #" + str(len(item[1])) + " of subwords:"
    print item[1]


