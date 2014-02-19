import json

def getTiles():
    ''' returns a list of tiles from the input.json file'''
    tileList = []
    with open('input.json', 'r') as f:
        json_obj = json.load(f)
        
        for tiles in json_obj['tiles']:
            tileList.append(tiles)
    return tileList

def getTileLetters():
    ''' returns a list of tiles from the input.json file'''
    tileList = []
    with open('input.json', 'r') as f:
        json_obj = json.load(f)
        
        for tiles in json_obj['tiles']:
            tileList.append(tiles)
    letterList = []
    for tile in tileList:
        splitTile = list(tile)
        letter = str(splitTile[0])
        letterList.append(letter)
    return letterList
    
def getScoreDict(tiles):
    ''' returns a dictionary with a key value pair letter:score '''
    score_dict = {}
    for tile in tiles:
        split = list(tile)
        score_dict[split[0]] = int(split[1])
    return score_dict
    
score_dict = getScoreDict(getTiles())
def getLetterScore(tile):
    return score_dict[tile]

def getWordScore(word):
    ''' takes a word and returns its score '''
    score = 0
    for char in word:
        char_score = getLetterScore(char)
        score += char_score
    return score

def getBoard():
    ''' returns a list of rows with each element containg a integer '''
    with open('input.json', 'r') as f:
        json_obj = json.load(f)
        
        board = []
        
        for row in json_obj['board']:
            tmp = []
            for num in row.split():
                tmp.append(int(num))
            board.append(tmp)
    return board
    
def getWordList():
    words = []
    with open('input.json', 'r') as f:
        json_obj = json.load(f)
        for word in json_obj['dictionary']:
            words.append(word)
            
    return words
    
def validWords():
    ''' returns list of words that '''
    words = getWordList()
    tiles = getTileLetters()
    validWords = []
    
    for word in words:
        tilesCopy = tiles[:]
        compareWord = ''
        
        for char in word:
            if char in tilesCopy:
                compareWord += char
                tilesCopy.remove(char)
            if compareWord == word:
                validWords.append(word)
    return validWords

def testScore(word, nums):
    ''' nums is a list of integers. word is a valid word of equal length to the nums.
        this will calculate the scoreby multiplying the score of each tile to the 
        corresponding number and adding them up'''
    i = 0
    score = 0
    for num in nums:
        score += getLetterScore(word[i]) * num
        i += 1
    return score

print testScore('tordulaba',[1, 1, 4, 1, 1, 1, 1, 2, 1])
    
validWords = validWords()
board = getBoard()

    
def highestScore(validWords, board):
    highestScore = 0
    
        
    return highestScore, word
print highestScore(validWords, board)