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


def getLetterScore(tile):
    score_dict = getScoreDict(getTiles())
    return score_dict[tile]

def getBoard():
    ''' returns a list of rows with each element containing a integer '''
    with open('input.json', 'r') as f:
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
    with open('input.json', 'r') as f:
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
def flipBoard(board):
    return map(list, zip(*board))
def unFlipBoard(flipBoard):
    return map(list, zip(*flipBoard))
    
validWords = validWords() # words composed of the tiles from the json file
board = getBoard() # 2-d array of integers
flipBoard = flipBoard(board)

highest = 0
highestWord = ''
whichRow = None
whichCol = None

is_board_flipped = None
# the following will give the highest word and the location of the highest scoring word
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
                is_board_flipped = True
            rowMarker += 1
    
    # this loop will determine the highest word for words going top down 
    for row in flipBoard: 
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
                is_board_flipped = False
            rowMarker += 1
# this will print a string of the board with the word in the correct location
def printNewBoard(highestWord, board):
    output = ''
    trigger = False
    shift = 0

    for row in range(len(board)):
        for col in range(len(board[row])):
                
            output += str(board[row][col])
        output += '\n'
    return output
def returnBoard(board, highestWord):
    for i in range(len(highestWord)):
        board[whichRow][whichCol+i] = highestWord[i]
    board = printNewBoard(highestWord, board)
    return board

def returnFlipBoard(flipBoard, highestWord):
    for i in range(len(highestWord)):
        flipBoard[whichRow][whichCol+i] = highestWord[i]
    temp = unFlipBoard(flipBoard)
    board = printNewBoard(highestWord, temp)
    print board
if is_board_flipped:
    ans = returnBoard(board, highestWord)
else:
    ans = returnFlipBoard(flipBoard,highestWord)
with open('output.txt', 'w')as f:
    f.write(ans)
    