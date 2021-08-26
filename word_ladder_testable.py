import re, os

def getSimilarity(word, targetWord):
  #Returns the number of correct characters in word
  return sum([1 if word[i] == targetWord[i] else 0 for i in range(len(word))])

def getNeighbours(pattern, viableWords, seenWords, potentialWords):
  #Returns all possible mutations of pattern that have not already been seen or found
  return [word for word in viableWords if re.search(pattern, word) and word not in seenWords and word not in potentialWords]

def findPath(targetWord, queue, seen, viableWords):
  #Find words that may be in a path from the end of the first path in queue to targetWord
  word = queue[0][-1]
  path = list(queue[0])
  potentialWords = []
  for i in range(len(word)):
    potentialWords += getNeighbours(word[:i] + "." + word[i + 1:], viableWords, seen, potentialWords)
  if len(potentialWords) == 0: #No new words found
    return 
  for word in potentialWords:
    match = getSimilarity(word, targetWord)
    if match >= len(targetWord) - 1:
      if match == len(targetWord) - 1:
        path.append(word)
      path.append(targetWord)
      return path #Found a path to targetWord
    seen.add(word)
    path.append(word)
    queue.append(list(path)) #Add next paths to check to the queue
    path.pop()

def getPath(startWord, targetWord, blackListWords, intermediateWord, viableWords):
  #Intialise variables to be used for first list of bestPath
  searchQueue = [[startWord]]
  seenWords = set([startWord])
  seenWords.update(blackListWords)

  bestPath = None

  if intermediateWord: #If there is a value for intermediateWord make the statement true and execute the code below
    seenWords.add(targetWord)
    while searchQueue and not bestPath: #Produce a list with range of [startWord ,...., intermediateWord]
      bestPath = findPath(intermediateWord, searchQueue, seenWords, viableWords)
      searchQueue.pop(0) #Remove path just checked from start of queue 
    
    #Intialise variables to be used for the second list of secondPath
    searchQueue = [[intermediateWord]]
    seenWords = set([intermediateWord])
    seenWords.update(blackListWords)
    seenWords.update(set(bestPath))

    secondPath = None

    while searchQueue and not secondPath: #Produce a list with range of [intermediateWord ,...., targetWord]
      secondPath = findPath(targetWord, searchQueue, seenWords, viableWords)
      searchQueue.pop(0) #Remove path just checked from start of queue 

    bestPath += secondPath[1:]
  else: #If there is no input for desired word path execute findPath function with normal parameters [startWord -----targetWord]
    while searchQueue and not bestPath:
      bestPath = findPath(targetWord, searchQueue, seenWords, viableWords)
      searchQueue.pop(0)

  return bestPath

def main(dictionaryFile, startWord, targetWord, intermediateWord, blackListWords):
  #Inputs and validation
  #Dictionary
  dictionaryFile = dictionaryFile.strip()
  if dictionaryFile == '' or (not os.path.exists("./" + dictionaryFile) or not os.path.getsize("./" + dictionaryFile) > 0): #Make sure file exists and is not empty
    print("Dictionary file '" + dictionaryFile + "' does not exist or is empty.")
    return None
  #Start word
  startWord = startWord.strip().lower()
  if len(startWord) < 1:
    print("Start word must contain at least 1 character.")
    return None
  #Build viable word dictionary
  viableWords = []
  with open(dictionaryFile) as wordsFile:
    for wordsFileLine in wordsFile.readlines():
      word = wordsFileLine.rstrip().lower()
      if len(word) == len(startWord):
        viableWords.append(word)
  if startWord not in viableWords: #Check if start word is in dictionary
    print("Start word '" + startWord + "' is not in the dictionary.")
    return None
  #Target word
  targetWord = targetWord.lower()
  if len(startWord) != len(targetWord):
    print("Target word length must have match start word length.")
    return None
  if startWord == targetWord:
    print("Target word must be different to start word.")
    return None
  if targetWord not in viableWords:
    print("Target word '" + targetWord + "' is not in the dictionary.")
    return None
  #Intermediate word
  intermediateWord = intermediateWord.strip().lower()
  if len(intermediateWord) > 0:
    if len(startWord) != len(intermediateWord) :
      print("Intermediate word length must have match start word length.")
      return None
    if intermediateWord == targetWord or intermediateWord == startWord:
      print("Intermediate word must be different to start word and target word.")
      return None
    if intermediateWord not in viableWords:
      print("Intermediate word '" + intermediateWord + "' is not in the dictionary.")    
      return None
  #Blacklist words
  blackListWords = blackListWords.lower().split()
  for word in blackListWords:
    if len(word) != len(startWord):
      blackListWords.remove(word)
      print("Removed '" + word + "' from blacklist for reason: Wrong length.")
      return None
    elif word not in viableWords: 
      blackListWords.remove(word)
      print("Removed '" + word + "' from blacklist for reason: Word not in dictionary.")
      return None
    elif word == startWord: 
      blackListWords.remove(word)
      print("Removed '" + word + "' from blacklist for reason: Word matches start word.")
      return None
    elif word == targetWord:
      blackListWords.remove(word)
      print("Removed '" + word + "' from blacklist for reason: Word matches target word.")
      return None
    elif word == intermediateWord:
      blackListWords.remove(word)
      print("Removed '" + word + "' from blacklist for reason: Word matches intermediate word.")
      return None
  #Initialise blackListWords as a set
  blackListWords = set(blackListWords)

  path = getPath(startWord, targetWord, blackListWords, intermediateWord, viableWords)

  return path