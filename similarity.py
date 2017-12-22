def similarity (inputWord,wordCorpus):
    
    # get list of words that share the relatively same size +/- 1 letter
    
    if len(inputWord) == 0:
        print ("Please provide a valid word")
        return "INVALID_ENTRY"
    
    lowerWordLen = len(inputWord) - 1
    upperWordLen = len(inputWord) + 1
    
    # get the list of candidate words
    candidateWords = []
    
    for entry in wordCorpus:
        
        if len(entry) >= lowerWordLen and len(entry) <= upperWordLen:
            candidateWords.append(entry)
            
    # perform similarity comparison
    firstTime = True
    bestMatchCount = None
    bestMatchWord = None
    
    print ("Input word:",inputWord)
    for entry in candidateWords:
        matchCount = 0
        for l1 in entry:
            #print "letter:",l1
            if l1 in inputWord:
                matchCount += 1
                
        if firstTime == True:
            bestMatchCount = matchCount
            bestMatchWord = entry
            firstTime = False
        else:
            if matchCount > bestMatchCount:
                bestMatchCount = matchCount
                bestMatchWord = entry
                
    # display the best match
    print ("Best Match Is:", bestMatchWord)