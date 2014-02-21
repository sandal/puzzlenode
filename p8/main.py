import json

def getTiles():
    ''' returns a list of tiles from the input2.json file'''
    tileList = []
    with open('input2.json', 'r') as f:
        json_obj = json.load(f)
        
        for tiles in json_obj['tiles']:
            tileList.append(tiles)
    return tileList

def getTileLetters():
    ''' returns a list of tiles from the input2.json file'''
    tileList = []
    with open('input2.json', 'r') as f:
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


def getLetterScore(tile):
    score_dict = getScoreDict(getTiles())
    return score_dict[tile]

def getBoard():
    ''' returns a list of rows with each element containing a integer '''
    with open('input2.json', 'r') as f:
        json_obj = json.load(f)
        board = []
        for row in json_obj['board']:
            tmp = []
            for num in row.split():
                tmp.append(int(num))
            board.append(tmp)
    return board

def validWords():
    ''' returns list of words that '''
    words = []
    with open('input2.json', 'r') as f:
        json_obj = json.load(f)
        for word in json_obj['dictionary']:
            words.append(word)
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
    
validWords = validWords() # words composed of the tiles from the json file
board = getBoard() # 2-d array of integers

highest = 0
highestWord = ''
whichRow = None
whichCol = None
print validWords[-1]
for word in validWords:
    for row in board:
        rowMarker = 0
        shift = 0
        for i in range((len(row)-len(word))):
            columnMarker = i
            index = shift
            section = []
            for char in word:
                section.append(row[index])
                index += 1
                
            shift += 1

            if testScore(word, section) > highest:
                highest = testScore(word, section)
                highestWord = word
                whichRow = rowMarker
                whichCol = columnMarker

            rowMarker += 1
            
def printNewBoard(highestWord, board, whichRow, whichCol):
    output = ''
    trigger = False
    shift = 0

    for row in range(len(board)):
        for col in range(len(board[row])):

            
            if col == whichCol and row == whichRow:
                trigger = True
                output += highestWord[shift]
                
            else:
                output += str(board[row][col])
        output += '\n'
    return output
print printNewBoard(highestWord, board, whichRow,whichCol)
            